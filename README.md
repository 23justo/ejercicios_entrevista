# Ejercicios Entrevista
## Conocimiento Python
Los archivos para la solucion del ejercicio se encuentran en la carpeta [Conocimiento Python](https://github.com/23justo/ejercicios_entrevista/tree/main/Conocimiento%20Python).<br/>
el codigo fuente se encuentra en [main.py](https://github.com/23justo/ejercicios_entrevista/blob/main/Conocimiento%20Python/main.py)<br/>
la funcion principal utiliza un decorador para limpiar los parametros y la salida de la funcion principal
el decorador esta en el archivo lib/decorators.py
los archivos de pruebas estan en [test.py](https://github.com/23justo/ejercicios_entrevista/blob/main/Conocimiento%20Python/test.py)<br/>
### Correr el programa principal
```python main.py```
### Correr pruebas
```python test.py```

### Migracion a microservicios
Este ejercicio se puede ver en este [enlace](https://docs.google.com/document/d/1QCl3mwYVrfsi4jOn8LUl93WqPsoL1FbBk7EyyrapfZ4/edit?usp=sharing)


## Codigo limpio
Los archivos para la solucion del ejercicio se encuentran en la carpeta [Codigo Limpio](https://github.com/23justo/ejercicios_entrevista/tree/main/Codigo%20limpio).<br/>
Ya que se buscaba refactorizar no se utilizaron soluciones con funciones que hagan el trabajo directamente como sort o sorted, por esta misma razon se mantuvo el manejo del pivot y los ciclos.

Consideraciones
- Se modificaron los ciclos para implementar list comprehensions con el fin de separar las responsabilidades del ciclo.
- Se creo una funcion para obetener el pivot, con la intencion que si el codigo cambia sea mas facil modificar ese valor unicamente sin tener que cambiar el flujo completo.
- Se mantuvo la logica para la solucion del programa ya que no es una buena practica cambiar la logica de la funcion si esta cumple los requerimientos correctamente.
- Se cambiaron las listas a un solo diccionario para poder tener una sola variable para manejo.
- Implementacion del decorador para poder validar los parametros que llegan a la funcion con el fin de no recibir valores incorrectos.
- Se cambio el nombre de la variable pivot por random_pivot para una mejor legibilidad.
- Se mantuvieron comentarios y nombramiento de variables en español ya que era el lenguaje original del script.
### Correr el programa principal
```python main.py```
### Correr pruebas
```python test.py```
