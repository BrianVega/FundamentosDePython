def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if(palabra) == palabra_invertida:
        return True
    else:
        return False
     


def run():#Función principal, como el main
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('NO es palíndromo ')


if __name__ == '__main__':#Punto de entrada de un programa de python
    run()