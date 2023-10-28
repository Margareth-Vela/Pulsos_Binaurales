# Pulsos Binaurales
Repositorio de trabajo de graduación "Análisis cualitativo y cuantitativo del impacto de los pulsos binaurales en el estado de ánimo, concentración y calidad del sueño de las personas"

Este trabajo se centró en llevar a cabo un análisis estadístico para discernir el impacto de los pulsos binaurales en el estado de ánimo, concentración y calidad del sueño de las personas. Se mejoró un módulo generador de pulsos binaurales desarrollado en años anteriores, adaptándolo a las especificaciones de cada estudio. Asimismo, se realizó un protocolo de investigación y consentimiento informado específico para cada estudio.
El análisis cualitativo se apoyó en cuestionarios completados por los sujetos antes y después de las pruebas experimentales, tanto con la presencia como en la ausencia de pulsos binaurales. Paralelamente, el análisis cuantitativo consistió en la recopilación de resultados de pruebas de concentración y comentarios proporcionados por los sujetos. 

## Índice 
1. [Prerequisitos](#prerequisitos)
    - [Librería AccelBrainBeat](#librería-accelbrainbeat)
    - [Librería pydub](#librería-pydub)
    - [Framework FFmpeg](#framework-ffmpeg)
2. [Estructura de carpetas](#estructura-de-carpetas)

## Pruebas experimentales
### Pruebas de concentración 
Se estructuró el estudio para tener tres pruebas de concentración como distintos métodos de validación. Para la primera se utilizó la página web: [olimato.it](https://olimato.it/mat/). El sujeto de prueba debe realizar de manera mental la operación que se le presente en la pantalla, conforme va avanzando las operaciones son más complicadas. Cabe resaltar que los sujetos de prueba realizan la prueba tanto sin pulsos como con pulsos binaurales para poder tener datos de control y realizar la comparación. La página web presenta tres niveles de dificultad posibles: fácil, medio y difícil. Para este estudio se decidió utilizar el nivel medio debido a que se quería que el sujeto de prueba se concentrara lo más posible y pudiera avanzar en cada operación aritmética en un tiempo moderado. 

[logo]: https://github.com/Margareth-Vela/Pulsos_Binaurales/blob/main/Im%C3%A1genes/testaritmetico.png "Prueba aritmética"

## Prerequisitos
### Librería AccelBrainBeat
Instalar la librería por medio de pip como se menciona en el siguiente enlace: https://pypi.org/project/AccelBrainBeat/
Documentación de la librería en el siguiente enlace: https://code.accel-brain.com/Binaural-Beat-and-Monaural-Beat-with-python/

### Librería pydub
Instalar la librería por medio de pip como se menciona en el siguiente enlace: https://pypi.org/project/pydub/ 
Documentación de la librería en el siguiente enlace: https://github.com/jiaaro/pydub/blob/master/API.markdown

### Framework FFmpeg
Descargar el framework en el siguiente enlace: https://ffmpeg.org/download.html 
   
## Estructura de carpetas
**1. Código**
   - Pulsos binaurales constantes: código para el generador de pulsos binaurales del estudio de concentración y estado de ánimo.
   - Pulsos binaurales rutina: código para el generador de pulsos binaurales del estudio del sueño.
     
**2. Documentos protocolarios y manuales**
   - Consentimiento informado
      - Consentimiento para el estudio de concentración y estado de ánimo
      - Consentimiento para el estudio del sueño
   - Protocolo de investigación
   - Manual de usuario para la conexión entre la Cyton Board y el Electro-Cap desde OpenBCI
     
**3. Estadística**
   - Carpeta de análisis cualitativo
   - Carpeta de análisis cuantitativo
     
**4. Audios**
   - Enlaces de descarga para los audios de pulsos binaurales del ciclo del sueño y ejemplos de pulsos binaurales del estudio de concentración y estado de ánimo. 

 
