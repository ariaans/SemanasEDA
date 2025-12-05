# -*- coding: utf-8 -*-
"""
Análisis de Grafos - Semana 3
Carga y analiza grafos desde archivos generados por C#
"""

from collections import defaultdict
from typing import Dict, List, Tuple
import os

def load_graph(file_path: str, is_directed: bool = True) -> Dict[str, List[Tuple[str, float]]]:
    """
    Carga un grafo desde un archivo de texto con manejo robusto de errores.
    
    Args:
        file_path: Ruta al archivo de aristas
        is_directed: True para grafo dirigido, False para no dirigido
    
    Returns:
        Diccionario con lista de adyacencia
    """
    adjacency_list = defaultdict(list)
    
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo '{file_path}' no existe.")
        return adjacency_list
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                # Ignorar líneas vacías y comentarios
                if not line or line.startswith('#'):
                    continue
                
                parts = line.split()
                if len(parts) < 2:
                    print(f"⚠️  Línea {line_num}: '{line}' ignorada (faltan vértices)")
                    continue
                
                from_vertex, to_vertex = parts[0], parts[1]
                
                # Procesar peso con validación
                try:
                    weight = float(parts[2]) if len(parts) > 2 else 1.0
                except (ValueError, IndexError):
                    print(f"⚠️  Línea {line_num}: peso inválido, usando 1.0")
                    weight = 1.0
                
                # Agregar arista
                adjacency_list[from_vertex].append((to_vertex, weight))
                
                # Si es no dirigido, agregar arista inversa
                if not is_directed:
                    adjacency_list[to_vertex].append((from_vertex, weight))
                    
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{file_path}'")
    except Exception as e:
        print(f"❌ Error inesperado al leer '{file_path}': {e}")
    
    return dict(adjacency_list)

def get_neighbors(graph: Dict[str, List[Tuple[str, float]]], vertex: str) -> List[Tuple[str, float]]:
    """Obtiene la lista de vecinos de un vértice."""
    return graph.get(vertex, [])

def has_edge(graph: Dict[str, List[Tuple[str, float]]], from_vertex: str, to_vertex: str) -> bool:
    """
    Verifica si existe una arista de from_vertex a to_vertex.
    """
    neighbors = graph.get(from_vertex, [])
    return any(neighbor == to_vertex for neighbor, _ in neighbors)

def get_out_degree(graph: Dict[str, List[Tuple[str, float]]], vertex: str) -> int:
    """Calcula el grado de salida de un vértice."""
    return len(graph.get(vertex, []))

def get_in_degree(graph: Dict[str, List[Tuple[str, float]]], vertex: str) -> int:
    """Calcula el grado de entrada de un vértice."""
    in_degree = 0
    for neighbors in graph.values():
        in_degree += sum(1 for neighbor, _ in neighbors if neighbor == vertex)
    return in_degree

def analyze_graph(graph: Dict[str, List[Tuple[str, float]]], graph_type: str):
    """Analiza y muestra estadísticas detalladas del grafo."""
    print(f"\n{'='*60}")
    print(f"🔍 Análisis del Grafo {graph_type}")
    print(f"{'='*60}")
    
    if not graph:
        print("⚠️  El grafo está vacío")
        return
    
    vertices = sorted(graph.keys())
    total_edges = sum(len(neighbors) for neighbors in graph.values())
    
    print(f"📊 Estadísticas generales:")
    print(f"   • Vértices: {len(vertices)}")
    print(f"   • Aristas: {total_edges}")
    
    # Calcular densidad (para grafos dirigidos)
    max_possible_edges = len(vertices) * (len(vertices) - 1)
    if max_possible_edges > 0:
        density = total_edges / max_possible_edges
        print(f"   • Densidad: {density:.3f}")
        print(f"   • Tipo: {'Denso' if density > 0.5 else 'Disperso'}")
    
    print(f"\n🔍 Detalles por vértice:")
    for vertex in vertices:
        out_deg = get_out_degree(graph, vertex)
        in_deg = get_in_degree(graph, vertex)
        neighbors = get_neighbors(graph, vertex)
        
        neighbor_str = ", ".join([f"{neighbor}({weight:.1f}km)" for neighbor, weight in neighbors])
        
        print(f"   {vertex}: Out-degree={out_deg}, In-degree={in_deg}")
        if neighbor_str:
            print(f"      └─ Vecinos: [{neighbor_str}]")

def find_most_connected_vertex(graph: Dict[str, List[Tuple[str, float]]]) -> str:
    """Encuentra el vértice con mayor grado total (entrada + salida)."""
    if not graph:
        return ""
    
    max_degree = 0
    most_connected = ""
    
    for vertex in graph.keys():
        total_degree = get_out_degree(graph, vertex) + get_in_degree(graph, vertex)
        if total_degree > max_degree:
            max_degree = total_degree
            most_connected = vertex
    
    return most_connected

def calculate_total_weight(graph: Dict[str, List[Tuple[str, float]]]) -> float:
    """Calcula el peso total de todas las aristas."""
    total = 0.0
    for neighbors in graph.values():
        total += sum(weight for _, weight in neighbors)
    return total

# Programa principal
def main():
    """Función principal para análisis de grafos."""
    print("🐍 === Análisis de Grafos con Python === 🐍")
    
    # Analizar grafo no dirigido
    print("\n" + "="*60)
    print("📂 Cargando grafo NO DIRIGIDO...")
    print("="*60)
    undirected = load_graph("edges_undirected.txt", is_directed=False)
    
    if undirected:
        analyze_graph(undirected, "NO DIRIGIDO")
        
        most_connected = find_most_connected_vertex(undirected)
        if most_connected:
            total_deg = get_out_degree(undirected, most_connected) + get_in_degree(undirected, most_connected)
            print(f"\n🏆 Vértice más conectado: {most_connected} (grado total: {total_deg})")
        
        total_weight = calculate_total_weight(undirected)
        print(f"📏 Distancia total de calles: {total_weight:.1f} km")
    
    # Analizar grafo dirigido
    print("\n" + "="*60)
    print("📂 Cargando grafo DIRIGIDO...")
    print("="*60)
    directed = load_graph("edges_directed.txt", is_directed=True)
    
    if directed:
        analyze_graph(directed, "DIRIGIDO")
        
        most_connected = find_most_connected_vertex(directed)
        if most_connected:
            out_deg = get_out_degree(directed, most_connected)
            in_deg = get_in_degree(directed, most_connected)
            print(f"\n🏆 Vértice más conectado: {most_connected} (out: {out_deg}, in: {in_deg})")
        
        total_weight = calculate_total_weight(directed)
        print(f"📏 Distancia total de calles: {total_weight:.1f} km")
    
    # Comparación
    print("\n" + "="*60)
    print("⚖️  COMPARACIÓN DE REPRESENTACIONES")
    print("="*60)
    
    if undirected and directed:
        print("\n📊 Matriz vs Lista de Adyacencia:")
        print(f"   Para este grafo con {len(directed)} vértices:")
        print(f"   • Matriz: {len(directed)**2} espacios (O(n²))")
        print(f"   • Lista: {sum(len(neighbors) for neighbors in directed.values())} conexiones (O(n+m))")
        print(f"   • Ahorro de memoria: ~{((len(directed)**2 - sum(len(neighbors) for neighbors in directed.values())) / len(directed)**2 * 100):.1f}%")
    
    print("\n🎉 ¡Análisis completado exitosamente!")

if __name__ == "__main__":
    main()
