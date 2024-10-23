'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''
def func_entrada():
    numero = int(input('Introduce un número entero: '))
    return numero

def func_triangulo_asterisco(numero): 
    mensaje = []
    for i in range(1, numero + 1):
        mensaje.append('*' * i)

    return '\n'.join(mensaje)

def main():
    #Entrada
    numero = func_entrada()
    #Procesamiento
    triangulo_asterisco = func_triangulo_asterisco(numero)
    #Salida
    print(triangulo_asterisco)

if __name__ == '__main__':
    main()