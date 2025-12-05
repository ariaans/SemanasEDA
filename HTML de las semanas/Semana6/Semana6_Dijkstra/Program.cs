using System;
using System.Collections.Generic;
using System.Linq;

namespace Semana6_Dijkstra
{
    public class Dijkstra<T> where T : IComparable<T>
    {
        private readonly Dictionary<T, List<(T to, double weight)>> graph = new();

        public void AddEdge(T from, T to, double weight, bool directed = false)
        {
            if (!graph.ContainsKey(from)) graph[from] = new();
            if (!graph.ContainsKey(to)) graph[to] = new();
            
            graph[from].Add((to, weight));
            if (!directed) graph[to].Add((from, weight));
        }

        public (Dictionary<T, double> distances, Dictionary<T, T> previous) FindShortestPaths(T start)
        {
            var distances = new Dictionary<T, double>();
            var previous = new Dictionary<T, T>();
            var priorityQueue = new SortedSet<(double dist, T node)>();
            
            foreach (var node in graph.Keys)
            {
                distances[node] = double.PositiveInfinity;
            }
            
            distances[start] = 0;
            priorityQueue.Add((0, start));
            
            while (priorityQueue.Count > 0)
            {
                var (currentDist, current) = priorityQueue.Min;
                priorityQueue.Remove(priorityQueue.Min);
                
                if (currentDist > distances[current]) continue;
                
                foreach (var (neighbor, weight) in graph[current])
                {
                    var newDist = distances[current] + weight;
                    
                    if (newDist < distances[neighbor])
                    {
                        priorityQueue.Remove((distances[neighbor], neighbor));
                        distances[neighbor] = newDist;
                        previous[neighbor] = current;
                        priorityQueue.Add((newDist, neighbor));
                    }
                }
            }
            
            return (distances, previous);
        }

        public List<T> GetPath(Dictionary<T, T> previous, T start, T end)
        {
            var path = new List<T>();
            var current = end;
            
            while (!current.Equals(start))
            {
                path.Add(current);
                if (!previous.ContainsKey(current)) return new List<T>();
                current = previous[current];
            }
            
            path.Add(start);
            path.Reverse();
            return path;
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("🗺️ Semana 6 - Algoritmo de Dijkstra\n");
            
            var dijkstra = new Dijkstra<string>();
            
            // Crear grafo de ejemplo (red de ciudades)
            dijkstra.AddEdge("A", "B", 4);
            dijkstra.AddEdge("A", "C", 2);
            dijkstra.AddEdge("B", "C", 1);
            dijkstra.AddEdge("B", "D", 5);
            dijkstra.AddEdge("C", "D", 8);
            dijkstra.AddEdge("C", "E", 10);
            dijkstra.AddEdge("D", "E", 2);
            dijkstra.AddEdge("D", "F", 6);
            dijkstra.AddEdge("E", "F", 3);
            
            Console.WriteLine("📊 Red de ciudades:");
            Console.WriteLine("A-B(4), A-C(2), B-C(1), B-D(5), C-D(8)");
            Console.WriteLine("C-E(10), D-E(2), D-F(6), E-F(3)\n");
            
            var (distances, previous) = dijkstra.FindShortestPaths("A");
            
            Console.WriteLine("🎯 Distancias más cortas desde A:");
            foreach (var kvp in distances.OrderBy(x => x.Key))
            {
                var dist = kvp.Value == double.PositiveInfinity ? "∞" : kvp.Value.ToString("F1");
                Console.WriteLine($"  A → {kvp.Key}: {dist}");
            }
            
            Console.WriteLine("\n🛤️ Caminos más cortos:");
            foreach (var dest in new[] { "B", "C", "D", "E", "F" })
            {
                var path = dijkstra.GetPath(previous, "A", dest);
                if (path.Count > 0)
                {
                    Console.WriteLine($"  A → {dest}: {string.Join(" → ", path)} (distancia: {distances[dest]:F1})");
                }
            }
            
            Console.WriteLine("\n✅ Programa completado!");
        }
    }
}
