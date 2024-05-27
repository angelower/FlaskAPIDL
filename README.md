# Introducción
Este proyecto utiliza Flask para la construcción de una API que permita la clasificación de las 10 clases de la base de datos FASHION MNIST, utilizando una muy sencilla interfaz que permite carga la imagen.

# Estructura del proyecto
En este proyecto se tiene la siguiente distribución de carpetas y archivos:

>model
>>model_building.ipynb 
>>fashion_mnist_model.h5

>>test_img
>>>fashion_mnist_example.png
>>>fashion_mnist_example2.png
>>>fashion_mnist_example3.png

>>img
>>>banner_bioudea.png
>>>iris_flower.png

>templates
>>prediction.html

>app.py

>requirements.txt

>README.md

>.gitignore


* `model/model_building.ipynb` - Notebook para entrenar y guardar el modelo en un archivo con extensión 'h5'
* `model/fashion_mnist_model.h5` - Archivo que contiene el modelo entrenado
* `model/test_img.h5` - Contiene imágenes para hacer pruebas del funcionamiento de la API
* `templates/prediction.html` - Archivo HTML que se utiliza para mostrar la predicción
* `app.py` - Archivo que contiene la lógica de la API
* `requirements.txt` - Archivo que contiene las dependencias necesarias para el proyecto

# Construir el modelo
Para este ejercicio usamos el problema de clasificación de las prendas de la base de datos [FASHION MNIST](https://www.tensorflow.org/datasets/catalog/fashion_mnist?hl=es-419). Se entrena una Red Neuronal *fully connected*. El análisis de la base de datos, la contrucción del modelo en *tensorflow* y el entrenamiento de este se hace dentro del archivo `model_building.ipynb`.

# Ejecución del proyecto
### 1. Creación del ambiente vitual.
Primero debemos crear un ambiente virtual para instalar las dependencias necesarias para el proyecto.
#### Para sistema operativo Windows
- python -m venv mi_entorno
- mi_entorno\Scripts\activate
#### Para sistema operativo Linux o Mac
- python3 -m venv mi_entorno
- source mi_entorno/Scripts/activate

### 2. Instalación de las dependecias de la API
- pip install -r requirements.txt

### 3. Ejecución de la API
- python app.py

### 4. Prueba en el navegador
- Abrimos un navegador y accedemos a la dirección http://localhost:5000/
- Seleccionamos una imagen de prueba y la cargamos en el formulario.
- Se muestra la predicción de la clase de la prenda en la imagen.
