import turnero

def preguntar():
    print("Bienvenido a la Farmacio Python")
    
    while True:
        print("[P] - Perfumeria\n [F] - Farmacia\n [C] - Cosmetica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"]. index(mi_rubro)
        
        except ValueError:
            print("Esa no es una opcion valida")
        
        else:
            break
    

    turnero.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Queres sacar otro turno? [S] [N]").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == 'N':
                print("Gracias por su visita")
                break
            
inicio()