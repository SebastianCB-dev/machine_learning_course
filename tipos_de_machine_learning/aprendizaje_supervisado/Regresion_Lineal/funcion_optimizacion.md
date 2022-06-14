## Función de coste
J(θ) = 1/2m * sum( (h(x) - y)^2 )

- Minimizar el error cuadrático medio

J(x) = (x-3)^2

## Algoritmo de optimización (gradiente descendente)

Gradiente = Pendiente = Derivada de la función de coste
d/dx J(θ) = d/dx (x-3)^2 = 2x - 6

Inicializar el valor de x
x = 4
d/dx x = 2 -> Se aleja del valor deseado
x = 2
d/dx x = -2

## Función de optimización
J(x) = (x-3)^2
d/dx J(x) = 2x - 6
x = x - rate * d/dx J(x) 
x = 8 - 1/2 * 10 = 3
---
x = 3
x = 3 - 1/2 * 0 = 3


