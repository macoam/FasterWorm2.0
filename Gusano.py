from OpenGL.GL import *
from glew_wish import *
import glfw
import random
from math import *

class Gusano:
    #Posiciones
    posX = 0.0
    posY = 0.0
    deltaPosX = -0.1
    deltaPosY = 0.0

    #Condiciones
    condicionMovXP = False
    condicionMovXN = False
    condicionMovYP = False
    condicionMovYN = False

    #Movimiento
    velocidad = 0.3

    #Colisiones
    colisionPerder = False
    colisionAlimento = 0

    #score
    score = -1
    
    def actualizar(self, window, deltatime):
        movimiento = self.velocidad * deltatime

        estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
        estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

        if estado_tecla_derecha == glfw.PRESS:
            self.condicionMovXP = True
            self.condicionMovXN = False
            self.condicionMovYP = False
            self.condicionMovYN = False
        if estado_tecla_izquierda == glfw.PRESS:
            self.condicionMovXN = True
            self.condicionMovXP = False
            self.condicionMovYP = False
            self.condicionMovYN = False
        if estado_tecla_arriba== glfw.PRESS:
            self.condicionMovYP = True
            self.condicionMovXP = False
            self.condicionMovXN = False
            self.condicionMovYN = False
        if estado_tecla_abajo== glfw.PRESS:
            self.condicionMovYN = True
            self.condicionMovXP = False
            self.condicionMovXN = False
            self.condicionMovYP = False

        if self.condicionMovXP == True:
            self.posX = self.posX + movimiento
            self.deltaPosX = -0.1
            self.deltaPosY = 0.0
        if self.condicionMovXN == True:
            self.posX = self.posX - movimiento
            self.deltaPosX = 0.1
            self.deltaPosY = 0.0
        if self.condicionMovYP == True:
            self.posY = self.posY + movimiento
            self.deltaPosX = 0.0
            self.deltaPosY = -0.1
        if self.condicionMovYN == True:
            self.posY = self.posY - movimiento
            self.deltaPosX = 0.0
            self.deltaPosY = 0.1

    def checar_colisiones(self, alimento1, alimento2, alimento3, alimento4, alimento5, alimento6, alimento7, alimento8, alimento9, alimento10):
        if self.posX + 0.05 > 1.0:
            self.colisionPerder = True
        elif self.posX - 0.05 < -1.0:
            self.colisionPerder = True
        elif self.posY + 0.05 > 1.0:
            self.colisionPerder = True
        elif self.posY - 0.05 < -1.0:
            self.colisionPerder = True
        else:
            colisionPerder = False

        if self.posX + 0.05 > alimento1.posX - 0.05 and self.posX - 0.05 < alimento1.posX + 0.05 and self.posY + 0.05 > alimento1.posY - 0.05 and self.posY - 0.05 < alimento1.posY + 0.05:
            self.colisionAlimento = 1
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = random.uniform(-0.85,0.85)
            alimento2.posY = random.uniform(-0.85,0.85)
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento2.posX - 0.05 and self.posX - 0.05 < alimento2.posX + 0.05 and self.posY + 0.05 > alimento2.posY - 0.05 and self.posY - 0.05 < alimento2.posY + 0.05:
            self.colisionAlimento = 2
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = random.uniform(-0.85,0.85)
            alimento3.posY = random.uniform(-0.85,0.85)
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento3.posX - 0.05 and self.posX - 0.05 < alimento3.posX + 0.05 and self.posY + 0.05 > alimento3.posY - 0.05 and self.posY - 0.05 < alimento3.posY + 0.05:
            self.colisionAlimento = 3
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = random.uniform(-0.85,0.85)
            alimento4.posY = random.uniform(-0.85,0.85)
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento4.posX - 0.05 and self.posX - 0.05 < alimento4.posX + 0.05 and self.posY + 0.05 > alimento4.posY - 0.05 and self.posY - 0.05 < alimento4.posY + 0.05:
            self.colisionAlimento = 4
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = random.uniform(-0.85,0.85)
            alimento5.posY = random.uniform(-0.85,0.85)
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento5.posX - 0.05 and self.posX - 0.05 < alimento5.posX + 0.05 and self.posY + 0.05 > alimento5.posY - 0.05 and self.posY - 0.05 < alimento5.posY + 0.05:
            self.colisionAlimento = 5
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = random.uniform(-0.85,0.85)
            alimento6.posY = random.uniform(-0.85,0.85)
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento6.posX - 0.05 and self.posX - 0.05 < alimento6.posX + 0.05 and self.posY + 0.05 > alimento6.posY - 0.05 and self.posY - 0.05 < alimento6.posY + 0.05:
            self.colisionAlimento = 6
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = random.uniform(-0.85,0.85)
            alimento7.posY = random.uniform(-0.85,0.85)
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento7.posX - 0.05 and self.posX - 0.05 < alimento7.posX + 0.05 and self.posY + 0.05 > alimento7.posY - 0.05 and self.posY - 0.05 < alimento7.posY + 0.05:
            self.colisionAlimento = 7
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = random.uniform(-0.85,0.85)
            alimento8.posY = random.uniform(-0.85,0.85)
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento8.posX - 0.05 and self.posX - 0.05 < alimento8.posX + 0.05 and self.posY + 0.05 > alimento8.posY - 0.05 and self.posY - 0.05 < alimento8.posY + 0.05:
            self.colisionAlimento = 8
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = random.uniform(-0.85,0.85)
            alimento9.posY = random.uniform(-0.85,0.85)
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento9.posX - 0.05 and self.posX - 0.05 < alimento9.posX + 0.05 and self.posY + 0.05 > alimento9.posY - 0.05 and self.posY - 0.05 < alimento9.posY + 0.05:
            self.colisionAlimento = 9
            alimento1.posX = -1.5
            alimento1.posY = -1.5
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = random.uniform(-0.85,0.85)
            alimento10.posY = random.uniform(-0.85,0.85)
            self.velocidad += 0.05
            self.score += 1

        elif self.posX + 0.05 > alimento10.posX - 0.05 and self.posX - 0.05 < alimento10.posX + 0.05 and self.posY + 0.05 > alimento10.posY - 0.05 and self.posY - 0.05 < alimento10.posY + 0.05:
            self.colisionAlimento = 0
            alimento1.posX = random.uniform(-0.85,0.85)
            alimento1.posY = random.uniform(-0.85,0.85)
            alimento2.posX = -1.5
            alimento2.posY = -1.5
            alimento3.posX = -1.5
            alimento3.posY = -1.5
            alimento4.posX = -1.5
            alimento4.posY = -1.5
            alimento5.posX = -1.5
            alimento5.posY = -1.5
            alimento6.posX = -1.5
            alimento6.posY = -1.5
            alimento7.posX = -1.5
            alimento7.posY = -1.5
            alimento8.posX = -1.5
            alimento8.posY = -1.5
            alimento9.posX = -1.5
            alimento9.posY = -1.5
            alimento10.posX = -1.5
            alimento10.posY = -1.5
            self.velocidad += 0.05
            self.score += 1

    def dibujar(self):
        #cabeza
        glPushMatrix()
        glTranslatef(self.posX, self.posY, 0.0)
        glScalef(0.05,0.05,0.05)
        if self.condicionMovXP == True:
            glRotatef(-90,0,0,1)
        elif self.condicionMovXN == True:
            glRotatef(90,0,0,1)
        elif self.condicionMovYP == True:
            glRotatef(0,0,0,1)
        elif self.condicionMovYN == True:
            glRotatef(180,0,0,1)
        else:
            glRotatef(-90,0,0,1)
        glColor3f(0.9,0.8,0.1)
        glBegin(GL_POLYGON)
        for x in range(180):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
        glEnd()
        glColor3f(1,1,1)
        glBegin(GL_POLYGON)
        #ojos
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.45+0.5,sin(angulo)*0.45-0.6,0.0)
        glEnd()
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3+0.5,sin(angulo)*0.3-0.45,0.0)
        glEnd()
        glColor3f(1,1,1)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.45-0.5,sin(angulo)*0.45-0.6,0.0)
        glEnd()
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo)*0.3-0.5,sin(angulo)*0.3-0.45,0.0)
        glEnd()
        glPopMatrix()
        #cuerpo
        glPushMatrix()
        glTranslatef(self.posX + self.deltaPosX, self.posY + self.deltaPosY, 0.0)
        glScalef(0.05,0.05,0.05)
        glColor3f(0.9,0.8,0.1)
        glBegin(GL_QUADS)
        glVertex3f(-1,1,0)
        glVertex3f(1,1,0)
        glVertex3f(1,-1,0)
        glVertex3f(-1,-1,0)
        glEnd()
        glPopMatrix()
        #cola
        glPushMatrix()
        glTranslatef(self.posX + self.deltaPosX * 2, self.posY + self.deltaPosY * 2, 0.0)
        glScalef(0.05,0.05,0.05)
        if self.condicionMovXP == True:
            glRotatef(90,0,0,1)
        elif self.condicionMovXN == True:
            glRotatef(-90,0,0,1)
        elif self.condicionMovYP == True:
            glRotatef(180,0,0,1)
        elif self.condicionMovYN == True:
            glRotatef(0,0,0,1)
        else:
            glRotatef(90,0,0,1)
        glColor3f(0.9,0.8,0.1)
        glBegin(GL_POLYGON)
        for x in range(180):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
        glEnd()
        glPopMatrix()