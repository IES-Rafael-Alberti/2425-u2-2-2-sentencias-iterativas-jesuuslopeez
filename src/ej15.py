'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
'''
def func_entrada():
    numero = int(input('Introduce un número (Para terminar escribe "0"): '))
    return numero

def func_bucle(numero):
    contador = 0
    while numero != 0:
        if numero < 0:
            contador = contador
        else:
            contador = contador + numero
        numero = func_entrada()
    return contador

def main():
    #Entrada
    numero = func_entrada()
    #Procesamiento
    contador = func_bucle(numero)
    #Salida
    print(contador)

if __name__ == '__main__':
    main()

