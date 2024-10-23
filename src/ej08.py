'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''
def func_entrada():
    numero = int(input('Introduce un número (entero): '))
    return numero
    
def func_triangulo_numeros(numero): 
    mensaje = []
    contador = 1

    for i in range(1, numero + 1, 2):
        mensaje2 = []
        for z in range(i, 0, -2):
            mensaje2.append(str(z))
        mensaje.append(' '.join(mensaje2))

    return '\n'.join(mensaje)
def main():
    #Entrada
    numero = func_entrada()
    #Procesamiento
    triangulo_numeros = func_triangulo_numeros(numero)
    #Salida
    print(triangulo_numeros)

if __name__ == '__main__':
    main()