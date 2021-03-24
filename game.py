from OpenGL.GL import *
from glew_wish import *
import glfw
import random
from math import *
import sys

from Gusano import *
from Alimento import *
from Gusanito import *
from Fondo import *

gusano = Gusano()

naranja = Naranja()
limon = Limon()
cereza = Cereza()
pepino = Pepino()
manzana = Manzana()
pera = Pera()
zanahoria = Zanahoria()
flor = Flor()
rabano = Rabano()
uvas = Uvas()

gusanito1 = Gusanito(-0.7, 0.6)
gusanito2 = Gusanito(0.1, -0.1)
gusanito3 = Gusanito(0.6, -0.7)
gusanito4 = Gusanito(-0.7, -0.6)
gusanito5 = Gusanito(0.7, 0.6)

fondo = Fondo()

tiempo = 0.0
tiempoAnterior = 0.0

    
def actualizar(window):
    global tiempo
    global tiempoAnterior
    
    global gusano

    global naranja
    global limon
    global cereza
    global pepino
    global manzana
    global pera
    global zanahoria
    global flor
    global rabano
    global uvas

    global gusanito1
    global gusanito2
    global gusanito3
    global gusanito4
    global gusanito5
    

    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior
    
    gusano.actualizar(window, deltatime)
    gusanito1.actualizar(deltatime, gusanito1, gusanito2, gusanito3, gusanito4, gusanito5)
    gusano.checar_colisiones(naranja, limon, cereza, pepino, manzana, pera, zanahoria, flor, rabano, uvas)
    gusanito1.checar_colisiones(gusanito1, gusanito2, gusanito3, gusanito4, gusanito5)
    tiempoAnterior = tiempo

def dibujar():
    fondo.dibujarSuelo()
    fondo.dibujarEspinas()

    gusanito1.dibujar(-90, -90, 90, -0.02, 0.0)
    gusanito2.dibujar(-90, -90, 90, -0.02, 0.0)
    gusanito3.dibujar(-90, -90, 90, -0.02, 0.0)
    gusanito4.dibujar(-45, -45, 135, -0.0125, -0.0125)
    gusanito5.dibujar(-45, -45, 135, -0.0125, -0.0125)

    naranja.dibujar(gusano)
    limon.dibujar(gusano)
    cereza.dibujar(gusano)
    pepino.dibujar(gusano)
    manzana.dibujar(gusano)
    pera.dibujar(gusano)
    zanahoria.dibujar(gusano)
    flor.dibujar(gusano)
    rabano.dibujar(gusano)
    uvas.dibujar(gusano)

    gusano.dibujar()

def main():
    global gusano
    
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Gusano", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    #Establecer callback de evento de teclado
    #glfw.set_key_callback(window, key_callback)
    #tiempo = glfw.get_time()
    #tiempoAnterior = glfw.get_time()
    
    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.3,0.2,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #Actualizar valores de la app
        actualizar(window)
        #Dibujar
        dibujar()

        if gusano.colisionPerder == True:
            print("Tu score fue de: ", gusano.score)
            sys.exit()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()