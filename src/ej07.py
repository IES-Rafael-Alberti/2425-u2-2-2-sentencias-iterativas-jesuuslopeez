'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
def func_tablas(): 
    mensaje = []
    for i in range(1, 11):
        mensaje.append(f'Tabla de multiplicar del {i}\n')
        for z in range(1, 11):
            mensaje.append(f'{i} x {z} = {i * z}\n')
    return ''.join(mensaje)
def main():
    #Entrada
    
    #Procesamiento
    tablas = func_tablas()
    #Salida
    print(tablas)

if __name__ == '__main__':
    main()