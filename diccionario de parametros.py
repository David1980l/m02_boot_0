'''
En el primer caso *listadecosas ( precedido de un asterisco *) nos almacena los valores que introduccamos separados por comas como elementos de
una lista.
imprimecosas('cosa1,'cosa2','cosa3') nos crearia un array con 3 valores 

'''

def imprimeCosas(*listadecosas):
    for item in listadecosas:
        print(item)
        
'''
En este segundo caso **diccionariodeparametros Precedido de ** ) nos almacena los valores en un diccionario si los introducimos como
clave : valor .
imprimeconDiccionario(contenido='lacosa',line=3,colum=5) nos crearia un diccionario con 3 claves contenido, line, colum y cada clave
con su correspondiente valor ['contenido':'lacosa','line':3,'colum':5]

'''


def imprimeconDiccionario(**diccionariodeparametros):
    if line in diccionariodeparametros:
        print('posicionar en linea')
    else:
        print('no hay line')
        
        