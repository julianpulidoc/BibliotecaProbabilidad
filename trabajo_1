import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Crear el grafo dirigido
G = nx.DiGraph()

# Definir los nodos y sus conexiones con probabilidades
# Formato: (nodo_origen, nodo_destino, probabilidad)
edges = [
    # Desde INICIO
    ('INICIO', 'I1', 0.35),
    ('INICIO', 'S1', 0.15),
    ('INICIO', 'E1', 0.5),
    
    # Desde I1
    ('I1', 'I11', 0.45),
    ('I1', 'I12', 0.15),
    ('I1', 'IE2', 0.25),
    ('I1', 'IE3', 0.15),
    
    # Desde I11
    ('I11', 'I5', 0.40),
    ('I11', 'IE', 0.45),
    ('I11', 'ISI', 0.15),
    
    # Desde I12
    ('I12', 'I5', 0.40),
    ('I12', 'IE', 0.10),
    
    # Desde I5
    ('I5', 'IE', 0.45),
    ('I5', 'ISE', 0.40),
    
    # Desde IE
    ('IE', 'ISE', 0.45),
    ('IE', 'IEE', 0.45),
    
    # Desde IE2
    ('IE2', 'IEE', 0.45),
    ('IE2', 'IEL', 0.15),
    
    # Desde IE3
    ('IE3', 'SEE', 0.40),
    ('IE3', 'IEL', 0.40),
    
    # Desde IEL
    ('IEL', 'SEE', 0.40),
    ('IEL', 'SEL', 0.40),
    
    # Desde S1
    ('S1', 'SE1', 0.45),
    ('S1', 'SI1', 0.15),
    ('S1', 'EE1', 0.40),
    
    # Desde SE1
    ('SE1', 'SSI', 0.45),
    ('SE1', 'SSE', 0.40),
    
    # Desde SI1
    ('SI1', 'SII', 0.40),
    
    # Desde SSI
    ('SSI', 'SSE', 0.40),
    ('SSI', 'SIS', 0.40),
    
    # Desde SSE
    ('SSE', 'SEL', 0.15),
    ('SSE', 'SII', 0.40),
    
    # Desde E1
    ('E1', 'EE2', 0.45),
    ('E1', 'ES1', 0.15),
    ('E1', 'EI2', 0.40),
    
    # Desde EE2
    ('EE2', 'EEE', 0.40),
    ('EE2', 'EEI', 0.40),
    
    # Desde EEE
    ('EEE', 'SIE', 0.45),
    ('EEE', 'SIS', 0.40),
    
    # Desde ES1
    ('ES1', 'ESI', 0.45),
    ('ES1', 'EII', 0.40),
    
    # Desde EI2
    ('EI2', 'EII', 0.40),
    ('EI2', 'EIE', 0.40),
]

# Añadir las aristas con sus pesos (probabilidades)
for origen, destino, prob in edges:
    G.add_edge(origen, destino, weight=prob)

# Crear posiciones jerárquicas manualmente para mejor visualización
pos = {}

# Nivel 0 - INICIO
pos['INICIO'] = (0, 5)

# Nivel 1
pos['I1'] = (-2, 4)
pos['S1'] = (0, 4)
pos['E1'] = (2, 4)

# Nivel 2 - rama I1
pos['I11'] = (-3, 3)
pos['I12'] = (-2.5, 3)
pos['IE2'] = (-2, 3)
pos['IE3'] = (-1.5, 3)

# Nivel 2 - rama S1
pos['SE1'] = (-0.5, 3)
pos['SI1'] = (0, 3)
pos['EE1'] = (0.5, 3)

# Nivel 2 - rama E1
pos['EE2'] = (1.5, 3)
pos['ES1'] = (2, 3)
pos['EI2'] = (2.5, 3)

# Nivel 3
pos['I5'] = (-3.5, 2)
pos['IE'] = (-3, 2)
pos['ISI'] = (-2.5, 2)
pos['IEE'] = (-2, 2)
pos['IEL'] = (-1.5, 2)

pos['SSI'] = (-1, 2)
pos['SSE'] = (-0.5, 2)
pos['SII'] = (0, 2)

pos['EEE'] = (1.5, 2)
pos['EEI'] = (2, 2)
pos['ESI'] = (2.5, 2)
pos['EII'] = (3, 2)
pos['EIE'] = (3.5, 2)

# Nivel 4 (nodos finales)
pos['ISE'] = (-3.5, 1)
pos['SEE'] = (-2, 1)
pos['SEL'] = (-0.5, 1)
pos['SIS'] = (0.5, 1)
pos['SIE'] = (2, 1)

# Nivel 5 (nodos muy finales)
pos['SIT'] = (0, 0)
pos['SIE'] = (2, 0.5)

# Crear la figura
plt.figure(figsize=(18, 12))

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightcoral', 
                       node_size=1200, alpha=0.9, 
                       edgecolors='black', linewidths=2)

# Dibujar el nodo INICIO con color diferente
nx.draw_networkx_nodes(G, pos, nodelist=['INICIO'], 
                       node_color='lightgreen', 
                       node_size=1500, alpha=0.9,
                       edgecolors='black', linewidths=2)

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, edge_color='brown', 
                       width=2, alpha=0.6,
                       arrows=True, arrowsize=15,
                       arrowstyle='->', connectionstyle='arc3,rad=0.1')

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=9, 
                        font_weight='bold', font_color='black')

# Dibujar las probabilidades en las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
# Ajustar posiciones de las etiquetas para que no se superpongan
nx.draw_networkx_edge_labels(G, pos, edge_labels, 
                              font_size=7, font_color='blue',
                              bbox=dict(boxstyle='round,pad=0.3', 
                                       facecolor='white', alpha=0.7))

plt.title('Diagrama de Árbol - Trabajo 1', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig('diagrama_arbol_t1.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

# Imprimir información del grafo
print(f"Número total de nodos: {G.number_of_nodes()}")
print(f"Número total de aristas: {G.number_of_edges()}")
print(f"\nNodos: {list(G.nodes())}")
print(f"\nCaminos desde INICIO:")

# Encontrar todos los nodos finales (sin sucesores)
nodos_finales = [n for n in G.nodes() if G.out_degree(n) == 0]
print(f"\nNodos finales (hojas): {nodos_finales}")

# Calcular algunas rutas de ejemplo
if 'INICIO' in G.nodes():
    for nodo_final in nodos_finales[:5]:  # Mostrar solo 5 ejemplos
        try:
            camino = nx.shortest_path(G, 'INICIO', nodo_final)
            prob_total = 1.0
            for i in range(len(camino)-1):
                prob_total *= G[camino[i]][camino[i+1]]['weight']
            print(f"\nCamino a {nodo_final}: {' → '.join(camino)}")
            print(f"  Probabilidad total: {prob_total:.4f}")
        except nx.NetworkXNoPath:
            pass
