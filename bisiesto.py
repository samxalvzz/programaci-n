'''
Escribir un programa que pida al usuario un número que representa un año
y determine si ese año es bisiesto o no.

divisible entre 4 y no divisible entre 100 ó divisible entre 400.
'''

año = int(input("Introduzca el año: "))
p = año % 4 == 0
q = año % 100 == 0
r = año % 400 == 0

if (p and not q) or r:
    print("Si es bisiesto")
else:
    print("No es bisiesto")

''' otra manera donde solamente podemos unir todo en un mismo solo if
    
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
'''