import numpy as np

def integral_riemann(f, a, b, n):
    """
    Calcula la integral definida de una función f en el intervalo [a, b] utilizando la suma de Riemann.
    
    Parámetros:
    f : función
        La función a integrar.
    a : float
        El límite inferior de integración.
    b : float
        El límite superior de integración.
    n : int
        El número de subintervalos en los que se divide [a, b].
    
    Retorna:
    float
        La aproximación de la integral de f en [a, b].
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> integral_riemann(f, 0, 1, 100)
    0.3333333350000001
    """
    dx = (b - a) / n  # Tamaño del subintervalo
    x_i = np.linspace(a, b, n)  # Puntos en el intervalo
    y_i = f(x_i)  # Valores de la función en los puntos
    return np.sum(y_i * dx)  # Suma de Riemann

def integral_trapezoidal(f, a, b, n):
    """
    Calcula la integral definida de una función f en el intervalo [a, b] utilizando la regla del trapecio.
    
    Parámetros:
    f : función
        La función a integrar.
    a : float
        El límite inferior de integración.
    b : float
        El límite superior de integración.
    n : int
        El número de subintervalos en los que se divide [a, b].
    
    Retorna:
    float
        La aproximación de la integral de f en [a, b].
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> integral_trapezoidal(f, 0, 1, 100)
    0.33335
    """
    dx = (b - a) / n  # Tamaño del subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos en el intervalo
    y = f(x)  # Valores de la función en los puntos
    I = dx * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])  # Suma de trapecios
    return I

def integral_simpson(f, a, b, n):
    """
    Calcula la integral definida de una función f en el intervalo [a, b] utilizando la regla de Simpson.
    
    Parámetros:
    f : función
        La función a integrar.
    a : float
        El límite inferior de integración.
    b : float
        El límite superior de integración.
    n : int
        El número de subintervalos en los que se divide [a, b]. Debe ser par.
    
    Retorna:
    float
        La aproximación de la integral de f en [a, b].
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2
    >>> integral_simpson(f, 0, 1, 100)
    0.33333333333333337
    """
    if n % 2 == 1:
        n += 1  # La regla de Simpson requiere un número par de intervalos
    dx = (b - a) / n  # Tamaño del subintervalo
    x = np.linspace(a, b, n + 1)  # Puntos en el intervalo
    y = f(x)  # Valores de la función en los puntos
    I = dx / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])  # Suma de Simpson
    return I