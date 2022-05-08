menu = """
Bienvenido al conversor de monedas 😊🤑

1 - Pesos Colombianos 
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción """

opcion = input(menu)

if opcion == '1':
    valor_dolar = 3875
    pais = 'colombianos'
elif opcion == '2':
    valor_dolar = 65
    pais = 'argentinos'
elif opcion == '3':
    valor_dolar = 24
    pais = 'mexicanos'
else:
    print('Ingresa una opción correcta por favor')

pesos = input('¿Cuántos pesos ' + pais + ' tienes? ')
pesos = float(pesos)
#valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $'+ dolares + ' dólares')