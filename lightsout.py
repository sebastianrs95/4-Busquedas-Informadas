#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lightsout.py
------------

Tarea sobre búsquedas, donde lo que es importante es crear nuevas heurísticas

"""
__author__ = 'nombre del estudiante'


import busquedas


class LightsOut(busquedas.ModeloBusqueda):
    # --------------------------------------------------------
    # Completa la clase
    # para el modelo de lights out
    # --------------------------------------------------------
    """
    Problema del jueguito "Ligths out".

    La idea del juego es el apagar o prender todas las luces.
    Al seleccionar una casilla, la casilla y sus casillas
    adjacentes cambian (si estan prendidas se apagan y viceversa).

    El juego consiste en una matriz de 5 X 5, cuyo estado puede
    ser apagado 0 o prendido 1. Por ejemplo el estado

       (0,0,1,0,0,
        1,1,0,0,1,
        0,0,1,1,0,
        1,0,1,0,1,
        0,0,0,0,0)

    corresponde a:

    ---------------------
    |   |   | X |   |   |
    ---------------------
    | X | X |   |   | X |
    ---------------------
    |   |   | X | X |   |
    ---------------------
    | X |   | X |   | X |
    ---------------------
    |   |   |   |   |   |
    ---------------------

    Las acciones posibles son de elegir cambiar una luz y sus casillas
    adjacentes, por lo que la accion es un número entre 0 y 24.

    Para mas información sobre el juego, se puede consultar

    http://en.wikipedia.org/wiki/Lights_Out_(game)

    """
        
        
    def acciones_legales(self, estado):
        # cualquier accion es legal, puesto que una casilla siempre se puede seleccionar
        # y modificarse y a sus adyacentes
        return range(25)

    def sucesor(self, estado, accion):
        # la accion siempre es la misma, tocar casilla, entonces es un numero entre 0 y 24 (indices de las casillas)
        estado = list(estado)
        estado[accion] *= -1 
        
        # caso de las esquinas 
        if accion == 0: #esquina superior izquierda
            estado[accion+1] *= -1
            estado[accion+5] *= -1
            return tuple(estado)
            
        if accion == 4:     # esquina superior derecha
            estado[accion-1] *= -1
            estado[accion+5] *= -1
            return tuple(estado)
        
        if accion == 20:    # esquina inferior izquierda
            estado[accion+1] *= -1
            estado[accion-5] *= -1
            return tuple(estado)
        
        if accion == 24:    # esquina inferior derecha
            estado[accion-1] *= -1
            estado[accion-5] *= -1
            return tuple(estado)
            
        # caso de la columna izquierda
        if accion % 5 == 0:
            estado[accion+1] *= -1
            estado[accion-5] *= -1
            estado[accion+5] *= -1
            return tuple(estado)
        
        # caso de la columna derecha
        if (accion+1) % 5 == 0:
            
            estado[accion-1] *= -1
            estado[accion-5] *= -1
            estado[accion+5] *= -1
            return tuple(estado)
            
        
        if accion - 1 >= 0:
            estado[accion-1] *= -1
        
        if accion + 1 <= 24:
            estado[accion+1] *= -1

        if accion + 5 <= 24:
            estado[accion+5] *= -1
        
        if accion - 5 >= 0:
            estado[accion-5] *= -1
        
        return tuple(estado)
        

    @staticmethod
    def bonito(estado):
        """
        El prettyprint de un estado dado

        """
        cadena = "---------------------\n"
        for i in range(5):
            for j in range(5):
                if estado[5 * i + j] > 0:
                    cadena += "| X "
                else:
                    cadena += "|   "
            cadena += "|\n---------------------\n"
        return cadena


# ------------------------------------------------------------
#  Completa el problema de LightsOut
# ------------------------------------------------------------
class ProblemaLightsOut(busquedas.ProblemaBusqueda):
    def __init__(self, pos_ini):
        """
        Utiliza la superclase para hacer el problema

        """
        # Completa el código
        x0 = tuple(pos_ini)
        def meta(x):
            return 1 not in x

        super().__init__(x0=x0, meta=meta, modelo=LightsOut())


# ------------------------------------------------------------
#  Desarrolla una política admisible.
# ------------------------------------------------------------
def h_1(nodo):
    """
    DOCUMENTA LA HEURÍSTICA QUE DESARROLLES Y DA UNA JUSTIFICACIÓN
    PLATICADA DE PORQUÉ CREES QUE LA HEURÍSTICA ES ADMISIBLE

    """
    return 0


# ------------------------------------------------------------
#  Desarrolla otra política admisible.
#  Analiza y di porque piensas que es (o no es) dominante una
#  respecto otra política
# ------------------------------------------------------------
def h_2(nodo):
    """
    DOCUMENTA LA HEURÍSTICA DE DESARROLLES Y DA UNA JUSTIFICACIÓN
    PLATICADA DE PORQUÉ CREES QUE LA HEURÍSTICA ES ADMISIBLE

    """
    return 0


def prueba_modelo():
    """
    Prueba la clase LightsOut

    """

    pos_ini = (-1, 1, -1, 1, -1,
               -1, -1, 1, 1, -1,
               -1, -1, -1, 1, 1,
               -1, -1, 1, 1, 1,
               -1, -1, -1, 1, 1)

    pos_a0 = (1, -1, -1, 1, -1,
              1, -1, 1, 1, -1,
              -1, -1, -1, 1, 1,
              -1, -1, 1, 1, 1,
              -1, -1, -1, 1, 1)

    pos_a4 = (1, -1, -1, -1, 1,
              1, -1, 1, 1, 1,
              -1, -1, -1, 1, 1,
              -1, -1, 1, 1, 1,
              -1, -1, -1, 1, 1)

    pos_a24 = (1, -1, -1, -1, 1,
               1, -1, 1, 1, 1,
               -1, -1, -1, 1, 1,
               -1, -1, 1, 1, -1,
               -1, -1, -1, -1, -1)

    pos_a15 = (1, -1, -1, -1, 1,
               1, -1, 1, 1, 1,
               1, -1, -1, 1, 1,
               1, 1, 1, 1, -1,
               1, -1, -1, -1, -1)

    pos_a12 = (1, -1, -1, -1, 1,
               1, -1, -1, 1, 1,
               1, 1, 1, -1, 1,
               1, 1, -1, 1, -1,
               1, -1, -1, -1, -1)

    modelo = LightsOut()

    assert modelo.acciones_legales(pos_ini) == range(25)
    assert modelo.sucesor(pos_ini, 0) == pos_a0
    assert modelo.sucesor(pos_a0, 4) == pos_a4
    assert modelo.sucesor(pos_a4, 24) == pos_a24
    assert modelo.sucesor(pos_a24, 15) == pos_a15
    assert modelo.sucesor(pos_a15, 12) == pos_a12
    print("Paso la prueba de la clase LightsOut")


def compara_metodos(pos_inicial, heuristica_1, heuristica_2):
    """
    Compara en un cuadro lo nodos expandidos y el costo de la solución
    de varios métodos de búsqueda

    @param pos_inicial: Una tupla con una posicion inicial
    @param heuristica_1: Una función de heurística
    @param heuristica_2: Una función de heurística

    @return None (no regresa nada, son puros efectos colaterales)

    Si la búsqueda no informada es muy lenta, posiblemente tendras que quitarla
    de la función

    """
    solucion1 = busquedas.busqueda_A_estrella(ProblemaLightsOut(pos_inicial),
                                              heuristica_1)
    solucion2 = busquedas.busqueda_A_estrella(ProblemaLightsOut(pos_inicial),
                                              heuristica_2)

    print('-' * 50)
    print('Método'.center(10) + 'Costo'.center(20) + 'Nodos visitados')
    print('-' * 50 + '\n\n')
    print('A* con h1'.center(10) + str(solucion1.costo).center(20) +
          str(solucion1.nodos_visitados))
    print('A* con h2'.center(10) + str(solucion2.costo).center(20) +
          str(solucion2.nodos_visitados))
    print('-' * 50 + '\n\n')


if __name__ == "__main__":

    print("Antes de hacer otra cosa,")
    print("vamos a verificar medianamente la clase LightsOut")
    prueba_modelo()

    # Tres estados iniciales interesantes
    diagonal = (0, 0, 0, 0, 1,
                0, 0, 0, 1, 0,
                0, 0, 1, 0, 0,
                0, 1, 0, 0, 0,
                1, 0, 0, 0, 0)

    simetria = (1, 0, 1, 0, 1,
                1, 0, 1, 0, 1,
                0, 0, 0, 0, 0,
                1, 0, 1, 0, 1,
                1, 0, 1, 0, 1)

    problemin = (0, 1, 0, 1, 0,
                 0, 0, 1, 1, 0,
                 0, 0, 0, 1, 1,
                 0, 0, 1, 1, 1,
                 0, 0, 0, 1, 1)

    print("\n\nPara el problema en diagonal")
    print("\n{}".format(LightsOut.bonito(diagonal)))
    compara_metodos(diagonal, h_1, h_2)

    print("\n\nPara el problema simétrico")
    print("\n".format(LightsOut.bonito(simetria)))
    compara_metodos(simetria, h_1, h_2)

    print("\n\nPara el problema Bonito")
    print("\n".format(LightsOut.bonito(problemin)))
    compara_metodos(problemin, h_1, h_2)
