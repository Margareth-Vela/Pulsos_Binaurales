# Análisis cuantitativo

Se encuentra las distintas rutinas que se utilizaron para el análisis cuantitativo desde las herramientas usadas en Excel, hasta los programas realizados en Python. 

## Prueba t de Student
Para la prueba se utiliza el análisis de datos de Excel usando la opción de prueba t para muestras dependientes con un &alpha; de 0.05.

## Análisis de sentimientos
El código para el análisis de sentimientos de los comentarios tanto antes como después del uso de pulsos binaurales se encuentra en "analisis_sentimientos.py". 
Este utiliza las librerías [pandas](https://pandas.pydata.org/), [nltk](https://www.nltk.org/install.html),
[seaborn](https://pypi.org/project/seaborn/), y matplotlib. Además, se utiliza la librería [googletrans](https://pypi.org/project/googletrans/) 
para poder traducir los comentarios de español a inglés para que puedan ser interpretados correctamente en el análisis.
Este utiliza el archivo "comentarios.csv" en codificación utf-8 para obtener los comentarios realizados por los sujetos de prueba antes de 
usar pulsos binaurales. Además, utiliza el archivo "comentariosPulsos.csv" en codificación utf-8 para obtener los comentarios realizados por los sujetos de prueba después de usar pulsos binaurales. 

## Prueba de Wilcoxon
Para la prueba de Wilcoxon se utilizó la librería [scipy](https://scipy.org/install/). Se utilizan los conjuntos de datos
datos_con_pulsos y datos_sin_pulsos para poder realizar la comparación. La prueba determina el resultado por el p_Valor. 
