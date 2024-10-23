'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''
def func_entrada():
    cantidad = float(input('Introduce la cantidad a invertir: '))
    interes_anual = float(input('Introduce el interés anual: '))
    num_years = int(input('Introduce el número de años: '))
    return cantidad, interes_anual, num_years  
    if num_years <= 0:
        print('El número de años tiene que ser mayor a 0.')

def func_capital(cantidad, interes_anual, num_years): 
    capital = cantidad
    mensaje = ''
    mensajes = []
    for year in range(1, num_years + 1):
        capital += capital * (interes_anual / 100)
        mensaje =  'En el año ' + str(year) + ' se ha obtenido un capital de: ' + str(capital) + '€.'
        mensajes.append(mensaje)
    return '\n'.join(mensajes)

def main():
    #Entrada
    cantidad, interes_anual, num_years = func_entrada()
    #Procesamiento
    mensaje = func_capital(cantidad, interes_anual, num_years)
    #Salida
    print(mensaje)

if __name__ == '__main__':
    main()