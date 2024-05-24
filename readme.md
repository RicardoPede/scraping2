## Obtención de imagenes con Python
### ● Funcionalidad:
El web scraper debe ser capaz de recorrer el sitio web de manera efectiva y extraer todas
las etiquetas <img> con sus atributos src.
Debe descargar cada imagen encontrada y guardarla en una carpeta especificada.
La carpeta debe ser validada: si no existe, debe ser creada automáticamente.
Solo se deben descargar imágenes con los formatos png, jpg y webp.
### ● Manejo de Errores:
El programa debe manejar adecuadamente situaciones de error, como imágenes no
encontradas, errores de conexión, o problemas de formato de HTML.
Si una imagen no se puede descargar, el programa debe continuar con la siguiente.
### ● Legibilidad y Organización del Código:
El código debe estar bien organizado y estructurado, con nombres descriptivos de
variables y funciones.
### ● Presentación del Trabajo Práctico:
La presentación del trabajo práctico debe realizarse en un repositorio de GitHub, el cual
debe ser público para su posterior revisión y evaluación.

## Objetivo:
El objetivo de este trabajo práctico es implementar un web scraper en Python que pueda
recorrer un sitio web, extraer todas las etiquetas <img> con sus atributos src y descargar cada
imagen en una carpeta llamada “imagenes”. Si la carpeta no existe, el programa debe crearla
automáticamente. Solo se deben descargar imágenes con los formatos png, jpg y webp.

## Notas Adicionales:
Se deben usar la librería BeautifulSoup y requests.
El programa primero válida si la carpeta existe y, de no ser así, se debe crear.
Se recorren todas las etiquetas <img> de la página dada, se obtienen los enlaces src y se
descargan las imágenes en la carpeta especificada, siempre y cuando sean de los formatos png,
jpg, y webp.
Se manejan errores de conexión y descarga para asegurar que el programa no se detenga ante
cualquier problema.

### ● Aclaraciones:
● Se recomienda utilizar un entorno virtual para la ejecución del programa.
● Se recomienda utilizar un archivo requirements.txt para listar las librerías necesarias.
● Se recomienda utilizar un archivo .gitignore para evitar subir archivos innecesarios al
repositorio.
● Se recomienda utilizar un archivo README.md para la descripción del trabajo práctico.

## Ejecución:
Para ejecutar el programa, se debe correr el archivo main.py con el comando python main.py.
Se debe ingresar la URL de la página web de la cual se desean obtener las imágenes.
Se debe esperar a que el programa descargue todas las imágenes y las guarde en la carpeta
“imagenes”.

habilitando entorno de trabajo virtual:
```bash
python -m venv venv
source venv/Scripts/activate
```
si source no funciona, es suficiente con ejecutar el siguiente comando:
```bash
venv/Scripts/activate
```

instalando librerias necesarias:
```bash
pip install -r requirements.txt
```

ejecutando el programa:
```bash
python main.py
```