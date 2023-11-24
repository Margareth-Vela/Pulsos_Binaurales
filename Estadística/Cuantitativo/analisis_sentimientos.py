import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import seaborn as sns 
import matplotlib.pyplot as plt

# Configurar SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Configurar Traductor
translator = Translator()

#Leer archivo csv
df_es_sin_pulsos = pd.read_csv('comentariosSinPulsos.csv', encoding='utf-8')
df_es_con_pulsos = pd.read_csv('comentariosPulsos.csv', encoding='utf-8')

# Traducir los comentarios a inglés
df_es_sin_pulsos['comentario_ingles_aritmetica'] = df_es_sin_pulsos['comentario aritmetica'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_alegria'] = df_es_sin_pulsos['comentario alegria'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_tristeza'] = df_es_sin_pulsos['comentario tristeza'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_frustracion'] = df_es_sin_pulsos['comentario frustracion'].apply(lambda x: translator.translate(x, src='es', dest='en').text)

df_es_con_pulsos['comentario_ingles_aritmetica'] = df_es_con_pulsos['comentario aritmetica'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_alegria'] = df_es_con_pulsos['comentario alegria'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_tristeza'] = df_es_con_pulsos['comentario tristeza'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_frustracion'] = df_es_con_pulsos['comentario frustracion'].apply(lambda x: translator.translate(x, src='es', dest='en').text)


# Realizar el análisis de sentimientos para comentarios en inglés
df_es_sin_pulsos['polaridad_aritmetica'] = df_es_sin_pulsos['comentario_ingles_aritmetica'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_alegria'] = df_es_sin_pulsos['comentario_ingles_alegria'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_tristeza'] = df_es_sin_pulsos['comentario_ingles_tristeza'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_frustracion'] = df_es_sin_pulsos['comentario_ingles_frustracion'].apply(lambda x: sia.polarity_scores(x)['compound'])

df_es_con_pulsos['polaridad_aritmetica'] = df_es_con_pulsos['comentario_ingles_aritmetica'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_alegria'] = df_es_con_pulsos['comentario_ingles_alegria'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_tristeza'] = df_es_con_pulsos['comentario_ingles_tristeza'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_frustracion'] = df_es_con_pulsos['comentario_ingles_frustracion'].apply(lambda x: sia.polarity_scores(x)['compound'])


# Imprimir estadísticas
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Sin Pulsos")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

print("Análisis de Sentimientos Pruebas Aritméticas:")
print("Máximo valor:", df_es_sin_pulsos['polaridad_aritmetica'].max())
print("Mínimo valor:", df_es_sin_pulsos['polaridad_aritmetica'].min())
print("Valor medio:", df_es_sin_pulsos['polaridad_aritmetica'].mean())

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Alegría):")
print("Máximo valor:", df_es_sin_pulsos['polaridad_alegria'].max())
print("Mínimo valor:", df_es_sin_pulsos['polaridad_alegria'].min())
print("Valor medio:", df_es_sin_pulsos['polaridad_alegria'].mean())

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Tristeza):")
print("Máximo valor:", df_es_sin_pulsos['polaridad_tristeza'].max())
print("Mínimo valor:", df_es_sin_pulsos['polaridad_tristeza'].min())
print("Valor medio:", df_es_sin_pulsos['polaridad_tristeza'].mean())

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Frustración):")
print("Máximo valor:", df_es_sin_pulsos['polaridad_frustracion'].max())
print("Mínimo valor:", df_es_sin_pulsos['polaridad_frustracion'].min())
print("Valor medio:", df_es_sin_pulsos['polaridad_frustracion'].mean())

print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Con Pulsos")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Pruebas Aritméticas:")
print("Máximo valor:", df_es_con_pulsos['polaridad_aritmetica'].max())
print("Mínimo valor:", df_es_con_pulsos['polaridad_aritmetica'].min())
print("Valor medio:", df_es_con_pulsos['polaridad_aritmetica'].mean())

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Alegría):")
print("Máximo valor:", df_es_con_pulsos['polaridad_alegria'].max())
print("Mínimo valor:", df_es_con_pulsos['polaridad_alegria'].min())
print("Valor medio:", df_es_con_pulsos['polaridad_alegria'].mean())

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Tristeza):")
print("Máximo valor:", df_es_con_pulsos['polaridad_tristeza'].max())
print("Mínimo valor:", df_es_con_pulsos['polaridad_tristeza'].min())
print("Valor medio:", df_es_con_pulsos['polaridad_tristeza'].mean())

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Frustración):")
print("Máximo valor:", df_es_con_pulsos['polaridad_frustracion'].max())
print("Mínimo valor:", df_es_con_pulsos['polaridad_frustracion'].min())
print("Valor medio:", df_es_con_pulsos['polaridad_frustracion'].mean())
# Visualizar distribución de sentimientos
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_aritmetica'], color='green', kde=True, ax=axes[0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas aritméticas', weight='bold')

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_aritmetica'], color='green', kde=True, ax=axes[1])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas aritméticas', weight='bold')

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar la figura
#plt.show()

# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_alegria'], color='green', kde=True, ax=axes[0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo (alegría)', weight='bold')

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_alegria'], color='green', kde=True, ax=axes[1])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo (alegría)', weight='bold')

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar la figura
#plt.show()

# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_tristeza'], color='green', kde=True, ax=axes[0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo (tristeza)', weight='bold')

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_tristeza'], color='green', kde=True, ax=axes[1])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo (tristeza)', weight='bold')

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar la figura
#plt.show()

# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_frustracion'], color='green', kde=True, ax=axes[0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo (frustración)', weight='bold')

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_frustracion'], color='green', kde=True, ax=axes[1])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo (frustración)', weight='bold')

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar la figura
plt.show()