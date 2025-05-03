# EJERCICIO PRÁCTICO TEMA 2 - GRUPO 6

Se pide realizar un script que  recupere los productos de un e-commerce para 
realizar un estudio de productos, y así crear un catálogo de los productos más 
baratos y caros, en función de nuestras necesidades. 
Para ello, vamos a servirnos de la siguiente fuente externa : 
https://fakestoreapi.com/ 
Los endpoints son los siguientes: 
Acceder a todos los productos: /products 
Acceder a un solo producto :/id, siendo id un número. 
Los requisitos del ejercicio son los siguientes: 
Se pide crear las siguientes listas /y o estadísticas. 
1-  Productos disponibles. 
2-  Productos más baratos 
3- Recuperar los productos más caros 
4- Hacer una media el precio de los productos 
5- Crear lista de los productos más vendidos 
6- Crear lista de los productos con mayor rate. 

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener **Python 3.6+** instalado en tu máquina.

## Instrucciones de instalación

### 1. Crear un entorno virtual

Para crear un entorno virtual y aislar las dependencias de tu proyecto, sigue estos pasos:

#### Código para consola

```bash
# Navega a la carpeta de tu proyecto
cd C:\\ruta\\a\\tu\\proyecto
# Crea el entorno virtual
python -m venv venv
# Activa el entorno virtual
.\venv\Scripts\activate
```


### 2. Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias para el proyecto utilizando pip. Estas dependencias están listadas en el archivo requirements.txt.

```bash
pip install -r requirements.txt
```
### 5. Ejecutar el proyecto
Una vez que tengas todas las dependencias instaladas y el entorno virtual activado, puedes ejecutar el servidor de Flask con el siguiente comando:

```bash
python app.py
```