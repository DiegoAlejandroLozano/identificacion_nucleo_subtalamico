# Identificación Automática del Núcleo Subtalámico mediante Redes Neuronales Convolucionales

Este repositorio contiene el proyecto aplicado presentado como requisito para optar por el título de Magíster en Ciencia de Datos en la Pontificia Universidad Javeriana de Cali. El proyecto aborda el desarrollo de un sistema de inteligencia artificial basado en redes neuronales convolucionales (CNN) para la identificación automática del núcleo subtalámico (STN) a partir de señales de microelectrodos (MER), con el objetivo de asistir en procedimientos de estimulación cerebral profunda (DBS) en pacientes con Parkinson.

## Enlace al repositorio

- [https://github.com/DiegoAlejandroLozano/identificacion_nucleo_subtalamico](https://github.com/DiegoAlejandroLozano/identificacion_nucleo_subtalamico)

## Autores

- **Diego Alejandro Lozano Millán**  
- **Andrés Parada Hernández**  
- **Christian Camilo Vega Preciado**  

**Director del proyecto:** Hernán Darío Vargas Cardona  

## Descripción del proyecto

La enfermedad de Parkinson (EP) es una patología neurodegenerativa que afecta la calidad de vida de millones de personas en todo el mundo. La estimulación cerebral profunda (DBS) ha emergido como una solución efectiva para pacientes en etapas avanzadas de la enfermedad. Este proyecto busca mejorar la precisión en la identificación del núcleo subtalámico (STN), una estructura crítica para el éxito del procedimiento, mediante el entrenamiento de modelos de redes neuronales convolucionales.

### Objetivo general

Desarrollar un sistema basado en CNN para identificar automáticamente el STN a partir de señales MER en el contexto de procedimientos DBS.

### Objetivos específicos

1. Preprocesar la base de datos de señales MER etiquetadas.
2. Entrenar y comparar diferentes arquitecturas de CNN para la identificación del STN.
3. Evaluar los modelos utilizando métricas estándar como Accuracy, Precision, Recall, F1-score y ROC-AUC.

## Metodología

El proyecto incluye las siguientes etapas principales:

1. **Preprocesamiento de datos:** Limpieza, segmentación y normalización de señales MER previamente etiquetadas.
2. **Desarrollo de modelos:** Entrenamiento de arquitecturas CNN 1D y 2D, incluyendo modelos con y sin transferencia de aprendizaje (VGG19 y ResNet50).
3. **Evaluación de resultados:** Uso de métricas de desempeño y análisis comparativo para seleccionar el modelo más adecuado.

## Resultados

Los modelos desarrollados lograron una precisión superior al 90% en la identificación del STN. Los modelos basados en transfer learning (VGG19 y ResNet50) mostraron un rendimiento superior en comparación con los modelos entrenados desde cero, destacándose en términos de precisión y sensibilidad.

## Archivos excluidos

Los siguientes archivos y directorios fueron excluidos del repositorio para reducir su tamaño o proteger datos sensibles:

- `venv/`: Entorno virtual de Python.
- `BD_original/`: Base de datos original con señales MER.
- `prueba/`: Directorio de pruebas internas.
- `BD_procesada/`: Base de datos procesada.
- `imagenes/`: Archivos de imágenes no relevantes para el repositorio público.
- `explicacion_datos.ipynb`: Notebook con información sensible o interna de los datos.
- `split_imagenes/`: Carpeta con partición de imágenes utilizada en experimentos.
- `**/modelo_generado/`: Modelos generados durante los experimentos.
- `**/repeticiones_experimento/`: Resultados de repeticiones de experimentos.

Si necesitas acceso a estos archivos, comunícate con los autores del proyecto.

## Requisitos del sistema

- Python 3.8 o superior.
- Librerías principales: TensorFlow, Keras, NumPy, Pandas, Matplotlib, Scikit-learn.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/DiegoAlejandroLozano/identificacion_nucleo_subtalamico.git
   cd identificacion_nucleo_subtalamico
