### Aprendizaje Online y Batch

* ###### Aprendizaje Batch
Los sistemas basados en aprendizaje batch **no aprenden de manera incremental**, se entrenan utilizando todos los datos disponibles.

Si los datos cambian, debemos ajustar los datos y volver a entrenar.

- Si se desea que el sistema se adapte a un nuevo tipo de dato, se debe entrenar de nuevo con todos los datos disponibles.
- Solución sencilla
- Funciona bien para sistemas que no requieren un conjunto de datos muy grande ni adaparte a nuevos datos de manera muy rápida.
- Muy restringido para dispotivos con una capacidad limitada de memoria, como un smartphone.


* ###### Aprendizaje Online
Los sistemas basados en aprendizaje online **se entrenan incrementalmente**, mediante el consumo incremental de datos, ya sea individuales o en pequeños grupos (mini-batches)

Una vez este algoritmo esta en producción, este puede continuar entrenando con datos nuevos, sin necesidad de volver a entrenar.

- Solución ideal para sistemas que reciben datos **continuamente**, como una base de datos y requieren adaptarse a ellos de manera rápida.
- Es capaz de lidiar con grades conjuntos de datos que puede que no entren en una sola maquina.
- Aparecen algunas variables importantes que hay que determinar, como el ratio de aprendizaje.
- Pueden ser muy inestables si por alguna razón se consumen datos de baja calidad.

