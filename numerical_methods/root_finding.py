def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función f utilizando el método de Newton-Raphson.
    
    Parámetros:
    f        : función
               La función de la cual se quiere encontrar la raíz.
    f_prime  : función
               La derivada de la función f.
    x0       : float
               Valor inicial para la iteración.
    tol      : float, opcional
               Tolerancia para el criterio de convergencia. Por defecto es 1e-6.
    max_iter : int, opcional
               Número máximo de iteraciones permitidas. Por defecto es 100.
    
    Retorna:
    float
        Aproximación de la raíz de la función f.
    
    Lanza:
    ValueError
        Si no se encuentra una solución dentro del número máximo de iteraciones.
    
    Ejemplo de uso:
    >>> def f(x):
    >>>     return x**2 - 2
    >>> def f_prime(x):
    >>>     return 2 * x
    >>> newton_raphson(f, f_prime, x0=1)
    1.414213562373095
    """
    x_n = x0  # Valor inicial para la iteración
    
    for _ in range(max_iter):
        # Calcula el siguiente valor utilizando la fórmula de Newton-Raphson
        x_n1 = x_n - f(x_n) / f_prime(x_n)
        
        # Verifica si la diferencia absoluta entre las iteraciones es menor que la tolerancia
        if abs(x_n1 - x_n) < tol:
            return x_n1  # Retorna la raíz encontrada
        
        x_n = x_n1  # Actualiza el valor de x_n para la siguiente iteración
    
    # Lanza una excepción si no se encuentra una solución dentro del número máximo de iteraciones
    raise ValueError(f'No se encontró una solución dentro de {max_iter} iteraciones')