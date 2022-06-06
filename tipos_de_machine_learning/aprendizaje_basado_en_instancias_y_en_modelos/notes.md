## Aprendizaje basado en instancias y en modelos

* ### Aprendizaje basado en instancias: 
El sistema aprende los ejemplos del conjunto de datos de entrenamiento y luego intenta generalizar para nuevos ejemplares.
Se requiere una **medida de similitud** para determinar la similitud entre los ejemplos de entrenamiento y los ejemplos de prueba.
**Medida de similitud** = Cuando tengamos un nuevo ejemplar, lo comparamos con los ejemplos de entrenamiento y nos quedamos con el que tiene mayor similitud.
- Aprende especificamente para cada ejemplo de entrenamiento.
- Aprende generalmente para todos los ejemplos de entrenamiento.
- Cuando agregamos un nuevo ejemplo de entrenamiento, el sistema intenta **generalizarlo**.

* ### Aprendizaje basado en modelos:
- Se crea un modelo que describe el conjunto de datos y se utiliza para realizar predicciones.
- Se requiere ajustar los **parámetros del modelo**.

No aprenderan con el conjunto de datos, si no que crearán una función e intentarán generalizarla con base en los ejemplos de prueba.

- Función hipotética:
Es una función que describe un conjunto de datos.
Tambien es conocida como **modelo de regresión**.
