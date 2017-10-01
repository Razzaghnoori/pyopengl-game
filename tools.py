import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

Objects = []

def add_object(obj):
    global Objects
    Objects.append(obj)

def isColided(obj1, obj2, trans1, trans2, rotat1, rotat2, scale1, scale2, algorithm='cylinder'):
    safe_zone = 0
    if algorithm == 'cylinder':
        if euclidean(trans1, trans2) < obj1.bounding_radius * scale1 + obj2.bounding_radius * scale2 + safe_zone:
            return True
        else:
            return False

    elif algorithm == 'euclidean':
        legal_dist = min(obj1.max_x - obj1.min_x, obj1.max_z - obj1.min_z) / 100
        Vs = np.array(obj1.vertices)[:int(0.01 * len(obj1.vertices))]
        Us = np.array(obj2.vertices)[:int(0.001 * len(obj2.vertices))]
        
        Vs = fromHomogeneous(toHomogeneous(Vs).dot(mat1.T))
        Us = fromHomogeneous(toHomogeneous(Us).dot(mat2.T))
        
        for v in Vs:
            for u in Us:
                if euclidean(u, v) < legal_dist:
                    #print v, u
                    return True
        return False


def euclidean(u, v):
    return np.sqrt(np.sum((u-v)**2))

def l2(v):
    if v.ndim == 1:
        v = v.reshape(1, -1)
    return np.sqrt(np.sum(v**2, axis=1))

def toHomogeneous(arr):
    return np.hstack([arr, np.ones(arr.shape[0]).reshape(-1,1)])
def fromHomogeneous(arr):
    return (arr / arr[:, 3].reshape(-1, 1))[:, :3]

def show_text(font, text, color, screen, text_surface):
    del text_surface
    text_surface = font.render(text, 1, color)
    screen.blit(text_surface, (10, 10))
    return text_surface

def gravity(velocities, ms=1, g=10):
    out = np.array(velocities)
    if out.ndim == 1:
        out[1] -= 0.001 * g * ms
    else:
        out[:, 1] -= 0.001 * g * ms
    return out

def move(poses, velocities, ms=1):
    velocities = gravity(velocities, ms)
    return poses + ms * velocities, velocities



##################################################
# CLASSES
##################################################

quad = gluNewQuadric()

class Explode():
    def __init__(self, obj, speed=1, scale=1):
        self.verts = np.array(obj.vertices)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        self.indices = np.random.permutation(len(obj.faces))[:min(500, len(obj.faces))]
        self.obj = obj
        self.speed = speed
        self.scale = scale

    def time(self, time_):
        glPushMatrix()
        scale = self.scale * time_ * 5
        glScalef(scale, scale, scale)
        # glColor4f(1, 1, 1, 1./(time_+1))
        # gluSphere(quad, 2, 20, 20)
        self.obj.velocities /= 1.5
        gl_list = glGenLists(1)
        glNewList(gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        for f in self.indices:
            face = self.obj.faces[f]
            vertices, normals, texture_coords, material = face
            mtl = self.obj.mtl[material]

            trans = gravity(self.obj.velocities[f], 20000) * time_

            if 'texture_Kd' in mtl:
                # use diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            else:
                # just use diffuse colour
                glColor(*mtl['Kd'])
                    
            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.obj.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.obj.texcoords[texture_coords[i] - 1])
                glVertex3fv(self.verts[vertices[i] - 1] + trans)
            glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()

        glCallList(gl_list)
        glPopMatrix()
        


class Bullet():
    def __init__(self, point, direction, env, velocity=5):
        self.direction = direction / l2(direction) 
        self.point = np.array(point)
        self.time_ = 0
        self.velocity = velocity
        self.env = env
        self.point[1] = 2
        self.radius = 0.1
        add_object(self)

    def time(self):
        self.pos,_ = move(self.point, self.velocity * self.direction, 3 * self.time_)
        if not ((self.env.min_x < self.pos[0] < self.env.max_x) and
                (self.env.min_z < self.pos[2] < self.env.max_z) and
                (self.pos[1]>0)):
            del self
            return
        glColor((1, 0, 0))
        glPushMatrix()
        glTranslate(self.pos[0], self.pos[1], self.pos[2])
        gluSphere(quad, self.radius, 5, 5)
        glPopMatrix()
        glColor((1,1,1))
        self.time_ += 1

    def hit(self, obj, trans, rotate, scale):
        for lamb in range(100):
            if euclidean(self.point + lamb * self.direction, trans) < 2.5:
                return True
        return False
