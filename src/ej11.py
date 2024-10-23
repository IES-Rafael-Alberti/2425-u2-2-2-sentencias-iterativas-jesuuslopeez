'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''
def func_entrada():
    palabra = input('Introduce una palabra: ')
    if palabra.isalpha():
        return palabra
    else:
        raise ValueError('No puedes introducir números ni carácteres especiales.')

def func_desglosamiento(palabra):
    letras = ''
    longitud = len(palabra)

    for i in range(longitud - 1, -1, -1):
        letras += palabra[i] + '\n'
    return letras

def main():
    #Entrada
    palabra = func_entrada()
    #Procesamiento
    letras = func_desglosamiento(palabra)
    #Salida
    print(letras)

if __name__ == '__main__':
    main()

