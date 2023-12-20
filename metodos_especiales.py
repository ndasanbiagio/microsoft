# mi_lista = [1,1,1,1,1,1,1,1,1]
# print(len(mi_lista))

# mi_objeto = Objeto()
# print(mi_objeto)


#Nuevo

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"
    
    
    def __len__(self):
        return self.canciones
    
    
    
mi_cd = CD('Pink Floyd', 'The Wall', 24)


# del mi_cd  # ------------> BORRA TODO SIN AVISAR

print(len(mi_cd))



