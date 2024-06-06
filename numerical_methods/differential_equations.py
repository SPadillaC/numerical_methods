import numpy as np

def euler_method(f, y0, t0, tf, h):
    """
    Resuelve una ecuación diferencial ordinaria (EDO) utilizando el método de Euler.
    
    Parámetros:
    f  : función
         La función que define la EDO, de la forma f(t, y), donde t es el tiempo e y es el valor de la función en el tiempo t.
    y0 : float
         Valor inicial de y en t0 (condición inicial).
    t0 : float
         Tiempo inicial.
    tf : float
         Tiempo final.
    h  : float
         Tamaño del paso (incremento de tiempo).
    
    Retorna:
    t_values : numpy.ndarray
               Arreglo de valores de tiempo desde t0 hasta tf con incrementos de h.
    y_values : numpy.ndarray
               Arreglo de valores de y correspondientes a cada valor de tiempo en t_values.
    
    Ejemplo de uso:
    >>> def f(t, y):
    >>>     return -2 * y + t
    >>> t, y = euler_method(f, y0=1, t0=0, tf=2, h=0.1)
    """
    # Crear un arreglo de valores de tiempo desde t0 hasta tf con incrementos de h
    t_values = np.arange(t0, tf + h, h)
    
    # Inicializar un arreglo de ceros para los valores de y
    y_values = np.zeros(len(t_values))
    
    # Establecer la condición inicial
    y_values[0] = y0
    
    # Iterar sobre el rango de tiempo para calcular los valores de y usando el método de Euler
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
    
    return t_values, y_values