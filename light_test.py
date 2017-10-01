from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *

import pygame

pygame.init()
srf = pygame.display.set_mode((800, 800), OPENGL | DOUBLEBUF)

quad = gluNewQuadric()
clock = pygame.time.Clock()

glLightfv(GL_LIGHT0, GL_POSITION,  (0, 4, 0, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
#glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
#glLightfv(GL_LIGHT0, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded


# glLightfv(GL_LIGHT1, GL_POSITION,  (0, 4, 0, 1.0))
# glLightfv(GL_LIGHT1, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
# glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
# glLightfv(GL_LIGHT1, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
# glEnable(GL_LIGHT1)



while True:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()

    glColor4f(1,0,0,1)
    gluSphere(quad, 0.5, 20, 20)

    pygame.display.flip()
