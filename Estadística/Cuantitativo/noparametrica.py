from scipy.stats import wilcoxon

# Supongamos que tienes dos conjuntos de datos: datos_con_pulsos y datos_sin_pulsos
datos_con_pulsos = [0.99, 0.99, 0.99, 0.96, 0.99, 1, 1]
datos_sin_pulsos = [0.99, 0.81, 0.98, 0.97, 0.98, 0.99, 0.99]

# Supongamos que tienes un DataFrame llamado 'df' con las columnas 'ConPulsos' y 'SinPulsos'
stat, p_value = wilcoxon(datos_con_pulsos, datos_sin_pulsos)

print(f"Estadístico de la prueba de Wilcoxon: {stat}")
print(f"Valor p: {p_value}")

# Interpretación del resultado
if p_value < 0.05:
    print("Se rechaza la hipótesis nula. Hay evidencia de una diferencia significativa.")
else:
    print("No se puede rechazar la hipótesis nula. No hay evidencia suficiente de una diferencia significativa.")
