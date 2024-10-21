'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
def func_numero(numero):
    if numero <= 0:
        print('Introduce un número positivo')
        return
    impares = []

    for i in range(1, numero + 1):
        if i % 2 != 0:
            impares.append(str(i))
    print(', '.join(impares))

def main():
    #Entrada
    numero = int(input('Introduce un número positivo: '))
    #Procesamiento

    #Salida
    func_numero(numero)

if __name__ == '__main__':
    main()