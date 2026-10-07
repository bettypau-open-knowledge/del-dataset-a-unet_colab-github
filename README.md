# GitHub, Google Colab y Google Drive

Repositorio de práctica del taller **Del dataset a U-Net: segmentación de imágenes con Deep Learning**.

Este proyecto contiene un ejemplo sencillo para explorar el flujo de trabajo entre **GitHub**, **Google Colab** y **Google Drive**.

Durante la práctica se utilizará este repositorio para:

- clonar un proyecto desde GitHub utilizando `git clone`;
- explorar su estructura de directorios desde Google Colab;
- utilizar archivos almacenados dentro del proyecto;
- importar funciones definidas en archivos `.py`;
- procesar una imagen desde un notebook;
- guardar resultados de manera persistente en Google Drive.

---

## 📁 Estructura del proyecto

```text
del-dataset-a-unet_colab-github/
│
├── data/
│   ├── images/
│   │   └── imagen.jpg
│   │
│   └── text/
│       └── mensaje.txt
│
├── src/
│   ├── text_utils.py
│   └── image_utils.py
│
└── README.md
```

### `data/`

Contiene los archivos utilizados como datos de entrada durante la práctica.

- **`data/images/`**: contiene la imagen que será cargada y procesada.
- **`data/text/`**: contiene un archivo de texto que será leído desde Python.

### `src/`

Contiene código Python reutilizable.

- **`text_utils.py`**: incluye funciones para trabajar con el archivo de texto.
- **`image_utils.py`**: incluye funciones para cargar y transformar la imagen.

Las funciones definidas en estos archivos podrán importarse y utilizarse desde un notebook.

---

## 🔄 Flujo de trabajo

Durante la práctica se seguirá el siguiente flujo:

```text
GitHub
   │
   │ git clone
   ▼
Google Colab
   │
   ├── explorar el proyecto
   ├── leer datos
   ├── importar código desde src/
   └── procesar la imagen
             │
             ▼
        Google Drive
     guardar resultados
```

En este flujo:

- **GitHub** almacena y distribuye el código y los archivos del proyecto.
- **Google Colab** proporciona el entorno temporal donde se ejecutará el código.
- **Google Drive** proporciona almacenamiento persistente para los resultados que se deseen conservar.

> **Importante:** los archivos almacenados únicamente en el runtime de Google Colab son temporales y pueden desaparecer cuando termina la sesión. Los resultados que deban conservarse se guardarán en Google Drive.

---

## 🧰 Herramientas utilizadas

- Git
- GitHub
- Google Colab
- Google Drive
- Python
- `pathlib`
- Pillow (`PIL`)

---

## 🎯 Objetivo de la práctica

Al finalizar esta práctica se habrá recorrido un flujo básico que posteriormente se utilizará en proyectos de procesamiento y segmentación de imágenes:

```text
obtener datos
     ↓
cargar datos
     ↓
procesarlos con Python
     ↓
visualizar resultados
     ↓
guardar resultados
```

Este mismo principio se extenderá posteriormente al entrenamiento y evaluación de modelos de **Deep Learning para segmentación de imágenes**.
