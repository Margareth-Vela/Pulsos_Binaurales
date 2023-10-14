# Código para el módulo generador de pulsos binaurales
Se encuentra el código para el módulo generador utilizado para el estudio del sueño y para el estudio de concentración y estado de ánimo.

Para utilizar el código exportador de pulsos binaurales se necesita la librería.
- AccelBrainBeat
- Pydub 

Además, se necesita descargar FFmpeg. 

Nota: la variable ruta utiliza la dirección en donde se encuentra instalado FFmpeg. 

## Archivos de audio
El archivo llamado "pista.wav" contiene la pista moduladora para la función generadora. Es necesario que este se encuentre dentro de la carpeta del código. 

Para utilizar la verificación de las frecuencias centrales es necesario que se encuentre dentro de la carpeta del código el archivo llamado "beat.wav" del pulso binaural que se quiere estudiar. Este se puede generar al momento de la exportación del audio del pulso binaural. 

## Código pulsos binaurales constantes
El código se encuentra dividido en tres secciones:
**1. Código principal, exportación del pulso binaural.** En esta rutina se exporta el pulso binaural a la carpeta donde se encuentra actualmente el código. Necesita que se indique la frecuencia del canal izquierdo, derecho y la duración del audio en minutos.

**2. Código secundario, reproducción del pulso binaural constante.** Para utilizar esta parte del código se necesita instalar la librería [threading](https://pypi.org/project/threaded/) con el fin de usar programación multihilo. Necesita que se indique la frecuencia del canal izquierdo y derecho.

**3. Extra, verificación de las frecuencias centrales.** En esta rutina se utilizan las librerías numpy, matplotlib y [scipy](https://scipy.org/install/). Se grafica la forma de onda y la transformada rápida de Fourier para observar las frecuencias centrales del pulso con y sin pista moduladora.

## Código pulsos binaurales rutina
El código consiste en la exportación de un ciclo del sueño a la vez, teniendo un total de cinco ciclos. Se debe especificar que ciclo se quiere exportar por medio de la variable "stage_durations". Cada ciclo se encuentra constituido por las etapas N1, N2, N3, N4 y REM. 
