'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
def func_entrada():
    numero = int(input('Introduce un número positivo: '))
    if numero <= 0:
        raise ValueError('Tienes que introducir un número positivo.')
    return numero
def func_procesamiento(numero):
    impares = ''

    for i in range(1, numero + 2, 2):
        impares = impares + str(i) + ', '
    return impares

def main():
    #Entrada
    numero = func_entrada()
    #Procesamiento
    calculo = func_procesamiento(numero)
    #Salida
    print(calculo)

if __name__ == '__main__':
    main()