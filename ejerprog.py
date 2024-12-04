def list2dict(lista: list) -> dict:
    """Devuelve el diccionario equivalente a una lista."""
    return { i:e for i, e in enumerate(lista)}
    
    res = {}
    for i, e in enumerate(lista):
        res[i] = e
    return res
