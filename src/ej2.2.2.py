'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
def func_entrada():
    edad = int(input('Introduce tu edad: '))
    return edad

def func_procesamiento(edad):
    final = ''

    for year in range(1, edad + 1):
        final = final + str(year) + '\n'
    return final

def main():
    #Entrada
    edad = func_entrada()

    #Procesamiento
    calculo = func_procesamiento(edad)
    
    #Salida
    print(calculo)

if __name__ == '__main__':
    main()