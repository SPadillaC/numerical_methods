# Numerical Methods

Esta es una librería de métodos numéricos que incluye funciones para diferenciación, integración, interpolación, y resolución de ecuaciones diferenciales, todas enseñadas y aplicadas en clases en Física Computacional III.

Última actualización: 06/06/2024

## Instalación

Puedes clonar este repositorio y usar los scripts directamente.

```sh
git clone https://github.com/tu-usuario/numerical_methods.git
```

O simplemente descargando la carpeta con los métodos y pegándola en la misma carpeta donde tienes planeado programar las clases.

## ¿Cómo usar las funciones?

```python

# Ejemplo de uso

import numpy as np
import matplotlib.pyplot as plt
from numerical_methods import euler_method

# Definir la ecuación diferencial
def f(t, y):
    return y**2 * np.exp(t)

# Condiciones iniciales
y0 = 0.5
t0 = 0
tf = 2
h = 0.1

# Solución analítica
def analytical_solution(t):
    return 1 / (np.exp(t) - 2)

# Resolver la ecuación diferencial usando el método de Euler
t_values, y_values = euler_method(f, y0, t0, tf, h)

# Calcular la solución analítica
t_analytical = np.linspace(t0, tf, 100)
y_analytical = analytical_solution(t_analytical)

# Graficar las soluciones
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, 'o-', label='Método de Euler')
plt.plot(t_analytical, y_analytical, '-', label='Solución Analítica')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Método de Euler vs Solución Analítica')
plt.legend()
plt.grid(True)
plt.show()
```
```python

# Otro ejemplo, con múltiples métodos

import numpy as np
import matplotlib.pyplot as plt
from numerical_methods import central_difference, integral_riemann, integral_trapezoidal

# Definir la función a derivar e integrar
def f(x):
    return np.cos(x)

# Punto en el que se calculará la derivada
x = np.pi / 4

# Calcular la derivada central
derivada_central = central_difference(f, x)
print(f"La derivada central de f(x) en x={x} es: {derivada_central}")

# Definir los límites de integración
a = 0
b = np.pi
n = 1000  # número de subintervalos

# Calcular la integral usando los métodos de Riemann, trapezoidal y Simpson
I_riemann = integral_riemann(f, a, b, n)
I_trapezoidal = integral_trapezoidal(f, a, b, n)

print(f"La integral calculada numéricamente con el método de Riemann es: {I_riemann}")
print(f"La integral calculada numéricamente con el método trapezoidal es: {I_trapezoidal}")
```
```python

# Si no recuerdan cómo usar un método, o qué argumentos tiene la función, pueden hacer lo siguiente:

from numerical_methods import integral_simpson

help(integral_simpson)

# Esto les va a devolver:
```
![image](https://github.com/SPadillaC/numerical_methods/assets/143565516/039f8254-ea76-49bc-919c-1b058bf74f9e)

