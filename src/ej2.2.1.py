'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''
def func_nombre(nombre):
    for i in range(10):
        print(nombre)

def main():
    #Entrada
    nombre = input('Introduce tu nombre: ')
    #Procesamiento

    #Salida
    func_nombre(nombre)

if __name__ == '__main__':
    main()