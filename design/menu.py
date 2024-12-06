from logic.formula import hi

def design():
    print("Bienvenido al mejor sistema del mundo")
    print("¿Qué deseas hacer?")
    print("     0. Atras")
    print("     1. La maquina te saluda")
    opc = int(input("Elija una de las opciones disponibles: "))
    

    if (opc ==1):
        name = input("Ingrese su nombre: ")
        result = hi(name)
        print(result)

    return opc