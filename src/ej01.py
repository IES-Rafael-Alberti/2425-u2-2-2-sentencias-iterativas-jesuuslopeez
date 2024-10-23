'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''
def func_entrada():
    nombre = input('Introduce tu nombre: ')
    if nombre.isalpha():
        return nombre
    else:
        raise ValueError('No puedes introducir números ni carácteres especiales.')

def func_procesamiento(nombre):
    mensaje = ''

    for i in range(10):
        mensaje = mensaje + nombre + '\n'
    return mensaje

def main():
    #Entrada
    nombre = func_entrada()
    #Procesamiento
    salida_final = func_procesamiento(nombre)
    #Salida
    print(salida_final)

if __name__ == '__main__':
    main()