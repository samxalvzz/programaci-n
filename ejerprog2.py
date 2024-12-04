'''
Escribir una funcion dict2list que convierta un diccionario
en una lista, con base en la siguiente especificacion informal:

- Debe recibir como argumento un diccionario.
- Debe ser una funcion pura.
- Las claves del diccionario deben ser enteros y representan indices
de los elementos de la lista.
-Los valores del diccionario pueden ser de cualquier tipo y representan
los elementos almacenados en la lista.
- Si hay huecos que rellenar en mitad de la lista, deben rellenarse con None.
- La lista no debe tneer más elementos de los necesarios.
'''

def dict2list(dic: dict) -> list:
    """
    dict2list({0: 'a', 2: 'c', 1: 'b'}) # => ['a', 'b', 'c']
    dict2list({2: 'c', 0: 'a'}) # => ['a', None, 'c']
    """
    res = [None] * (max(dic) + 1)
    for k, v in dic.items():
        res[k] = v
    return res
  

