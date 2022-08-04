import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# esta función lee la base de datos "monstrios.py"
def nodes_():
  df = pd.read_csv("creaturas.csv") # lee la base de datos
  lote = pd.unique(df['personaje']) # convierte la columna de monstruos en una array
  dfel = pd.unique(df['amigos']) # convierte la columna de monstruos en una array
  k = dfel.tolist() # convierte el array de amigos en una lista
  s = str(k) # convierte la lista de amigos en  cadenas para quitar las dobles comillas
  nm =s.replace('"', "") 
  output=eval(nm) # como se quitaron las comillas ya se pueden leer los amigos como tuplas


  Red = nx.Graph() # crear el grafo
  nodos = lote # se crean los nodos (lista de personajes)
  enlaces = output # se crean los enlaces (lista de tuplas de amigos)
  Red.add_nodes_from(nodos) # se agregan los nodos
  Red.add_edges_from(enlaces) # se agregan las relaciones
  print ('\n')
  nd_enlazados = nodos_enlazados(nodos,enlaces) # se llama la función que retorna los nodos enlazados a esa criatura
  print('los nodos enlazados a esa creatura son: ',nd_enlazados)
  print ('\n')
  centralidad = central(Red) # se llama la función que retorna el nodo mas importante y su valor de centralidad
  print ('El nodo mas importante y su centralidad es: ',centralidad) 
  print('\n')
  rutat = ruta_nodos(Red) # se llama a la función para buscar si hay una ruta entre dos creaturas y retornar la ruta
  if len (rutat) == 0:
    print ('No hay una ruta en común para las creaturas, es decir no tienen relación')
  print('La ruta de relaciones entre las creaturas es: ',rutat)

  
  nx.draw(Red,node_size = 30 ,edge_color = 'r',node_color = 'g',font_size=7,with_labels=True,node_shape = 'o') # se crea el grafico
  plt.show()
  


def central(Red):
  
  dic=nx.eigenvector_centrality_numpy(Red)

  V_con_valor_maximo=[]
  Final = []

  M=max([dic[vertice] for vertice in 
  dic.keys()])

  tolerancia=0.001

  for vertice in dic.keys():
      if abs(dic[vertice]-M)<=tolerancia:
          V_con_valor_maximo.append(vertice)
          Final.append(vertice)
          Final.append(dic[vertice])

  return Final

  

def nodos_enlazados(nodos,enlaces):
  
  
  nombre_b = str(input('Ingrese el nombre de la creatura para conocer con que nodos esta relacionada: '))
  nodos_e = []
  ubicacion = 0
  for item in enlaces:
    for i in item:
      if i == nombre_b:
        nodos_e.append(nodos[ubicacion])
    ubicacion += 1
  if len(nodos_e) == 0:
    print('El monstruo ingresado no pertenece a un nodo ó no tiene relación con ningun otro monstruo')
    return
  return nodos_e
  
def ruta_nodos(Red):
  print('Para conocer si dos creaturas tienen relación o tambien llamado un camino que los una en la red necesitamos ingresas el nombre de ambas')
  print('\n')
  nodo_ini = str(input('Ingrese el nombre de la primera creatura: '))
  print('\n')
  nodo_fin = str(input('Ingrese el nombre de la segunda creatura  '))
  print('\n')
  
  
  creaturas = nx.dijkstra_path(Red,source = nodo_ini,target = nodo_fin) # esta función recibe dos nodos y busca si hay un camino entre ellos y lo retorna en orde, de no haber un amigo entre amos saldra error
  return creaturas
  

  
        
  





  
   





  
  