""" 
1r Punto . esPrimo(numero).Decir si un número es primo o no. 

Teoría: Un número primo es un número natural mayor que 1 que tiene 
    únicamente dos divisores distintos: él mismo y el 1.
    
    Argumentos:
        numero: El número entero a verificar.
        
    Retorna:
        True si es primo, False en caso contrario.
        
    Excepciones:
        TypeError: Si el argumento no es un número entero.
    """



def esPrimo(numero):
    if not isinstance(numero, int):
        raise TypeError("Debe ser un número entero")
    if numero < 2:
        return False
    
    # El bucle busca si hay algún divisor
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False # Si encuentra uno, NO es primo.
            
    
    return True

""" 
2n Punto primos(numero). Dar una lista de todos los primos hasta ese número. 

Devuelve una tupla con todos los números primos menores que el argumento.
    
    Teoría: Recorremos los números desde 2 hasta el límite y usamos 
    la función esPrimo() para saber cuáles incluir en la lista.


"""  


def primos(numero):
    if not isinstance(numero, int): # Validación de tipo requerida que sea int para evitar errores al usar range()
        raise TypeError("El argumento debe ser un número entero") # defini el error 
    # Creamos la lista de primos menores que 'numero'
    lista = [n for n in range(2, numero + 1) if esPrimo(n)] 
    # 'n' recorre el rango desde 2 hasta numero-1
    # Por cada 'n', llamamos a la función esPrimo(n)
    # Si esPrimo(n) es True, el número se guarda en la lista    
    return tuple(lista) 
  # El enunciado pide una tupla específicamente. Las tuplas ocupan 
  # menos memoria y no se pueden modificar, lo que asegura los datos. 

""" 
3r Punto descompon(numero).Decir qué factores primos forman un número
 Devuelve una tupla con la descomposición en factores primos.
    Ejemplo: descompon(12) -> (2, 2, 3) 
    
""" 


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos.
    Teoría: Basado en el Teorema Fundamental de la Aritmética.
    """
    if not isinstance(numero, int):
        raise TypeError("El argumento debe ser un número entero")
    
    factores = []
    divisor = 2
    temp = numero
    
    while temp > 1:
        if temp % divisor == 0:
            factores.append(divisor)
            temp //= divisor
        else:
            divisor += 1 #
            
    return tuple(factores) # 

"""
4r Punto mcm(n1, n2).Calcular el mínimo común múltiplo.

Teoría: El MCD de dos números es el producto de sus factores primos comunes elevados al menor exponente.
En el código: Comparamos las dos listas de factores y nos quedamos solo con los que se repiten en ambas.

2. Mínimo Común Múltiplo (MCM)

Teoría: Existe una propiedad matemática muy útil: MCM(a,b)=  a por b / MCM(a,b)
En el código: Multiplicamos los dos números y dividimos el resultado por el MCD que ya calculamos.

"""

def mcd(n1, n2):
    """
    Calcula el Máximo Común Divisor de dos números.
    Teoría: Factores comunes con el menor exponente.
    """
    f1 = list(descompon(n1)) # f1 se convierte en una lista de sus factores primos: [2, 2, 3, 7, 11]. Hacemos list() para poder borrar                                elementos luego.
    f2 = list(descompon(n2)) # Creamos una lista vacía donde guardaremos solo los "cromos repetidos" (factores que estén en ambos                                      números).
    comunes = []
    
    for f in f1:    #  Empezamos a revisar cada factor del primer número.        
        if f in f2: # ¿Este factor también está en la lista del segundo número?"
            comunes.append(f) #Si la respuesta es sí, lo guardamos en nuestra lista de comunes.
            f2.remove(f) # Evitamos contar el mismo factor dos veces 
            
    res = 1
    for x in comunes:
        res *= x  # Multiplicamos todos los números que guardamos en la lista comunes.
    return res

def mcm(n1, n2):
    """
    Calcula el Mínimo Común Múltiplo de dos números.
    Teoría: Propiedad mcm(a,b) = (a*b) / mcd(a,b)
    """
    return (n1 * n2) // mcd(n1, n2) 

"""
5t Punto mcd(n1, n2).Calcular el máximo común divisor.

    Calcula el máximo común divisor de dos números.
    Teoría: Obtenemos los factores primos de ambos y multiplicamos los comunes.
    

""" 

def mcd(n1, n2):

    f1 = list(descompon(n1))
    f2 = list(descompon(n2))
    comunes = []
    
    for f in f1:
        if f in f2:
            comunes.append(f)
            f2.remove(f) # Evitamos contar el mismo factor dos veces
            
    res = 1
    for x in comunes:
        res *= x
        
    return res



def Mcm(*numeros):
    """Devuelve el mínimo común múltiplo de sus argumentos."""
    # Tu código actual para calcular el mcm, pero aplicado a la lista 'numeros'
    # O usando la librería math que es más directa para varios números:
    import math
    return math.lcm(*numeros)

def Mcd(*numeros):
    """Devuelve el máximo común divisor de sus argumentos."""
    import math
    return math.gcd(*numeros)

    