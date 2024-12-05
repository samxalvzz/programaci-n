'''
Ej Cuadrados
(Ya todo se verá hecho)

cuadrado(3) =
[ 1  2  3
  4  5  6  = [[1,2,3],[4,5,6],[7,8,9]]
  7  8  9 ]
  
cuadrado(2) =
[ 1 2
  3 4] = [[1,2],[3,4]]
  
cuadrado(1)=
[1
  ]  = [[1]]
'''

def cuadrado(n: int) -> list(list[int]):
    """Devuelve un cuadrado de n * n con los números del 1 al n. """
    res = []
    c = 1
    for i in range(n):
        f = []
        for i in range(n):
            f.append(c)
            c += 1
        res.append(f)
    return res

def imprimir_cuadrado(c: list[list[int]]) -> None:
    """Imprime el cuadrado generado por la función cuadrado()."""
    for fila in c:
        for e in fila:
            print(f"{e:3}", end=' ')
        print()
        
    
    
imprimir_cuadrado(cuadrado(10))
    

