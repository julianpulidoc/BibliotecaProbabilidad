# -----------------------------------------------
# researchpy: summary_cont, ttest, anova (solo)
# -----------------------------------------------
# !pip install researchpy pandas scipy

import numpy as np
import pandas as pd
import researchpy as rp
import warnings

# 1) Silenciar FutureWarning que emite researchpy (no afecta resultados)
warnings.filterwarnings("ignore", category=FutureWarning, module="researchpy")

# 2) Datos simulados reproducibles
np.random.seed(42)
N = 120

# Opción A (aleatoria, puede quedar desbalanceado):
genero = np.random.choice(['Hombre', 'Mujer'], size=N)
# Opción B (descomenta si quieres 60/60 balanceado):
# genero = np.array(['Hombre']*(N//2) + ['Mujer']*(N//2))
# np.random.shuffle(genero)

seccion = np.random.choice(['A', 'B', 'C'], size=N, p=[0.35, 0.35, 0.30])

nota_base = np.random.normal(loc=70, scale=12, size=N)
ajuste_genero = np.where(genero == 'Mujer', 1.5, -1.0)  # solo para crear diferencias
ajuste_seccion = np.select(
    [seccion == 'A', seccion == 'B', seccion == 'C'],
    [ 2.0, 0.0, -1.5],
    default=0.0
)
nota = np.clip(nota_base + ajuste_genero + ajuste_seccion, 0, 100).round(1)

df = pd.DataFrame({'nota': nota, 'genero': genero, 'seccion': seccion})

print("Vista rápida de los datos:")
print(df.head(), "\n")

# 3) summary_cont(): descriptivas
print("1) Estadísticas descriptivas (general):")
desc_general = rp.summary_cont(df['nota']).round(4)
print(desc_general.reset_index(drop=True), "\n")

print("1b) Estadísticas descriptivas por género:")
desc_genero = rp.summary_cont(df['nota'].groupby(df['genero'])).round(4)
print(desc_genero.reset_index().rename(columns={'index': 'genero'}), "\n")

# 4) ttest(): Hombres vs Mujeres (Welch por robustez)
print("2) Prueba t (Welch) Hombres vs Mujeres:")
res_ttest, resumen_dos_grupos = rp.ttest(
    df.loc[df['genero'] == 'Hombre', 'nota'],
    df.loc[df['genero'] == 'Mujer',  'nota'],
    group1_name='Hombres',
    group2_name='Mujeres',
    equal_variances=False  # Welch
)
print("Resumen de ambos grupos:")
print(resumen_dos_grupos.round(4).reset_index(drop=True), "\n")
print("Resultados de la prueba t (Welch):")
print(res_ttest.round(4), "\n")

# 5) anova(): un factor (nota ~ seccion)
# ------------------------------------------------------
# ANOVA de 1 factor (nota ~ seccion)
# ------------------------------------------------------
print("3) ANOVA de 1 factor (nota ~ seccion):")
anova_model = rp.anova('nota ~ seccion', data=df)

# Algunas versiones devuelven tuple en .results(); otras devuelven algo ya tabular
try:
    res = anova_model.results()
except AttributeError:
    # En ciertas versiones, rp.anova ya es el tuple
    res = anova_model

# Desempaquetar de forma robusta
if isinstance(res, tuple) and len(res) >= 2:
    anova_meta, anova_tabla = res[0], res[1]  # anova_tabla es el DataFrame que queremos
else:
    # Si no es tuple, asumir que ya es DataFrame-like
    anova_tabla = res

# Redondear y ordenar columnas (solo si existen)
anova_tabla = anova_tabla.round(4)
cols_pref = ['Source', 'Sum of Squares', 'Degrees of Freedom',
             'Mean Squares', 'F value', 'p-value',
             'Eta squared', 'Epsilon squared', 'Omega squared']
anova_tabla = anova_tabla[[c for c in cols_pref if c in anova_tabla.columns]]

print(anova_tabla.to_string(index=False), "\n")
