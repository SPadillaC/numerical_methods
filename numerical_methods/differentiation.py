import numpy as np

def forward_difference(f, x, h=1e-5):
    """
    Calcula la derivada de una función f en un punto x utilizando el método de diferencia hacia adelante.
    
    Parámetros:
    f : función
        La función de la cual se quiere calcular la derivada.
    x : float
        El punto en el cual se quiere calcular la derivada.
    h : float, opcional
        El tamaño del paso. Por defecto es 1e-5.
    
    Retorna:
    float
        La derivada de f en el punto x.
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> forward_difference(f, 1)
    2.00001000001393
    """
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-5):
    """
    Calcula la derivada de una función f en un punto x utilizando el método de diferencia hacia atrás.
    
    Parámetros:
    f : función
        La función de la cual se quiere calcular la derivada.
    x : float
        El punto en el cual se quiere calcular la derivada.
    h : float, opcional
        El tamaño del paso. Por defecto es 1e-5.
    
    Retorna:
    float
        La derivada de f en el punto x.
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> backward_difference(f, 1)
    1.99999000001393
    """
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-5):
    """
    Calcula la derivada de una función f en un punto x utilizando el método de diferencia central.
    
    Parámetros:
    f : función
        La función de la cual se quiere calcular la derivada.
    x : float
        El punto en el cual se quiere calcular la derivada.
    h : float, opcional
        El tamaño del paso. Por defecto es 1e-5.
    
    Retorna:
    float
        La derivada de f en el punto x.
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> central_difference(f, 1)
    2.000000000002
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative_central(f, x, h=1e-5):
    """
    Calcula la segunda derivada de una función f en un punto x utilizando el método de diferencia central.
    
    Parámetros:
    f : función
        La función de la cual se quiere calcular la segunda derivada.
    x : float
        El punto en el cual se quiere calcular la segunda derivada.
    h : float, opcional
        El tamaño del paso. Por defecto es 1e-5.
    
    Retorna:
    float
        La segunda derivada de f en el punto x.
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> second_derivative_central(f, 1)
    2.000000165480742
    """
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2