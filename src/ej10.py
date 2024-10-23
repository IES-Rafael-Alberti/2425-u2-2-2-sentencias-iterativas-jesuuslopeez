'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
def func_entrada():
    numero = int(input('Introduce un número entero: '))
    if numero <= 0:
        raise ValueError('Tienes que introducir un entero.')
    return numero

def func_num_primo(num_entero): 
    mensaje = ''
    contador1 = 1
    contador2 = 0

    for contador1 in range(1, num_entero + 1):
        if num_entero % contador1 == 0:
            contador2 += 1
            if contador2 > 2 or contador2 == 1:
                mensaje = 'El número no es primo.'
            else:
                mensaje = 'El número es primo.'
    return mensaje


def main():
    #Entrada
    num_entero = func_entrada()
    #Procesamiento
    num_primo = func_num_primo(num_entero)
    #Salida
    print(num_primo)

if __name__ == '__main__':
    main()