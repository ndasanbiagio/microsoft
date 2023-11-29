# La POO es un paradigma de programación que se basa en el concepto de "objetos", 
# que pueden contener datos en forma de atributos y código en forma de métodos. 
# En Python, todo es un objeto, y la POO se utiliza para organizar y estructurar 
# el código de una manera más modular y reutilizable.

# Aquí hay algunos conceptos clave:

# Clases y Objetos:
# Una clase es una plantilla para crear objetos. Define atributos (características) 
# y métodos (funciones) que los objetos creados a partir de esa clase tendrán.
# Un objeto es una instancia de una clase.


#Explicacion del siguiente bloque

# Definición de la Clase Persona:

# Se define una clase llamada Persona que tiene un constructor __init__ y un método llamado saludar.
# El constructor (__init__) se llama automáticamente cuando se crea un nuevo objeto de la clase. 
# En este caso, inicializa dos atributos de la instancia (self): nombre y edad.
# El método saludar es un método de instancia que imprime un saludo con el nombre y la edad de la persona.
# Creación de un Objeto de la Clase Persona:

# Se crea un nuevo objeto de la clase Persona llamado persona1 y se le pasan dos argumentos al constructor: 
# "Juan" como nombre y 25 como edad.
# La instancia resultante (persona1) tiene atributos nombre y edad con los valores proporcionados.
# Llamada al Método del Objeto:

# Se llama al método saludar en el objeto persona1. Este método imprime un mensaje que utiliza los valores de nombre y edad de la instancia actual.
# En resumen, este código crea una clase Persona con un constructor que inicializa los atributos nombre y edad, 
# y un método saludar que imprime un saludo utilizando esos atributos. 
# Luego, se crea un objeto de esta clase llamado persona1 y se llama al método saludar en ese objeto, 
# mostrando un mensaje personalizado. En este caso, imprimirá "Hola, soy Juan y tengo 25 años."







class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 25)

# Llamar a un método del objeto
persona1.saludar()
