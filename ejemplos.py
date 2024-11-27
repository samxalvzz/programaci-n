'''
def f(x):
    x = 5
    return 7

z = 9
y = f(z)
'''

def cambia(l):
    print(l)
    l.append(99)

lista = [1, 2, 3]
cambia(lista)      #Imprime [1, 2, 3]
print (lista)      #Imprime [1, 2, 3, 99]

'''
Cambia es una función impura porque provoca un efecto
lateral: modifica su argumento mutable.
'''

