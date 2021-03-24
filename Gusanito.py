from OpenGL.GL import *
from glew_wish import *
import glfw
import random
from math import *

class Gusanito:
    posX = 0.0
    posY = 0.0

    velocidad = 0.15

    def __init__(self, x, y):
        self.posX = x
        self.posY = y

    def actualizar(self, deltatime, gusanito1, gusanito2, gusanito3, gusanito4, gusanito5):
        movimiento = self.velocidad * deltatime

        gusanito1.posX = gusanito1.posX + movimiento
        gusanito2.posX = gusanito2.posX - movimiento
        gusanito3.posX = gusanito3.posX + movimiento

        gusanito4.posX = gusanito4.posX + movimiento
        gusanito4.posY = gusanito4.posY + movimiento
        gusanito5.posX = gusanito5.posX - movimiento
        gusanito5.posY = gusanito5.posY - movimiento

    def checar_colisiones(self, gusanito1, gusanito2, gusanito3, gusanito4, gusanito5):
        if gusanito1.posX + 0.01 > 1.0:
            gusanito1.posX = -1.05
        if gusanito2.posX + 0.01 < -1.0:
            gusanito2.posX = 1.05
        if gusanito3.posX + 0.01 > 1.0:
            gusanito3.posX = -1.05

        if gusanito4.posY + 0.01 > 1.0:
            gusanito4.posY = -1.05
            gusanito4.posX = -0.8
        if gusanito5.posY - 0.01 < -1.0:
            gusanito5.posY = 1.05
            gusanito5.posX = 0.7

    def dibujar(self, rotacionCabeza, rotacionCuerpo, rotacionCola, deltaposX, deltaposY):
        #cabeza
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        glScalef(0.01,0.01,0.01)
        glRotate(rotacionCabeza,0,0,1)
        glColor3f(0.8,0.2,0.3)
        glBegin(GL_POLYGON)
        for x in range(180):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
        glEnd()
        glPopMatrix()
        #cuerpo
        glPushMatrix()
        glTranslatef(self.posX + deltaposX, self.posY + deltaposY, 0.0)
        glScalef(0.01,0.01,0.01)
        glRotate(rotacionCuerpo,0,0,1)
        glColor3f(0.8,0.2,0.3)
        glBegin(GL_QUADS)
        glVertex3f(-1,1,0)
        glVertex3f(1,1,0)
        glVertex3f(1,-1,0)
        glVertex3f(-1,-1,0)
        glEnd()
        glPopMatrix()
        #cola
        glPushMatrix()
        glTranslatef(self.posX + deltaposX * 2, self.posY + deltaposY * 2, 0.0)
        glScalef(0.01,0.01,0.01)
        glRotate(rotacionCola,0,0,1)
        glColor3f(0.8,0.2,0.3)
        glBegin(GL_POLYGON)
        for x in range(180):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
        glEnd()
        glPopMatrix()