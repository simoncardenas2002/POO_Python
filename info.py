#Declarar una clase

# class nombre_de_la_clase(super_clase):
#     def __init__(self, parametros): #siempre los metodos deben llevar el parámetro self# 
#         expresion
#     
#     def nombre_del_metodo(self, otros_parametos):
#         expresion

#EJEMPLO

class Persona:
    def __init__(self, name,age): #aqui declaro los atributos de esa clase, lo que debe tener cualquier objeto que pertenezca a esta clase
        self.name=name
        self.age=age
    def saluda(self,otra_persona): #Aqui definí una de las posibles "acciones" que puede realizar este objeto persona
        return  "Hola {otra_persona.name}, me llamo {self.name}"

david= Persona("David",34)
erika= Persona("Erika",30)

david.saluda(erika)
