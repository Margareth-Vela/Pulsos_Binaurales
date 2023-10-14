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
df_es = pd.read_csv('comentariosPulsos.csv', encoding='utf-8')

# Traducir los comentarios a inglés
df_es['comentario_ingles'] = df_es['comentario'].apply(lambda x: translator.translate(x, src='es', dest='en').text)

# Realizar el análisis de sentimientos para comentarios en inglés
df_es['polaridad'] = df_es['comentario_ingles'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Imprimir estadísticas
print("Análisis de Sentimientos:")
print("Máximo valor:", df_es['polaridad'].max())
print("Mínimo valor:", df_es['polaridad'].min())
print("Valor medio:", df_es['polaridad'].mean())

# Visualizar distribución de sentimientos
sns.set(style="whitegrid")
#plt.figure(figsize=(10, 6))
ax = sns.distplot(df_es['polaridad'], color='green', kde=True)
ax.set(xlabel='Polaridad General', ylabel='Densidad')
ax.set_title('Polaridad de los comentarios con pulsos binaurales',weight='bold')
plt.show()