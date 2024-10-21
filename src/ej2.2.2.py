'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
def func_edad(edad):
    for año in range(1, edad + 1):
        print(año)

def main():
    #Entrada
    edad = int(input('Introduce tu edad: '))
    #Procesamiento

    #Salida
    func_edad(edad)

if __name__ == '__main__':
    main()