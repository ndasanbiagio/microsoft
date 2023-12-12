#Ejercicio con Match y Case

cliente = {'nombre': 'Nicolas',
           'edad': 39,
           'ocupacion': 'instructor'}

pelicula = {'titulo': 'Matrix',
            'ficha tecnica': {'protagonista': 'Keanu Reeves',
                              'director': 'Lana y Lilly Wachwski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")