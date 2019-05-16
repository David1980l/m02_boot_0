class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU GUAU")
        else:
            print("guau guau")
            
    def __str__(self):
        return " Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    
 # PerroAsistencia hereda atributos y metodos de Perro
 
class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = False
    
# Se pueden sobre escirbir metodos  en cada instancia si no los toma de el objeto de el que hereda o objeto padre

    def __str__(self):
        return "Perro de asistencia de {} ".format(self.amo)
    
    def pasear(self):
        print("{} ayudi a mi dueño {} a pasear".format(self.nombre,self.amo))
        
    def ladrar(self):
        if self.__trabajando :
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    
    def trabajando (self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            
    
