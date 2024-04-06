# %%Acción
class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    

# %%Estado
class Estado:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

    def __str__(self):
        return self.nombre
    

# %%Problema
class Problema:
    def __init__(self,estado_inicial, estado_objetivo, acciones, costo=None, heuristicas=None):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.acciones = acciones
        self.costo = costo
        self.heuristicas = heuristicas
        self.infinito = 99999999

        if not costo:
            self.costo = {}
            for estado in self.acciones.keys():
                self.costo[estado] = {}
                for accion in self.acciones[estado].keys():
                    self.costo[estado][accion] = 1

        if not heuristicas:
            self.heuristicas = {}
            for estado in self.acciones.keys():
                self.heuristicas[estado] = {}
                for objetivo in self.estado_objetivo:
                    self.heuristicas[estado][objetivo] = self.infinito

    def __str__(self):
        msg = "Estado Inicial: {0} -> Objetivos: {1}"
        return msg.format(self.estado_inicial.nombre, self.estado_objetivo.nombre)
    
    def es_objetivo(self, estado):
        return estado in self.estado_objetivo
    
    def resultado(self, estado, accion):
        if estado.nombre not in self.acciones.keys():
            return None
        acciones_estado = self.acciones[estado.nombre]
        if accion.nombre not in acciones_estado.keys():
            return None
        return acciones_estado[accion.nombre]
    
    def costo_accion(self, estado, accion):
        if estado.nombre not in self.costo.keys():
            return self.infinito
        costo_estado = self.costo[estado.nombre]
        if accion.nombre not in costo_estado.keys():
            return self.infinito
        return costo_estado[accion.nombre]
    
    def costo_camino(self, nodo):
        total = 0
        while nodo.padre:
            total += self.costo_accion(nodo.padre.estado, nodo.accion)
            nodo = nodo.padre
        return total
    

# %%Nodo
class Nodo:
    def __init__(self, estado, accion = None, acciones = None, padre = None):
        self.estado = estado
        self.accion = accion
        self.acciones = acciones
        self.padre = padre
        self.hijos = []
        self.costo = 0
        self.heuristicas = {}
        self.valores = {}


    def __str__(self):
        return self.estado.nombre
    
    def expandir(self, problema):
        self.hijos = []
        if not self.acciones:
            if self.estado.nombre not in problema.acciones.keys():
                return self.hijos
            self.acciones = problema.acciones[self.estado.nombre]
        for accion in self.acciones.keys():
            accion_hijo = Accion(accion)
            nuevo_estado = problema.resultado(self.estado, accion_hijo)
            acciones_nuevo = {}
            if nuevo_estado.nombre in problema.acciones.keys():
                acciones_nuevo = problema.acciones[nuevo_estado.nombre]
            hijo = Nodo(nuevo_estado, accion_hijo, acciones_nuevo, self)
            costo = self.padre.costo if self.padre else 0
            costo += problema.costo_accion(self.estado, accion_hijo)
            hijo.heuristicas = problema.heuristicas[hijo.estado.nombre]
            hijo.valores = {estado: heuristica + hijo.costo for estado, heuristica in hijo.heuristicas.items()}
            self.hijos.append(hijo)
        return self.hijos
    
    