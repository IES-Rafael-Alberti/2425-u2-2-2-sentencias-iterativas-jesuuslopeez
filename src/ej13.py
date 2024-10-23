'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''
def func_entrada():
    palabra = input('Introduce cualquier cosa (Para terminar escribe "salir"): ')
    return palabra

def func_bucle(palabra):
    while palabra !=  'salir':
        print(palabra)
        palabra = func_entrada()
    print('Terminando...')

def main():
    #Entrada
    palabra = func_entrada()
    #Procesamiento

    #Salida
    func_bucle(palabra)

if __name__ == '__main__':
    main()

