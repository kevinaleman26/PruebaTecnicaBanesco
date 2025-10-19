# Prueba Técnica Banesco

## Descripción del proyecto

Proyecto creado para la evaluación técnica de Banesco.

Se requiere evaluar tres fuentes de datos, realizar un cruce de información
entre todas ellas y crear un archivo llamado **`integration_output.json`**, que
contendrá una lista de objetos con el cruce por usuario.

Se tomaron en cuenta las siguientes fuentes de datos:

- **API de Usuarios (JSON)**: https://jsonplaceholder.typicode.com/
- **API del Clima (JSON)**: https://openweathermap.org/api (Requiere API KEY)
- **Datos de Pedidos (CSV)**:\
  https://www.google.com/search?q=https://www.contextures.com/SampleData.zip\
  (En la segunda hoja del Excel se encuentra la lista de transacciones, la cual
  debe ser guardada en un archivo llamado: `orders.csv`)

## Análisis

Se proponen los siguientes pasos para la realización de la solución:

1. Leer el API de usuarios.
2. Leer el API del clima pasándole la latitud y longitud obtenidas del API de
   usuarios.
3. Leer el archivo `orders.csv`, segmentar la lista por nombres de cliente para
   evaluar las unidades y el total de ventas.
4. Cruzar los datos para obtener la respuesta de cada usuario y acumularla en
   una lista.
5. Guardar el resultado de la lista en un archivo llamado
   **`integration_output.json`**.

Se observa que las distintas fuentes de datos no generan un volumen de
información lo suficientemente grande como para requerir una base de datos.\
Por ello, se opta por realizar el cruce de información directamente en memoria.

## Solución

Se realizaron soluciones de forma diferente con el fin de mostrar dominio del
lenguaje Python.\
Una solución se desarrolló con **Jupyter**, que fue la primera herramienta
utilizada para el análisis de datos.

Posteriormente, se tomaron los resultados y se estructuraron en un proyecto
estándar de Python.

**Ambas soluciones generan los mismos resultados en el archivo
`integration_output.json`.**

### Jupyter

#### Ruta principal

```
cd jupyter
```

#### Ejecutar el Jupyter Notebook

Abrir el archivo: "prueba_tecnica.ipynb" Ejecutar el notebook y se generará el
archivo: "integration_output.json"

### Python

#### Ruta principal

```
cd python
```

#### Instalar dependencia

```
pip install -r requirements.txt
```

o

```
pip3 install -r requirements.txt
```

#### Iniciar programa

```
python main.py
```

o

```
python3 main.py
```

#### Salida

Se genera el archivo: "integration_output.json"

## Justificacion de la solucion

A pesar de que el proyecto permitía el uso de herramientas tipo no-code, se optó
por desarrollar la solución mediante código, ya que Jupyter Notebook es una
excelente herramienta para el análisis de datos. En ella se realizó el análisis
de las respuestas y de las distintas fuentes, así como el cruce de información
necesario para obtener el resultado final.

Una vez obtenido el resultado, migrar todo a un proyecto más formal resulta
sencillo.

De igual forma, conociendo ya el resultado, mover la solución a otro tipo de
herramientas —ya sean no-code o basadas en contenedores— se vuelve mucho más
simple.

## Posibles soluciones

Se evaluó el uso de otras herramientas:

- **N8N** : Se pudo utilizar para orquestar las fuentes de datos y realizar el
  cruce de información a través de una interfaz no-code. No se usó esta
  herramienta porque hubiera requerido montar un servidor para la aplicación
  (mediante un contenedor o instalación directa en el equipo con Node.js). Al
  ser un proyecto pequeño y de ejecución única, no se consideró necesario
  implementar esta solución.
- **Uso de contenedores**: Requiere instalar Docker en el equipo para descargar
  las dependencias del proyecto, las cuales podrían incluir una base de datos
  (en caso de datasets más grandes), un app server para la ejecución del código
  Python o una instancia de N8N para orquestar la información. Sin embargo, dado
  que el caso de uso es sencillo, se decidió no implementar una solución tan
  compleja.
