'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
def func_entrada():
    
    contrasena_int_usuario = input('Introduce la contraseña: ')
    return contrasena_int_usuario   

def func_comprobacion_contrasena(contrasena_int_usuario): 
    contrasena_correcta = 'contraseña'
    correcta = ''

    while contrasena_correcta != contrasena_int_usuario:
        print('¡Contraseña incorrecta! Vuelve a intentarlo.')
        contrasena_int_usuario = input('Introduce la contraseña: ')

    correcta = '¡La contraseña es correcta!'

    return correcta

def main():
    #Entrada
    contrasena_int_usuario = func_entrada()
    #Procesamiento
    comprobacion_contrasena = func_comprobacion_contrasena(contrasena_int_usuario)
    #Salida
    print(comprobacion_contrasena)

if __name__ == '__main__':
    main()