

empleados = [
    ('Maria', 'Gonzalez', 1800.23),
    ('Javier', 'Ruiz', 1630.50),
    ('Jesús', 'Pérez', 2100.42),
    ('Rosa', 'Muñoz', 2240.78)
]

suma = 0
for i, emple in enumerate(empleados):
    nombre, apellidos, salario = emple
    salario = round(salario * 1.10, 2)
    print("Empleado", nombre, apellidos, "con salario", salario)
    suma += salario
print("El salario total es", suma)
print(empleados)


   
'''
lista = [ 'a', 'b', 'c']

for i, _ in enumerate(lista):
    lista[i] *= 2

print(lista)
'''
    