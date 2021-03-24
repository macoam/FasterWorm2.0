from OpenGL.GL import *
from glew_wish import *
import glfw
import random
from math import *

class Naranja:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 0:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 0:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.9,0.6,0.1)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo),0.0)
        glEnd()
        glColor3f(0.7,0.7,0.5)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.15+0.55,sin(angulo)*0.15+0.55,0.0)
        glEnd()
        glPopMatrix()

class Limon:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 1:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 1:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.8,0.9,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.85,sin(angulo)*0.75,0.0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex3f(-1.0,0.0,0.0)
        glVertex3f(-0.7,0.2,0.0)
        glVertex3f(-0.7,-0.2,0.0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex3f(1.0,0.0,0.0)
        glVertex3f(0.7,0.2,0.0)
        glVertex3f(0.7,-0.2,0.0)
        glEnd()
        glPopMatrix()

class Cereza:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 2:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 2:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.5,0.1,0.2)
        glBegin(GL_QUADS)
        glVertex3f(-0.55,-0.5,0.0)
        glVertex3f(-0.45,-0.5,0.0)
        glVertex3f(0.45,0.8,0.0)
        glVertex3f(0.55,0.8,0.0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.45,0.8,0.0)
        glVertex3f(0.55,0.8,0.0)
        glVertex3f(0.45,-0.8,0.0)
        glVertex3f(0.55,-0.8,0.0)
        glEnd()
        glColor3f(0.7,0.1,0.2)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.35-0.5,sin(angulo)*0.35-0.5,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.35+0.5,sin(angulo)*0.35-0.5,0.0)
        glEnd()
        glPopMatrix()

class Pepino:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        glRotate(45,0,0,1)
        if gusano.colisionAlimento == 3:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 3:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.1,0.4,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.35,sin(angulo)*1.3,0.0)
        glEnd()
        glPopMatrix()

class Manzana:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 4:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 4:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.3,0.1,0.0)
        glBegin(GL_QUADS)
        glVertex3f(0.0,1.1,0.0)
        glVertex3f(0.1,1.1,0.0)
        glVertex3f(-0.35,-0.5,0.0)
        glVertex3f(-0.25,-0.5,0.0)
        glEnd()
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.7-0.2,sin(angulo)*0.9-0.1,0.0)
        glEnd()
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.7+0.2,sin(angulo)*0.9-0.1,0.0)
        glEnd()
        glPopMatrix()

class Pera:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 5:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 5:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.3,0.1,0.0)
        glBegin(GL_QUADS)
        glVertex3f(0.0,1.1,0.0)
        glVertex3f(0.1,1.1,0.0)
        glVertex3f(-0.35,-0.5,0.0)
        glVertex3f(-0.25,-0.5,0.0)
        glEnd()
        glColor3f(0.6,0.9,0.1)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.5,sin(angulo)*0.6+0.1,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.6,sin(angulo)*0.6-0.3,0.0)
        glEnd()
        glPopMatrix()

class Zanahoria:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 6:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 6:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.9,0.6,0.0)
        glBegin(GL_POLYGON)
        for x in range(181):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.7,sin(angulo)*0.7-1.0,0.0)
        glEnd()
        glColor3f(0.5,0.8,0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.3,1.0,0.0)
        glVertex3f(-0.4,0.4,0.0)
        glVertex3f(0.0,-0.3,0.0)
        glVertex3f(0.0,0.4,0.0)
        glEnd()
        glColor3f(0.3,0.5,0.0)
        glBegin(GL_QUADS)
        glVertex3f(0.2,1.0,0.0)
        glVertex3f(-0.1,0.4,0.0)
        glVertex3f(0.0,-0.3,0.0)
        glVertex3f(0.3,0.4,0.0)
        glEnd()
        glPopMatrix()

class Flor:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 7:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 7:
            glScalef(0.0,0.0,0.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.2,0.4,0.0)
        glVertex3f(0.15,0.4,0)
        glVertex3f(-0.15,0.4,0)
        glVertex3f(0.0,-1.0,0)
        glEnd()
        glColor3f(0.9,0.2,0.1)
        glBegin(GL_POLYGON)
        glVertex3f(0.0,-0.3,0)
        glVertex3f(0.3,0.1,0)
        glVertex3f(0.15,0.4,0)
        glVertex3f(-0.15,0.4,0)
        glVertex3f(-0.3,0.1,0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex3f(0.3,0.1,0)
        glVertex3f(0.15,0.4,0)
        glVertex3f(0.8,0.6,0)
        glVertex3f(0.15,0.4,0)
        glVertex3f(-0.15,0.4,0)
        glVertex3f(0.0,1.0,0)
        glVertex3f(-0.3,0.1,0)
        glVertex3f(-0.15,0.4,0)
        glVertex3f(-0.8,0.6,0)
        glEnd()
        glPopMatrix()

class Rabano:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 8:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 8:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.8,0.0,0.3)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.6,sin(angulo)*0.6-0.2,0.0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex3f(-0.6,-0.2,0.0)
        glVertex3f(0.0,-1.0,0.0)
        glVertex3f(0.6,-0.2,0.0)
        glEnd()
        glColor3f(0.5,0.8,0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.3,1.0,0.0)
        glVertex3f(-0.4,0.7,0.0)
        glVertex3f(0.0,0.4,0.0)
        glVertex3f(0.0,0.7,0.0)
        glEnd()
        glColor3f(0.3,0.5,0.0)
        glBegin(GL_QUADS)
        glVertex3f(0.2,1.0,0.0)
        glVertex3f(-0.1,0.7,0.0)
        glVertex3f(0.0,0.4,0.0)
        glVertex3f(0.3,0.7,0.0)
        glEnd()
        glPopMatrix()

class Uvas:
    posX = 0.0
    posY = 0.0

    def dibujar(self, gusano):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        if gusano.colisionAlimento == 9:
            glScalef(0.05,0.05,0.05)
        if gusano.colisionAlimento != 9:
            glScalef(0.0,0.0,0.0)
        glColor3f(0.3,0.1,0.0)
        glBegin(GL_QUADS)
        glVertex3f(0.0,1.0,0)
        glVertex3f(0.2,1.0,0)
        glVertex3f(0.1,0.2,0)
        glVertex3f(0.0,0.2,0)
        glEnd()
        glColor3f(0.6,0.2,0.6)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25,sin(angulo)*0.25-0.65,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25+0.25,sin(angulo)*0.25-0.2,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25-0.25,sin(angulo)*0.25-0.2,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25+0.5,sin(angulo)*0.25+0.25,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25,sin(angulo)*0.25+0.25,0.0)
        glEnd()
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.25-0.5,sin(angulo)*0.25+0.25,0.0)
        glEnd()
        glPopMatrix()