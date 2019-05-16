# Al introducir (*) considera que todos los valores separados por comas, seran parte de un array o lista llamada l en nuestro caso 
def maxi(*l):
    if len(l) == 0:
        return 0
# Si encuentra una lista vacia nos devuelve cero por defecto
    m = l[0]
# La variable m se inicializa con el primer valor de la lista l
    for ix in range (1,len(l)):
        if l[ix] > m:
            m = l[ix]
# Recorremos cada uno de los indices de la lista l desde la 2º posicion o indice 1 ya que m contiene el indice 0
# si el mayor valor estuviera en este indice 0 ya lo tendriamos capturado.recorremosla lista en un rango delimitado por un numero
# que obtenemos (con len de l) este nos devolvera el numero de indices de la lista.
# al recorrer la lista si el valor de un indice [ix] de la lista l ( el que se esta leyendo es mayor que m esta toma valor 
    return m

def mini(*l):
    
    if len(l) == 0:
        
        return 0

    
    m = l[0]
    
    for ix in range (1,len(l)):
        
        if l[ix] < m:
            
            m = l[ix]
            
    return m


def media(*l):
    
    if len(l) == 0:
        
        return 0

    suma = 0
    
    for valor in l:
        
        suma += valor
    
    return suma / len(l)

# Definimos un diccionario que invoca nuestras funciones
# De esta forfa pondriamos por ejemplo en la shell :   returnf('max')(1,3,-1,15,9) y nos devolveria el resutado  15
#                                                      returnf('min')(1,3,-1,15,9)                               -1
#                                                      returnf('med')(1,3,-1,15,9)                               5.4

funciones = {
    'max': maxi,
    'min': mini,
    'med': media
    }

def returnf(nombre):
    
    nombre = nombre.lower()
    
    if nombre in funciones.keys():
        
        return funciones[nombre]
    
    return None

   
        
    

