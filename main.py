
# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out


# IMPORT OBJECT LOADER
from objLoader import *
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys, pygame
import numpy as np
import time
import tools


from math import sin, cos, atan, radians, degrees

pygame.init()
pygame.mixer.init()

width = 800
height = 600
shooting_path = os.path.join('sounds', 'gun.wav')
background_path = os.path.join('sounds', 'light_of_the_seven.mp3')
speech_path = os.path.join('sounds', 'WALLE.wav')
has_background_sound = has_shooting_sound = has_speech_sound = True
font = pygame.font.SysFont('monospace', 30)
text_surface = 0
viewport = (width, height)
hx = viewport[0]/2
hy = viewport[1]/2

pygame.display.gl_set_attribute(GL_STENCIL_SIZE, 8)
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)


hour = time.localtime().tm_hour / 24.
brightness = -abs(hour - 0.5) + 1
view = 'third'
num_lights = 5
num_terrors = 5
nitro = 1
sound = dict()
background_music = background_path
screenshot_dir = 'screenshots'
Bullets = []
Dead = [False] * num_terrors
time = [0] * num_terrors
hit = False

white = (1, 1, 1)
black = (0, 0, 0)
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
gray = (0.5, 0.5, 0.5)

sound['gun'] = pygame.mixer.Sound(shooting_path)
sound['Wall-E'] = pygame.mixer.Sound(speech_path)
sound['Eve'] = pygame.mixer.Sound(os.path.join('sounds', 'Eve.wav'))
sound['explosion'] = pygame.mixer.Sound(os.path.join('sounds', 'Explosion.wav'))

if has_background_sound:
    pygame.mixer.music.load(background_path)
    pygame.mixer.music.play(-1)

glClearColor(1 * brightness, 1 * brightness, 1 * brightness, 1.)

# LOAD OBJECT AFTER PYGAME INIT
CT = OBJ('Texture', 'Wall-Elowpoly.obj')
street = OBJ('textures', 'Street_environment_V01.obj')
terror = OBJ('mario_luigi_textures', 'Luigi_obj.obj')
light= OBJ('light_textures', 'Gamelantern_updated.obj')

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5

cam_pos = np.zeros(3)
ct_pos = np.array([0., 0., 0.])
ct_angle = 0
move_step = 0.2

terror_pos = np.random.rand(num_terrors, 3)
terror_pos[:,1] = 0
terror_destination = np.random.rand(num_terrors, 3)
terror_angle = np.random.rand(num_terrors) * 360
for i in range(num_terrors):
    terror_x = terror_pos[i,0] * (street.max_x - street.min_x) + street.min_x
    terror_z = terror_pos[i,2] * (street.max_z - street.min_z) + street.min_z
    terror_pos[i] = terror_x, 0, terror_z

    terror_x = terror_destination[i,0] * (street.max_x - street.min_x) + street.min_x
    terror_z = terror_destination[i,2] * (street.max_z - street.min_z) + street.min_z
    terror_destination[i] = terror_x, 0, terror_z

terror_explode = tools.Explode(terror, 0.1, 0.02)

light_pos = np.random.rand(num_lights, 4)
for i in range(num_lights):
    light_x = light_pos[i,0] * (street.max_x - street.min_x) + street.min_x
    light_z = light_pos[i,2] * (street.max_z - street.min_z) + street.min_z
    light_pos[i] = light_x, 1.75, light_z, 1






rotate = move = False

while 1:
    clock.tick(30)


    glLightfv(GL_LIGHT0, GL_POSITION,  (0, 3, 0, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded


    # direction = np.array([0,-1,0])
    # for i in range(num_lights):
    #     direction = [0.0, -1.0, 0.0]
    #     spotAngle = 20
    #     lightColor = [1, 1, 1, 1]
    #     glEnable(GL_LIGHTING)
    #     glEnable(GL_LIGHT1)
    #     glMatrixMode(GL_MODELVIEW)
    #     glPushMatrix()
    #     glLoadIdentity()
    #     glLightfv(GL_LIGHT1, GL_POSITION, light_pos[i])
    #     glLightfv(GL_LIGHT1, GL_SPECULAR, lightColor);
    #     glLightfv(GL_LIGHT1, GL_DIFFUSE, lightColor);
    #     glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, spotAngle)
    #     glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, direction)
    #     #glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 2.0);
    #     glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 2)
    #     glPopMatrix()


    # glLightfv(GL_LIGHT1, GL_POSITION,  (ct_pos[0], 4, ct_pos[1], 1.0))
    # glLightfv(GL_LIGHT1, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    # glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    # glLightfv(GL_LIGHT1, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
    # glEnable(GL_LIGHT1)

    ##################################################
    # KEYBOARD
    ##################################################
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        direction = np.array([-sin(radians(ct_angle)), 0, -cos(radians(ct_angle))]) * move_step * nitro
        colide = False
        inMap = ((street.min_x < (ct_pos + direction)[0] < street.max_x) and (street.min_z < (ct_pos + direction)[2] < street.max_z))
        for t in range(num_terrors):
            if not Dead[t] and tools.isColided(CT, terror, ct_pos + direction, terror_pos[t], 0, 0, 0.01, 0.02):
                colide = True
        if not colide and inMap:
            ct_pos += direction
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        direction = np.array([sin(radians(ct_angle)), 0, cos(radians(ct_angle))]) * move_step
        colide = False
        inMap = ((street.min_x < (ct_pos + direction)[0] < street.max_x) and (street.min_z < (ct_pos + direction)[2] < street.max_z))
        for t in range(num_terrors):
            if not Dead[t] and tools.isColided(CT, terror, ct_pos + direction, terror_pos[t], 0, 0, 0.01, 0.02):
                colide = True
        if not colide and inMap:
            ct_pos += direction
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #old_ct_angle = ct_angle
        ct_angle += 2
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #old_ct_angle = ct_angle
        ct_angle -= 2

    ##################################################
    # MOUSE
    ##################################################
    mouse_pos = list(pygame.mouse.get_pos())
    mouse_pos[0] /= float(width)
    mouse_pos[1] /= float(height)
    mouse_pos = np.array(mouse_pos)
    mouse_pos *= 2
    mouse_pos -= 1
    ct_angle += mouse_pos[0] * -1

    #########################
    # Terror Movement
    #########################
    for i in range(num_terrors):
        inMap = ((street.min_x < terror_pos[i, 0] < street.max_x) and (street.min_z < terror_pos[i, 2] < street.max_z))
        if tools.euclidean(terror_pos[i], terror_destination[i]) < 1 or not inMap:
            terror_destination[i] = np.random.random(3)
            terror_x = terror_destination[i,0] * (street.max_x - street.min_x) + street.min_x
            terror_z = terror_destination[i,2] * (street.max_z - street.min_z) + street.min_z
            terror_destination[i] = [terror_x, 0, terror_z]

    terror_direction = terror_destination - terror_pos
    terror_direction /= tools.l2(terror_direction).reshape(-1,1)
    terror_pos += terror_direction * move_step
    angle_difference = (np.degrees(np.arctan(terror_direction[:,0]/terror_direction[:,2])) - terror_angle)
    angle_difference[angle_difference < 0] += 360
    terror_angle += angle_difference * 0.2


    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                sys.exit()
            if e.key == K_LSHIFT:
                nitro = 5
            if e.key in [K_PRINT, K_p]:
                glPixelStorei(GL_PACK_ALIGNMENT, 1)
                pixels = pygame.image.save(srf, os.path.join(screenshot_dir, str(int(time.time())) + '.jpg'))
            if e.key == K_v:
                if view == 'first':
                    view = 'third'
                elif view == 'third':
                    view = 'first'
                elif view == 'top':
                    view = 'third'
            if e.key == K_t:
                view = 'top'
            if e.key == K_1:
                if has_speech_sound:
                    sound['Wall-E'].play()
            if e.key == K_2:
                sound['Eve'].play()
        elif e.type == KEYUP:
            if e.key == K_LSHIFT:
                nitro = 1
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1:
                bullet = tools.Bullet(ct_pos, direction, street)
                Bullets.append(bullet)
                if has_shooting_sound:
                    sound['gun'].play()
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()



    if view == 'third':
        cam_pos = ct_pos - np.array([sin(radians(ct_angle+180)), -0.7, cos(radians(ct_angle + 180))]) * 3
        gluLookAt(cam_pos[0], cam_pos[1], cam_pos[2],
                  ct_pos[0], 0, ct_pos[2],
                  0, 1, 0)
        #tools.show_text(font, 'THIRD PERSON', gray, srf, text_surface)
    elif view == 'first':
        cam_pos = ct_pos + np.array([sin(radians(ct_angle+180)), 1.5, cos(radians(ct_angle + 180))]) * 1
        look_pos = ct_pos + np.array([sin(radians(ct_angle+180)), 0.5, cos(radians(ct_angle + 180))]) * 3
        gluLookAt(cam_pos[0], cam_pos[1], cam_pos[2],
                  look_pos[0], look_pos[1], look_pos[2],
                  0, 1, 0)
        #tools.show_text(font, 'FIRST PERSON', gray, srf, text_surface)
    elif view == 'top':
        gluLookAt(ct_pos[0], zpos, ct_pos[2], ct_pos[0], ct_pos[1], ct_pos[2], 1, 0, 0)
        #tools.show_text(font, 'TOP VIEW', gray, srf, text_surface)

    # RENDER OBJECT
    # glTranslate(tx/20., ty/20., - zpos)
    #glRotate(ry, 1, 0, 0)
    #glRotate(rx, 0, 1, 0)

    glCallList(street.gl_list)

    glPushMatrix()
    glTranslate(ct_pos[0], ct_pos[1], ct_pos[2])
    glRotate(ct_angle, 0, 1, 0)
    glScalef(0.01, 0.01, 0.01)
    glCallList(CT.gl_list)
    glPopMatrix()

    for i in range(num_terrors):
        if Dead[i]:
            continue
        glPushMatrix()
        #rdeg = atan(float(terror_x - ct_pos[0])/(terror_z - ct_pos[2]))
        #deg = degrees(rdeg) + 180
        glTranslate(terror_pos[i,0], 0, terror_pos[i, 2])
        glRotate(terror_angle[i], 0, 1, 0)
        glScalef(0.02, 0.02, 0.02)
        glCallList(terror.gl_list)
        glPopMatrix()

    for i in range(num_lights):
        glPushMatrix()
        glTranslate(light_pos[i,0], light_pos[i, 1], light_pos[i, 2])
        glScalef(4, 4, 4)
        glCallList(light.gl_list)
        glPopMatrix()

    for obj in tools.Objects:
        obj.time()

    if pygame.time.get_ticks() % 1 == 0:
        for t in range(num_terrors):
            if Dead[t] and time[t] == 0:
                continue
            for i in range(len(Bullets)):
                if Bullets[i].hit(terror, terror_pos[t], 0, 0.02):
                    if time[t] == 0:
                        hit = True
                    if time[t] == 10:
                        time[t] = 0
                        del Bullets[i]
                        break

                    Dead[t] = True

                    if time[t] < 10:
                        glPushMatrix()
                        glTranslate(terror_pos[t][0], terror_pos[t][1], terror_pos[t][2])
                        terror_explode.time(time[t])
                        glPopMatrix()
                        time[t] += 1

    if hit:
        sound['explosion'].play()
        hit = False


    pygame.display.flip()


if __name__ == "__main__":
    start(600, 800, 1, 1, 1, 'sounds/light_of_the_seven.mp3', 'sounds/WALLE.wav', 'sounds/gun.wav')
