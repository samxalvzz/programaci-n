'''
12. Escribir un programa que gestione datos almacenados en una lista, de forma que muestre
un menú con las siguientes opciones:
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.
El programa deberá pedir la información necesaria para cada opción elegida por el
usuario
'''

def mostrar_menu():
    '''Muestra el menú'''
    print('''
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.''')


def elegir_opcion():
    ''' Pide al usuario la opción que desea .'''
    return = input("Introduzca la opción deseada: ")



lista = []
while True:
    mostrar_menu()
    opc = elegir_opcion()
    if opc == "1":
        añadir_elemento(lista)
    elif opc == "2":
        cambiar_elemento(lista)
    elif opc == "3":
        eliminar_elemento(lista)
    elif opc == "4":
        eliminar_todos(lista)
    elif opc == "5":
        mostrar_elementos(lista)
    elif opc == "0":
        break
    else:
        print("Opción Incorrecta")

