'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''
def func_entrada():
    cantidad = float(input('Introduce la cantidad a invertir: '))
    interes_anual = float(input('Introduce el interés anual: '))
    num_years = int(input('Introduce el número de años: '))
    if cantidad <= 0:
        raise ValueError('La cantidad a invertir tiene que ser mayor a 0.')  
    if interes_anual <= 0:
        raise ValueError('El interes anual tiene que ser mayor a 0.')
    if num_years <= 0:
        raise ValueError('El número de años tiene que ser mayor a 0.')
    return cantidad, interes_anual, num_years

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