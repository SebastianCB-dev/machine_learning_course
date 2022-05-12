# Import
import numpy as np

# Arrays
# Array cuyos valores son todos 0
a = np.zeros((2, 4))
"""
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.]])
"""

a.shape # (2,4)
a.ndim # 2
a.size # 8

#! Creación Arrays
# Array cuyos valores son todos 0
np.zeros((2, 3, 4))
"""
array([[[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]],

       [[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]]])
"""

# Array cuyos valores son todos 1
np.ones((2, 3, 4))
"""
array([[[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]],

       [[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]]])
"""

# Array cuyos valores son todos el valor indicado como segundo parámetro de la función
np.full((2, 3, 4), 8)
"""
array([[[8, 8, 8, 8],
        [8, 8, 8, 8],
        [8, 8, 8, 8]],

       [[8, 8, 8, 8],
        [8, 8, 8, 8],
        [8, 8, 8, 8]]])
"""

# El resultado de np.empty no es predecible 
# Inicializa los valores del array con lo que haya en memoria en ese momento
np.empty((2, 3, 9))

"""
array([[[ 2.31584178e+077, -1.49457241e-154,  2.24704384e-314,
          2.24703961e-314,  2.24703803e-314,  2.24059351e-314,
          2.24704094e-314,  2.24704777e-314,  2.24703958e-314],
        [ 2.24703739e-314,  2.24703980e-314,  2.24703344e-314,
          2.24704170e-314,  2.24704720e-314,  2.24704043e-314,
          2.26943022e-314,  2.26943028e-314,  2.26857648e-314],
        [ 2.26864577e-314,  2.24703942e-314,  2.24703945e-314,
          2.24703983e-314,  2.24704008e-314,  2.24704011e-314,
          2.24704736e-314,  2.24704745e-314,  2.24704739e-314]],

       [[ 2.24704764e-314,  2.24704087e-314,  2.26859791e-314,
          2.26859772e-314,  2.26859855e-314,  2.26859779e-314,
          2.26859863e-314,  2.31584178e+077,  2.31584178e+077],
        [ 2.24076228e-314,  2.24133656e-314,  0.00000000e+000,
          0.00000000e+000,  0.00000000e+000,  4.94065646e-324,
          4.94065646e-324,  0.00000000e+000,  0.00000000e+000],
        [ 2.26958240e-314,  0.00000000e+000,  0.00000000e+000,
          0.00000000e+000,  2.26958233e-314,  2.26958233e-314,
          0.00000000e+000, -1.29073793e-231,  3.75914434e-308]]])
"""

# Inicializacion del array utilizando un array de Python
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

b.shape # (2,3)

# Creación del array utilizando una función basada en rangos
# (minimo, maximo, número elementos del array)
print(np.linspace(0, 6, 10))

"""
[0.         0.66666667 1.33333333 2.         2.66666667 3.33333333
 4.         4.66666667 5.33333333 6.        ]
"""

# Inicialización del array con valores aleatorios
np.random.rand(2, 3, 4)

"""
array([[[0.03378783, 0.51370292, 0.0448622 , 0.59146622],
        [0.65020737, 0.98552739, 0.02602994, 0.23295317],
        [0.61644088, 0.74966376, 0.98919117, 0.10470065]],

       [[0.43496062, 0.5189665 , 0.6438961 , 0.75687474],
        [0.76658059, 0.27930081, 0.70681049, 0.74179797],
        [0.39368796, 0.2892813 , 0.85135049, 0.84055115]]])
"""

# Inicialización del Array utilizando una función personalizada

def func(x, y):
    return x + 2 * y

np.fromfunction(func, (3, 5))
"""
array([[ 0.,  2.,  4.,  6.,  8.],
       [ 1.,  3.,  5.,  7.,  9.],
       [ 2.,  4.,  6.,  8., 10.]])
"""

# Creación de un Array unidimensional
array_uni = np.array([1, 3, 5, 7, 9, 11])
print("Shape:", array_uni.shape) # 1
print("Array_uni:", array_uni) 

# Accediendo al quinto elemento del Array
array_uni[4]

# Accediendo al tercer y cuarto elemento del Array
array_uni[2:4]

# Accediendo a los elementos 0, 3 y 5 del Array
array_uni[0::3]

# Creación de un Array multidimensional
array_multi = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape:", array_multi.shape)
print("Array_multi:\n", array_multi)

# Accediendo al cuarto elemento del Array
array_multi[0, 3]

# Accediendo a la segunda fila del Array
array_multi[1, :]

# Accediendo al tercer elemento de las dos primeras filas del Array
array_multi[0:2, 2]

# Creación de un Array unidimensional inicializado con el rango de elementos 0-27
array1 = np.arange(28)
print("Shape:", array1.shape)
print("Array 1:", array1)

# Cambiar las dimensiones del Array y sus longitudes
array1.shape = (7, 4)
print("Shape:", array1.shape)
print("Array 1:\n", array1)

# El ejemplo anterior devuelve un nuevo Array que apunta a los mismos datos. 
# Importante: Modificaciones en un Array, modificaran el otro Array
array2 = array1.reshape(4, 7)
print("Shape:", array2.shape)
print("Array 2:\n", array2)

# Modificación del nuevo Array devuelto
array2[0, 3] = 20
print("Array 2:\n", array2)

# Desenvuelve el Array, devolviendo un nuevo Array de una sola dimension
# Importante: El nuevo array apunta a los mismos datos
print("Array 1:", array1.ravel())

# Creación de dos Arrays unidimensionales
array1 = np.arange(2, 18, 2)
array2 = np.arange(8)
print("Array 1:", array1)
print("Array 2:", array2)

# Suma
print(array1 + array2)

# Resta
print(array1 - array2)

# Multiplicacion
# Importante: No es una multiplicación de matrices
print(array1 * array2)


#! Broadcasting
# Creación de dos Arrays unidimensionales
array1 = np.arange(5)
array2 = np.array([3])
print("Shape Array 1:", array1.shape)
print("Array 1:", array1)
print()
print("Shape Array 2:", array2.shape)
print("Array 2:", array2)

# Suma de ambos Arrays
array1 + array2

# ! Funciones estadisticas sobre arrays
# Creación de un Array unidimensional
array1 = np.arange(1, 20, 2)
print("Array 1:", array1)

# Media de los elementos del Array
array1.mean()

# Suma de los elementos del Array
array1.sum()

# Cuadrado de los elementos del Array
np.square(array1)

# Raiz cuadrada de los elementos del Array
np.sqrt(array1)

# log de los elementos del Array
np.log(array1)

# Exponencial de los elementos del Array
np.exp(array1)