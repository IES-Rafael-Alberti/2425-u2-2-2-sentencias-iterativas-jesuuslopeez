'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''
def func_entrada():
    frase = input('Introduce una frase: ')
    letra = input('Introduce una letra: ')
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError('No puedes introducir números ni carácteres especiales.')
    return frase, letra

def func_contador_letras(frase, letra):
    contador = frase.lower().count(letra.lower())
    return contador

def main():
    #Entrada
    frase, letra = func_entrada()
    #Procesamiento
    contador = func_contador_letras(frase, letra)
    letra = letra.upper()
    #Salida
    print(f'La letra {letra} aparece {contador} veces en esta frase:\n{frase}')

if __name__ == '__main__':
    main()

