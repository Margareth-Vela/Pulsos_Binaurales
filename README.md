# Pulsos Binaurales
Repositorio de trabajo de graduación "Análisis cualitativo y cuantitativo del impacto de los pulsos binaurales en el estado de ánimo, concentración y calidad del sueño de las personas"

Este trabajo se centró en llevar a cabo un análisis estadístico para discernir el impacto de los pulsos binaurales en el estado de ánimo, concentración y calidad del sueño de las personas. Se mejoró un módulo generador de pulsos binaurales desarrollado en años anteriores, adaptándolo a las especificaciones de cada estudio. Asimismo, se realizó un protocolo de investigación y consentimiento informado específico para cada estudio.
El análisis cualitativo se apoyó en cuestionarios completados por los sujetos antes y después de las pruebas experimentales, tanto con la presencia como en la ausencia de pulsos binaurales. Paralelamente, el análisis cuantitativo consistió en la recopilación de resultados de pruebas de concentración y comentarios proporcionados por los sujetos. 

## Índice 
1. [Pruebas experimentales](#pruebas-experimentales)
    - [Pruebas de concentración](#pruebas-de-concentración)
    - [Pruebas de estado de ánimo](#pruebas-de-estado-de-ánimo)
    - [Pruebas de sueño](#pruebas-de-sueño)
1. [Prerequisitos](#prerequisitos)
    - [Librería AccelBrainBeat](#librería-accelbrainbeat)
    - [Librería pydub](#librería-pydub)
    - [Framework FFmpeg](#framework-ffmpeg)
2. [Estructura de carpetas](#estructura-de-carpetas)

## Pruebas experimentales
### Pruebas de concentración 
Se estructuró el estudio para tener tres pruebas de concentración como distintos métodos de validación. Para la primera se utilizó la página web: [olimato.it](https://olimato.it/mat/). El sujeto de prueba debe realizar de manera mental la operación que se le presente en la pantalla, conforme va avanzando las operaciones son más complicadas. Cabe resaltar que los sujetos de prueba realizan la prueba tanto sin pulsos como con pulsos binaurales para poder tener datos de control y realizar la comparación. La página web presenta tres niveles de dificultad posibles: fácil, medio y difícil. Para este estudio se decidió utilizar el nivel medio debido a que se quería que el sujeto de prueba se concentrara lo más posible y pudiera avanzar en cada operación aritmética en un tiempo moderado. 

<p align="center">
<img src="https://github.com/Margareth-Vela/Pulsos_Binaurales/blob/main/Im%C3%A1genes/testaritmetico.png" alt="Prueba aritmética" width="400px">
</p>

La segunda prueba realizada es la prueba de Toulouse-Pieron que se encuentra en la página web [metodorf.com](https://metodorf.com/tests/bourdon/tuluz_peron.php), la cual consiste en identificar tres figuras a lo largo de una serie de elementos durante quince minutos. Cabe destacar que la prueba va mostrando línea por línea teniendo treinta segundos para identificar las figuras iguales seleccionando el cuadro superior, mientras que las que no son iguales se subrayan (selección del cuadro inferior). Esta prueba permite evaluar las aptitudes perceptivas y atencionales de un individuo mayor de 17 años y se realiza de manera individual. 

<p align="center">
<img src="https://github.com/Margareth-Vela/Pulsos_Binaurales/blob/main/Im%C3%A1genes/tolouse_pieron_test.png" alt="Prueba aritmética" width="600px">
</p>

La tercera prueba consiste en 30 minutos realizando alguna actividad que requiera concentración como tareas o trabajo. Teniendo 15 minutos con ruido rosa y 15 minutos con ruido rosa mezclado con pulsos binaurales. Esto con el fin de poder mitigar el ruido externo y mantener las pruebas de concentración, lo más delimitadas posibles. 

### Pruebas de estado de ánimo
Las pruebas de estado de ánimo consistieron en la visualización de videos con el fin de obtener un dato de control de la percepción de la emoción y la lectura de cuentos cortos que presentara la misma emoción predominante que el video visto, pero aplicando pulsos binaurales para obtener el cambio en la percepción de la emoción. Para ello se realizó una colección de videos y cuentos cortos que se fueron variando según la emoción en cada sujeto de prueba para poder obtener mediciones lo más parciales posibles. 

La primer prueba es la visualización de videos que representen alguna emoción en particular, como alegría, tristeza, frustración, entre otros. Esta prueba dura entre 3-8 minutos. Se espera entre 15-20 minutos para que el sujeto de prueba regrese a una emoción neutral y poder obtener la medición con el cambio con pulsos binaurales. La segunda prueba es la lectura de cuentos cortos en los que predomine la misma emoción. Se pueden realizar varias pruebas de diversas emociones con el mismo sujeto de prueba pero se debe esperar la mayor cantidad posible de tiempo para permitir que este se encuentre en un estado neutral y no se tengan mediciones incorrectas. 

### Pruebas de sueño
La metodología consiste en la toma de datos de una noche en la cual no se reproducen los pulsos binaurales (datos de control), seguidas de dos noches en las que sí se reproducen los pulsos. Se realiza durante dos noches para reducir la posibilidad de factores externos que puedan afectar el resultado del impacto cualitativo del individuo, es decir, que por algún motivo externo al estudio pueda presentar relajación o mayor cansancio, lo que induzca a un sueño profundo sin la necesidad de utilizar los pulsos binaurales. 

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

 
