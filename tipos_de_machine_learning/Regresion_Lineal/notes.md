## Regresión lineal

- Son tecnicas basadas en aprendizaje supervisado, va a necesitar un conjunto de datos etiquetados.

-Tambien se basan en aprendizaje basado en modelos, como un modelo lineal.

- Realiza predicciones computando una suma podenrada de las características de entrada y sumándole una constante conocida como _bias_.

- Intenta predecir valores continuos.
- La salida es un valor continuo.

(**Ver Imagen de Regresión Lineal**)

Para usar regresión lineal, necesitas:
1. Tener los datos etiquetados.
2. Tener un modelo lineal.

**Terminología**
* Conjunto de datos de entrenamiento: _training set_, conjunto de datos para que el algoritmo aprenda
* Conjunto de datos de prueba: _test set_, conjunto de datos para que el algoritmo pruebe si el modelo es correcto.

Conjunto de datos de entrenamiento:
| Número de sistemas afectados (x)| Coste en euros (y) | 
|---------------------------------|--------------------|
|              1000               |        20000       | 
|              2000               |        40000       | 
|              1200               |        23000       | 
|              1500               |        25000       |
Se pueden tener varias variables de entrada.
x = Variables de entrada (x1) (Tambien llamada _feature_ o _característica_)

* Normalmente, solo hay una variable de salida.
* Solo se quiere predecir un valor continuo.

y = Variable de salida  (tambien llamada _target_ u _objetivo_)

Se van a tener una dupla de datos de entrada y salida.
(1000, 20000) -> (x1, y)
(2000, 40000) -> (x2, y)
(1200, 23000) -> (x3, y)
(1500, 25000) -> (x4, y)
...

(**Ver imagen 2**)
