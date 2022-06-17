'''
Implementación del algoritmo de busqueda BFS para generar la simulación de un GPS
La orientación se basa en la planificación de un viaje para encontrar lugares cercanos 
de interés por medio de un método de busqueda. 
'''
#Importamos la clase queue para la generación de Colas
from queue import Queue

'''
Generar la clase grafo que permite instanciar el objeto y definir
los nodos a considerar para obtener la búsqueda deseada
'''
class Grafo():
    
    def __init__(self, numero_de_nodos,dirigido=True):
        '''
        Generar el constructor, este método permite instanciar el objeto creado
            Parámetros:
                numero_de_nodos : int
                    Determina el rango que tendra el grafo
                
                dirigido : boolean
                    Determina si el grafo es dirigido o no
            Retorna:
                Nada
        Generar un control de excepciones
         try:
            except:
                print("Error")
        '''
        try:
            #Asignamos valores al número de nodos mediante el parámetro que se recibio
            self.m_numero_nodos = numero_de_nodos
            #Se genera el rango de nodos en base a m_numero_nodos
            self.m_nodos = range(self.m_numero_nodos)
            #Determinar si el grafo es dirigido o no dirigido
            self.m_dirigido = dirigido
            #Se genera un diccionario con los nodos que se van a visitar
        
            #Se genera una lista de los nodos que se van a visitar
            self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
        except Exception as e:
            print(e)
    def agregar_borde(self,nodo1,nodo2,peso=1):
        '''
        Generar el método para añadir nodos al grafo
        Parámetros:
            nodo1 : int
                Nodo que se va a añadir
            nodo2 : int
                Nodo que se va a añadir
            peso : int
                Peso que se le asigna al nodo
        Retorna:
            Nada
        
        Generar un control de excepciones
        try:
            except:
                print("Error")
        '''
        try:
            #Se añade el nodo 1 al nodo 2
            self.m_lista_adyacencia[nodo1].add((nodo2,peso))
            #Se añade el nodo 2 al nodo 1
            if not self.m_dirigido:
                self.m_lista_adyacencia[nodo2].add((nodo1,peso))
        except Exception as e:
            print(e)
    