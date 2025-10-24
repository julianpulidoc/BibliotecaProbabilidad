import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Datos de la tabla (P = probabilidad, x = valor)
datos = [
    (1/36, 2, 2, 3),
    (3/36, 3, 2, 3),
    (5/36, 4, 2, 5),
    (10/36, 5, 2, 6),
    (15/36, 6, 2, 7),
    (21/36, 7, 2, 8),
    (26/36, 8, 2, 9),
    (30/36, 9, 2, 10),
    (33/36, 10, 2, 11),
    (35/36, 11, 2, 12),
]

# Extraer valores
probabilidades = [d[0] for d in datos]
x_valores = [d[1] for d in datos]

# Añadir punto inicial en x=1 con P=0
x_valores_completos = [1] + x_valores + [12]
prob_acumulada = [0] + probabilidades + [1.0]

# Crear la figura
plt.figure(figsize=(12, 8))

# Crear gráfica escalonada (step plot)
# El parámetro 'post' hace que la línea vaya horizontal y luego suba
plt.step(x_valores_completos, prob_acumulada, where='post', 
         linewidth=2.5, color='darkred', label='F(x)')

# Añadir puntos en los cambios
for i in range(len(x_valores)):
    # Círculo lleno en el punto inicial de cada escalón
    plt.plot(x_valores[i], probabilidades[i], 'o', 
             color='darkred', markersize=8, markerfacecolor='darkred')
    
    # Círculo vacío en el punto final (excepto el último)
    if i < len(x_valores) - 1:
        plt.plot(x_valores[i+1], probabilidades[i], 'o', 
                 color='darkred', markersize=8, markerfacecolor='white',
                 markeredgewidth=2)

# Punto inicial
plt.plot(1, 0, 'o', color='darkred', markersize=8, markerfacecolor='darkred')
plt.plot(2, 0, 'o', color='darkred', markersize=8, markerfacecolor='white', markeredgewidth=2)

# Configurar ejes
plt.xlim(0, 13)
plt.ylim(-0.05, 1.05)
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('P(X ≤ x)', fontsize=14, fontweight='bold')
plt.title('Función de Distribución Acumulativa (CDF)', 
          fontsize=16, fontweight='bold', pad=20)

# Grid
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)

# Etiquetas en el eje x
plt.xticks(range(1, 13))

# Etiquetas en el eje y con fracciones
y_ticks = [0, 1/36, 3/36, 5/36, 10/36, 15/36, 21/36, 26/36, 30/36, 33/36, 35/36, 1.0]
y_labels = ['0', '1/36', '3/36', '5/36', '10/36', '15/36', 
            '21/36', '26/36', '30/36', '33/36', '35/36', '1']
plt.yticks(y_ticks, y_labels, fontsize=10)

# Alternativamente, mostrar como decimales
# plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.legend(fontsize=12, loc='lower right')
plt.tight_layout()
plt.savefig('funcion_acumulativa_t2.png', dpi=300, bbox_inches='tight')
plt.show()

# Crear también tabla de datos
print("\n" + "="*60)
print("TABLA DE FUNCIÓN DE DISTRIBUCIÓN ACUMULATIVA")
print("="*60)
df = pd.DataFrame({
    'x': x_valores,
    'P(X ≤ x)': [f"{int(p*36)}/36" for p in probabilidades],
    'Decimal': [f"{p:.4f}" for p in probabilidades],
    'Porcentaje': [f"{p*100:.2f}%" for p in probabilidades]
})
print(df.to_string(index=False))
print("="*60)

# Estadísticas adicionales
print("\n" + "="*60)
print("ESTADÍSTICAS")
print("="*60)

# Calcular probabilidades individuales (PMF)
pmf = [probabilidades[0]] + [probabilidades[i] - probabilidades[i-1] 
                              for i in range(1, len(probabilidades))]

# Valor esperado (media)
media = sum(x * p for x, p in zip(x_valores, pmf))
print(f"Valor Esperado E(X): {media:.4f}")

# Varianza
varianza = sum(((x - media)**2) * p for x, p in zip(x_valores, pmf))
print(f"Varianza Var(X): {varianza:.4f}")

# Desviación estándar
desv_std = np.sqrt(varianza)
print(f"Desviación Estándar σ: {desv_std:.4f}")

# Mediana
mediana_idx = np.argmax(np.array(probabilidades) >= 0.5)
print(f"Mediana: {x_valores[mediana_idx]}")

print("="*60)

# Crear también la función de masa de probabilidad (PMF)
plt.figure(figsize=(12, 6))

plt.bar(x_valores, pmf, width=0.6, alpha=0.7, 
        color='steelblue', edgecolor='black', linewidth=1.5)

for i, (x, p) in enumerate(zip(x_valores, pmf)):
    plt.text(x, p + 0.01, f'{int(p*36)}/36', 
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('P(X = x)', fontsize=14, fontweight='bold')
plt.title('Función de Masa de Probabilidad (PMF)', 
          fontsize=16, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7, axis='y')
plt.xticks(range(2, 13))
plt.xlim(1, 13)
plt.tight_layout()
plt.savefig('funcion_masa_probabilidad_t2.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ Gráficas guardadas exitosamente:")
print("  - funcion_acumulativa_t2.png (CDF)")
print("  - funcion_masa_probabilidad_t2.png (PMF)")
