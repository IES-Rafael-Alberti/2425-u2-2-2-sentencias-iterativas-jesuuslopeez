'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
def func_entrada():
    numero = int(input('Introduce un número positivo: '))
    return numero    

def func_cuenta_atras(numero): 
    numeros = []

    for i in range(numero, -1, -1):
        numeros.append(str(i))
    return ', '.join(numeros)
    
def main():
    #Entrada
    numero = func_entrada()
    #Procesamiento
    cuenta_atras = func_cuenta_atras(numero)
    #Salida
    print(cuenta_atras)

if __name__ == '__main__':
    main()