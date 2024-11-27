'''
Implementación recursiva de la función factorial usando bucles
'''

def factorial(n):
    ### Calcular el factorial de un número. ###
    res = 1
    while n >= 1:
        res *= n
        n -= 1
    return res
    
    
    
print(factorial(1000))