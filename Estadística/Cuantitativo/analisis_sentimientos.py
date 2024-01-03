import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import seaborn as sns 
import matplotlib.pyplot as plt

def get_polaridad_porcentaje(df):
    # Obtener los valores de polaridad positiva, negativa y neutra
    polaridad_positiva = df > 0
    polaridad_negativa = df < 0
    polaridad_neutra = df == 0

    # Calcular el número de observaciones para cada tipo de polaridad
    numero_polaridad_positiva = polaridad_positiva.sum()
    numero_polaridad_negativa = polaridad_negativa.sum()
    numero_polaridad_neutra = polaridad_neutra.sum()

    # Calcular el porcentaje de cada tipo de polaridad
    porcentaje_polaridad_positiva = numero_polaridad_positiva / len(df) * 100
    porcentaje_polaridad_negativa = numero_polaridad_negativa / len(df) * 100
    porcentaje_polaridad_neutra = numero_polaridad_neutra / len(df) * 100

    # Devolver un diccionario con los porcentajes
    return {
        'positiva': porcentaje_polaridad_positiva,
        'negativa': porcentaje_polaridad_negativa,
        'neutra': porcentaje_polaridad_neutra
    }


# Configurar SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Configurar Traductor
translator = Translator()

#Leer archivos csv
df_es_sin_pulsos = pd.read_csv('comentariosSinPulsos.csv', encoding='utf-8')
df_es_con_pulsos = pd.read_csv('comentariosPulsos.csv', encoding='utf-8')
df_es_sueño = pd.read_csv('comentariosSueño.csv', encoding='utf-8')

# Traducir los comentarios a inglés
df_es_sin_pulsos['comentario_ingles_conc_sin_ruido_rosa'] = df_es_sin_pulsos['comentario concentracion sin ruido'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_conc_con_ruido_rosa'] = df_es_sin_pulsos['comentario concentracion ruido rosa'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_est_sin_ruido_rosa'] = df_es_sin_pulsos['comentario estado sin ruido'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_est_con_ruido_rosa'] = df_es_sin_pulsos['comentario estado ruido rosa'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_alegria'] = df_es_sin_pulsos['comentario alegria'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_tristeza'] = df_es_sin_pulsos['comentario tristeza'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_sin_pulsos['comentario_ingles_frustracion'] = df_es_sin_pulsos['comentario frustracion'].apply(lambda x: translator.translate(x, src='es', dest='en').text)

df_es_con_pulsos['comentario_ingles_conc_sin_ruido_rosa'] = df_es_con_pulsos['comentario concentracion sin ruido'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_conc_con_ruido_rosa'] = df_es_con_pulsos['comentario concentracion ruido rosa'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_est_sin_ruido_rosa'] = df_es_con_pulsos['comentario estado sin ruido'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_est_con_ruido_rosa'] = df_es_con_pulsos['comentario estado ruido rosa'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_alegria'] = df_es_con_pulsos['comentario alegria'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_tristeza'] = df_es_con_pulsos['comentario tristeza'].apply(lambda x: translator.translate(x, src='es', dest='en').text)
df_es_con_pulsos['comentario_ingles_frustracion'] = df_es_con_pulsos['comentario frustracion'].apply(lambda x: translator.translate(x, src='es', dest='en').text)

df_es_sueño['comentario_ingles_sueño'] = df_es_sueño['comentario'].apply(lambda x: translator.translate(x, src='es', dest='en').text)

# Realizar el análisis de sentimientos para comentarios en inglés
df_es_sin_pulsos['polaridad_conc_sin_ruido_rosa'] = df_es_sin_pulsos['comentario_ingles_conc_sin_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_conc_con_ruido_rosa'] = df_es_sin_pulsos['comentario_ingles_conc_con_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_est_sin_ruido_rosa'] = df_es_sin_pulsos['comentario_ingles_est_sin_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_est_con_ruido_rosa'] = df_es_sin_pulsos['comentario_ingles_est_con_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_alegria'] = df_es_sin_pulsos['comentario_ingles_alegria'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_tristeza'] = df_es_sin_pulsos['comentario_ingles_tristeza'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_sin_pulsos['polaridad_frustracion'] = df_es_sin_pulsos['comentario_ingles_frustracion'].apply(lambda x: sia.polarity_scores(x)['compound'])

df_es_con_pulsos['polaridad_conc_sin_ruido_rosa'] = df_es_con_pulsos['comentario_ingles_conc_sin_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_conc_con_ruido_rosa'] = df_es_con_pulsos['comentario_ingles_conc_con_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_est_sin_ruido_rosa'] = df_es_con_pulsos['comentario_ingles_est_sin_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_est_con_ruido_rosa'] = df_es_con_pulsos['comentario_ingles_est_con_ruido_rosa'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_alegria'] = df_es_con_pulsos['comentario_ingles_alegria'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_tristeza'] = df_es_con_pulsos['comentario_ingles_tristeza'].apply(lambda x: sia.polarity_scores(x)['compound'])
df_es_con_pulsos['polaridad_frustracion'] = df_es_con_pulsos['comentario_ingles_frustracion'].apply(lambda x: sia.polarity_scores(x)['compound'])

df_es_sueño['polaridad_sueño'] = df_es_sueño['comentario_ingles_sueño'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Imprimir estadísticas
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Sin Pulsos")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

print("Análisis de Sentimientos Pruebas de Concentración sin ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_conc_sin_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])


print("Análisis de Sentimientos Pruebas de Concentración con ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_conc_con_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de ánimo sin ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_est_sin_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de ánimo con ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_est_con_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Alegría):")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_alegria'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Tristeza):")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_tristeza'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Frustración):")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sin_pulsos['polaridad_frustracion'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Con Pulsos")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Pruebas de Concentración sin ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_conc_sin_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Concentración con ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_conc_con_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de ánimo sin ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_est_sin_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de ánimo con ruido rosa:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_est_con_ruido_rosa'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Alegría):")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_alegria'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Tristeza):")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_tristeza'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("Análisis de Sentimientos Pruebas de Estado de Ánimo (Frustración):")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_con_pulsos['polaridad_frustracion'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])

print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("Análisis de Sentimientos Estudio del Sueño")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

print("Análisis de Sentimientos Estudio del Sueño:")
polaridad_porcentaje = get_polaridad_porcentaje(df_es_sueño['polaridad_sueño'])
print("Porcentaje positivo:",polaridad_porcentaje['positiva'])
print("Porcentaje positivo:",polaridad_porcentaje['negativa'])
print("Porcentaje positivo:",polaridad_porcentaje['neutra'])


#-----------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas de Concentración sin Ruido Rosa
#-----------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923, bottom=0.116, left=0.057, right=0.941, hspace=0.18, wspace=0.302)

# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_conc_sin_ruido_rosa'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de concentración', weight='bold', loc="center", multialignment="center")

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_conc_sin_ruido_rosa'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de concentración', weight='bold', loc="center", multialignment="center")

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas de Concentración con Ruido Rosa
#---------------------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923, bottom=0.116, left=0.057, right=0.941, hspace=0.18, wspace=0.302)

# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_conc_con_ruido_rosa'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de concentración', weight='bold', loc="center", multialignment="center")

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_conc_con_ruido_rosa'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de concentración', weight='bold', loc="center", multialignment="center")

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas Estado de Ánimo sin Ruido Rosa
#---------------------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923, bottom=0.116, left=0.057, right=0.941, hspace=0.18, wspace=0.302)
# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_est_sin_ruido_rosa'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo', weight='bold', loc="center", multialignment="center")

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_est_sin_ruido_rosa'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo', weight='bold', loc="center", multialignment="center")

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas de Estado de Ánimo con Ruido Rosa
#---------------------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923, bottom=0.116, left=0.057, right=0.941, hspace=0.18, wspace=0.302)


# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_est_con_ruido_rosa'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo', weight='bold', loc="center", multialignment="center")

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_est_con_ruido_rosa'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo', weight='bold', loc="center", multialignment="center")

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas Estado de Ánimo: Alegría
#---------------------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923,
bottom=0.132,
left=0.056,
right=0.949,
hspace=0.18,
wspace=0.272)
# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_alegria'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo (alegría)', weight='bold', loc="center", multialignment="center", fontsize=11.5)

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_alegria'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo (alegría)', weight='bold', loc="center", multialignment="center", fontsize=11.5)

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas Estado de Ánimo: Tristeza
#---------------------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923,
bottom=0.132,
left=0.057,
right=0.964,
hspace=0.18,
wspace=0.229)
# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_tristeza'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo (tristeza)', weight='bold', loc="center", multialignment="center", fontsize=11.5)

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_tristeza'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo (tristeza)', weight='bold', loc="center", multialignment="center", fontsize=11.5)

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Pruebas Estado de Ánimo: Frustración
#---------------------------------------------------------------------------
# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Crear una figura y ejes con dos subgráficos en una fila
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.subplots_adjust(top=0.923,
bottom=0.132,
left=0.052,
right=0.949,
hspace=0.18,
wspace=0.269)
# Graficar la primera distribución
sns.distplot(df_es_sin_pulsos['polaridad_frustracion'], color='green', kde=True, ax=axes[0]).set_xlim([-1.0, 1.0])
axes[0].set(xlabel='Polaridad General', ylabel='Densidad')
axes[0].set_title('Polaridad sin pulsos binaurales para pruebas de estado de ánimo (frustración)', loc="center", multialignment="center", weight='bold', fontsize=11.5)

# Graficar la segunda distribución
sns.distplot(df_es_con_pulsos['polaridad_frustracion'], color='green', kde=True, ax=axes[1]).set_xlim([-1.0, 1.0])
axes[1].set(xlabel='Polaridad General', ylabel='Densidad')
axes[1].set_title('Polaridad con pulsos binaurales para pruebas de estado de ánimo (frustración)', weight='bold', loc="center", multialignment="center", fontsize=11.5)

# Ajustar el espacio entre subgráficos
plt.tight_layout()

#---------------------------------------------------------------------------
# Visualizar distribución de sentimientos Estudio del Sueño
#---------------------------------------------------------------------------
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.distplot(df_es_sueño['polaridad_sueño'], color='green', kde=True)
ax.set(xlabel='Polaridad General', ylabel='Densidad')
ax.set_title('Polaridad de los comentarios del estudio del sueño',weight='bold', loc="center", multialignment="center")
ax.set_xlim([-1.0, 1.0])

# Mostrar la figura
plt.show()