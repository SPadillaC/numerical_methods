import numpy as np

def linear_interp(x_vals, y_vals, x):
    """
    Interpola los valores de y para los puntos dados de x utilizando la interpolación lineal.
    
    Parámetros:
    x_vals : array_like
             Valores de x conocidos.
    y_vals : array_like
             Valores de y correspondientes a x_vals.
    x : array_like
        Valores de x para los cuales se quiere interpolar y.
    
    Retorna:
    numpy.ndarray
        Valores interpolados de y correspondientes a los valores de x dados.
    
    Ejemplo de uso:
    >>> x_vals = np.array([0, 1, 2])
    >>> y_vals = np.array([0, 1, 4])
    >>> x = np.array([0.5, 1.5])
    >>> linear_interp(x_vals, y_vals, x)
    array([0.5, 2.5])
    """
    X = x
    Y = np.array([])
    for i in range(len(x_vals) - 1):
        # Selecciona los valores de X que están en el intervalo [x_vals[i], x_vals[i+1])
        x = X[(X <= x_vals[i+1]) & (X > x_vals[i])]
        # Calcula los valores de y utilizando la fórmula de interpolación lineal
        y = (y_vals[i+1] - y_vals[i]) / (x_vals[i+1] - x_vals[i]) * (x - x_vals[i]) + y_vals[i]
        # Agrega los valores calculados a Y
        Y = np.append(Y, y)
    return Y

def P_Lagrange(x_vals, y_vals, x):
    """
    Interpola el valor de y para un punto dado de x utilizando el polinomio de Lagrange.
    
    Parámetros:
    x_vals : array_like
             Valores de x conocidos.
    y_vals : array_like
             Valores de y correspondientes a x_vals.
    x : float
        El valor de x para el cual se quiere interpolar y.
    
    Retorna:
    float
        Valor interpolado de y correspondiente al valor de x dado.
    
    Ejemplo de uso:
    >>> x_vals = np.array([0, 1, 2])
    >>> y_vals = np.array([0, 1, 4])
    >>> x = 1.5
    >>> P_Lagrange(x_vals, y_vals, x)
    2.25
    """
    def L_k(k, x):
        """
        Calcula el k-ésimo polinomio base de Lagrange en el punto x.
        
        Parámetros:
        k : int
            Índice del polinomio base de Lagrange.
        x : float
            El valor de x para el cual se quiere evaluar el polinomio base.
        
        Retorna:
        float
            Valor del k-ésimo polinomio base de Lagrange en el punto x.
        """
        L_k = 1
        for j in range(len(x_vals)):
            if j != k:
                L_k *= (x - x_vals[j]) / (x_vals[k] - x_vals[j])
        return L_k
    
    L = 0
    for k in range(len(x_vals)):
        # Suma los productos de y_vals[k] y L_k(k, x) para cada k
        L += y_vals[k] * L_k(k, x)
    
    return L