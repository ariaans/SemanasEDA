using System;
using System.Collections.Generic;
using System.Linq;

namespace Semana8_ProyectoFinal
{
    // Integración de todos los conceptos del curso
    public class GraphSystem<T> where T : IComparable<T>
    {
        private readonly Dictionary<T, List<(T to, double weight)>> graph = new();

        public void AddEdge(T from, T to, double weight = 1.0, bool directed = false)
        {
            if (!graph.ContainsKey(from)) graph[from] = new();
            if (!graph.ContainsKey(to)) graph[to] = new();
            
            graph[from].Add((to, weight));
            if (!directed) graph[to].Add((from, weight));
        }

        // BFS - Camino más corto
        public List<T> BFS(T start, T end)
        {
            var visited = new HashSet<T>();
            var queue = new Queue<T>();
            var parent = new Dictionary<T, T>();
            
            queue.Enqueue(start);
            visited.Add(start);
            
            while (queue.Count > 0)
            {
                var current = queue.Dequeue();
                if (current.Equals(end))
                {
                    return ReconstructPath(parent, start, end);
                }
                
                foreach (var (neighbor, _) in graph[current])
                {
                    if (!visited.Contains(neighbor))
                    {
                        visited.Add(neighbor);
                        parent[neighbor] = current;
                        queue.Enqueue(neighbor);
                    }
                }
            }
            
            return new List<T>();
        }

        // Dijkstra - Camino más corto ponderado
        public (Dictionary<T, double> distances, Dictionary<T, T> previous) Dijkstra(T start)
        {
            var distances = new Dictionary<T, double>();
            var previous = new Dictionary<T, T>();
            var pq = new SortedSet<(double dist, T node)>();
            
            foreach (var node in graph.Keys)
                distances[node] = double.PositiveInfinity;
            
            distances[start] = 0;
            pq.Add((0, start));
            
            while (pq.Count > 0)
            {
                var (currentDist, current) = pq.Min;
                pq.Remove(pq.Min);
                
                if (currentDist > distances[current]) continue;
                
                foreach (var (neighbor, weight) in graph[current])
                {
                    var newDist = distances[current] + weight;
                    if (newDist < distances[neighbor])
                    {
                        pq.Remove((distances[neighbor], neighbor));
                        distances[neighbor] = newDist;
                        previous[neighbor] = current;
                        pq.Add((newDist, neighbor));
                    }
                }
            }
            
            return (distances, previous);
        }

        // DFS - Detección de ciclos
        public bool HasCycle()
        {
            var visited = new HashSet<T>();
            var recStack = new HashSet<T>();
            
            foreach (var node in graph.Keys)
            {
                if (!visited.Contains(node))
                {
                    if (HasCycleDFS(node, visited, recStack))
                        return true;
                }
            }
            return false;
        }

        private bool HasCycleDFS(T node, HashSet<T> visited, HashSet<T> recStack)
        {
            visited.Add(node);
            recStack.Add(node);
            
            foreach (var (neighbor, _) in graph[node])
            {
                if (!visited.Contains(neighbor))
                {
                    if (HasCycleDFS(neighbor, visited, recStack))
                        return true;
                }
                else if (recStack.Contains(neighbor))
                {
                    return true;
                }
            }
            
            recStack.Remove(node);
            return false;
        }

        private List<T> ReconstructPath(Dictionary<T, T> parent, T start, T end)
        {
            var path = new List<T>();
            var current = end;
            
            while (!current.Equals(start))
            {
                path.Add(current);
                if (!parent.ContainsKey(current)) return new List<T>();
                current = parent[current];
            }
            
            path.Add(start);
            path.Reverse();
            return path;
        }

        public void PrintStats()
        {
            Console.WriteLine($"📊 Estadísticas del grafo:");
            Console.WriteLine($"   Vértices: {graph.Count}");
            Console.WriteLine($"   Aristas: {graph.Values.Sum(list => list.Count)}");
            Console.WriteLine($"   Densidad: {(double)graph.Values.Sum(list => list.Count) / (graph.Count * (graph.Count - 1)):F3}");
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("🎓 Semana 8 - Proyecto Final Integrador");
            Console.WriteLine("Sistema Completo de Grafos\n");
            Console.WriteLine(new string('=', 60));

            var system = new GraphSystem<string>();

            // Crear red de ciudades
            Console.WriteLine("\n🏙️ Construyendo red de ciudades...");
            system.AddEdge("Madrid", "Barcelona", 620);
            system.AddEdge("Madrid", "Valencia", 350);
            system.AddEdge("Barcelona", "Valencia", 350);
            system.AddEdge("Barcelona", "Zaragoza", 300);
            system.AddEdge("Valencia", "Sevilla", 650);
            system.AddEdge("Sevilla", "Madrid", 530);
            system.AddEdge("Zaragoza", "Madrid", 320);

            system.PrintStats();

            // BFS - Camino más corto (sin pesos)
            Console.WriteLine("\n🔍 BFS - Camino más corto (número de ciudades):");
            var bfsPath = system.BFS("Madrid", "Sevilla");
            if (bfsPath.Count > 0)
            {
                Console.WriteLine($"   {string.Join(" → ", bfsPath)}");
                Console.WriteLine($"   Ciudades visitadas: {bfsPath.Count}");
            }

            // Dijkstra - Camino más corto (con pesos)
            Console.WriteLine("\n🗺️ Dijkstra - Camino más corto (distancia en km):");
            var (distances, previous) = system.Dijkstra("Madrid");
            
            foreach (var city in new[] { "Barcelona", "Valencia", "Sevilla", "Zaragoza" })
            {
                var path = new List<string>();
                var current = city;
                
                while (current != "Madrid")
                {
                    path.Add(current);
                    if (!previous.ContainsKey(current)) break;
                    current = previous[current];
                }
                
                if (path.Count > 0)
                {
                    path.Add("Madrid");
                    path.Reverse();
                    Console.WriteLine($"   Madrid → {city}: {string.Join(" → ", path)} ({distances[city]:F0} km)");
                }
            }

            // Detección de ciclos
            Console.WriteLine("\n🔄 Detección de ciclos:");
            Console.WriteLine($"   ¿Tiene ciclos? {system.HasCycle()}");

            // Resumen de conceptos aplicados
            Console.WriteLine(new string('=', 60));
            Console.WriteLine("✅ Conceptos aplicados en este proyecto:");
            Console.WriteLine("   ✓ Grafos (Listas de adyacencia)");
            Console.WriteLine("   ✓ BFS (Búsqueda en amplitud)");
            Console.WriteLine("   ✓ DFS (Búsqueda en profundidad)");
            Console.WriteLine("   ✓ Dijkstra (Caminos más cortos ponderados)");
            Console.WriteLine("   ✓ Detección de ciclos");
            Console.WriteLine("   ✓ Análisis de complejidad");
            Console.WriteLine(new string('=', 60));

            Console.WriteLine("\n🎉 ¡Proyecto Final Completado!");
            Console.WriteLine("📚 Curso de Estructuras de Datos Avanzadas - 100% Completo");
        }
    }
}
