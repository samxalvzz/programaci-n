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

"""def cuadrado(n: int) -> list(list[int]):
    Devuelve un cuadrado de n * n con los números del 1 al n.
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
    Imprime el cuadrado generado por la función cuadrado().
    for fila in c:
        for e in fila:
            print(f"{e:3}", end=' ')
        print()"""

from itertools import count

def imprimir_cuadrado(c: list[list[int]]) -> None:
    """Imprime el cuadrado generado por la función cuadrado()."""
    for fila in c:
        for e in fila:
            print(f"{e:3}", end=' ')
        print()

def magico (n:int) -> list[list[int]]:    
    """Devuelve el cuadrado mágico de n * n."""
    res = [[0] * n for _ in range(n)]
    c = count(1)
    fila, col = 0, n // 2
    for _ in range (n * n):
        res[fila][col] = next(c)
        # nueva_fila = n - 1 if fila == 0 else fila - 1
        # nueva_col = 0 if col == n - 1 else col + 1
        nueva_fila, nueva_col = (fila - 1) % n, (col + 1) % n
        if res[nueva_fila][nueva_col] != 0:
            nueva_fila, nueva_col = fila + 1, col
        fila, col = nueva_fila, nueva_col
    return res

def comprobar_magico(c: list[list[int]]) -> bool:
    """Comprueba si un cuadrado es mágico."""
    
imprimir_cuadrado(magico(5))
