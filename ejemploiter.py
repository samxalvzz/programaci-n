'''
Ejemplo de iterador
'''

t = ('a', 'b', 'c', 'd')


it = iter(t)
while True:
    try:
        elem = next(it)
        print(elem)
    except StopIteration:
        break
    

'''
t = ('a', 'b', 'c', 'd')

for elem in :
    print(elem)
'''

for elem in filter(lambda x: x % 3 == 0, range(10)):
    print(elem)
    