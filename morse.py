def morse (mensaje: str) -> str:
    cars_a_puntos = {
        
        
        
        
        
        
        
        
        
        
        }
        return " ".join(cars_a_puntos[c] for c in mensaje.upper() if c in cars_a_puntos)
    
    print(morse("CHALLeNGE") == "")
    print(morse("HELP ME !") == "")