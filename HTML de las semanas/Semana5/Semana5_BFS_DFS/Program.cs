using System;
using System.Collections.Generic;
using System.Linq;

namespace Semana5_BFS_DFS
{
    public class GraphTraversal<T> where T : IComparable<T>
    {
        private readonly Dictionary<T, List<T>> adjacencyList = new();

        public void AddEdge(T from, T to, bool directed = false)
        {
            if (!adjacencyList.ContainsKey(from)) adjacencyList[from] = new List<T>();
            if (!adjacencyList.ContainsKey(to)) adjacencyList[to] = new List<T>();
            
            adjacencyList[from].Add(to);
            if (!directed) adjacencyList[to].Add(from);
        }

        // BFS - Búsqueda en Amplitud
        public List<T> BFS(T start)
        {
            var visited = new HashSet<T>();
            var queue = new Queue<T>();
            var result = new List<T>();
            
            queue.Enqueue(start);
            visited.Add(start);
            
            while (queue.Count > 0)
            {
                var current = queue.Dequeue();
                result.Add(current);
                
                foreach (var neighbor in adjacencyList[current])
                {
                    if (!visited.Contains(neighbor))
                    {
                        visited.Add(neighbor);
                        queue.Enqueue(neighbor);
                    }
                }
            }
            
            return result;
        }

        // DFS - Búsqueda en Profundidad (Recursivo)
        public List<T> DFS(T start)
        {
            var visited = new HashSet<T>();
            var result = new List<T>();
            DFSRecursive(start, visited, result);
            return result;
        }

        private void DFSRecursive(T node, HashSet<T> visited, List<T> result)
        {
            visited.Add(node);
            result.Add(node);
            
            foreach (var neighbor in adjacencyList[node])
            {
                if (!visited.Contains(neighbor))
                {
                    DFSRecursive(neighbor, visited, result);
                }
            }
        }

        // DFS Iterativo (con pila)
        public List<T> DFSIterative(T start)
        {
            var visited = new HashSet<T>();
            var stack = new Stack<T>();
            var result = new List<T>();
            
            stack.Push(start);
            
            while (stack.Count > 0)
            {
                var current = stack.Pop();
                
                if (!visited.Contains(current))
                {
                    visited.Add(current);
                    result.Add(current);
                    
                    foreach (var neighbor in adjacencyList[current].AsEnumerable().Reverse())
                    {
                        if (!visited.Contains(neighbor))
                        {
                            stack.Push(neighbor);
                        }
                    }
                }
            }
            
            return result;
        }

        // Detección de ciclos (DFS)
        public bool HasCycle()
        {
            var visited = new HashSet<T>();
            var recStack = new HashSet<T>();
            
            foreach (var node in adjacencyList.Keys)
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
            
            foreach (var neighbor in adjacencyList[node])
            {
                if (!visited.Contains(neighbor))
                {
                    if (HasCycleDFS(neighbor, visited, recStack))
                        return true;
                }
                else if (recStack.Contains(neighbor))
                {
                    return true; // Ciclo detectado
                }
            }
            
            recStack.Remove(node);
            return false;
        }

        // Camino más corto (BFS)
        public List<T> ShortestPath(T start, T end)
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
                
                foreach (var neighbor in adjacencyList[current])
                {
                    if (!visited.Contains(neighbor))
                    {
                        visited.Add(neighbor);
                        parent[neighbor] = current;
                        queue.Enqueue(neighbor);
                    }
                }
            }
            
            return new List<T>(); // No hay camino
        }

        private List<T> ReconstructPath(Dictionary<T, T> parent, T start, T end)
        {
            var path = new List<T>();
            var current = end;
            
            while (!current.Equals(start))
            {
                path.Add(current);
                current = parent[current];
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
            Console.WriteLine("🔍 Semana 5 - BFS y DFS\n");
            
            var graph = new GraphTraversal<string>();
            
            // Crear grafo de ejemplo
            graph.AddEdge("A", "B");
            graph.AddEdge("A", "C");
            graph.AddEdge("B", "D");
            graph.AddEdge("B", "E");
            graph.AddEdge("C", "F");
            graph.AddEdge("E", "G");
            
            Console.WriteLine("📊 Grafo: A-B-C-D-E-F-G\n");
            
            // BFS
            var bfsResult = graph.BFS("A");
            Console.WriteLine($"BFS desde A: {string.Join(" → ", bfsResult)}");
            
            // DFS Recursivo
            var dfsResult = graph.DFS("A");
            Console.WriteLine($"DFS desde A: {string.Join(" → ", dfsResult)}");
            
            // DFS Iterativo
            var dfsIterResult = graph.DFSIterative("A");
            Console.WriteLine($"DFS Iterativo: {string.Join(" → ", dfsIterResult)}");
            
            // Camino más corto
            var path = graph.ShortestPath("A", "G");
            Console.WriteLine($"\nCamino más corto A → G: {string.Join(" → ", path)}");
            Console.WriteLine($"Distancia: {path.Count - 1} aristas");
            
            // Detección de ciclos
            Console.WriteLine($"\n¿Tiene ciclos? {graph.HasCycle()}");
            
            // Grafo con ciclo
            var cyclicGraph = new GraphTraversal<int>();
            cyclicGraph.AddEdge(1, 2, true);
            cyclicGraph.AddEdge(2, 3, true);
            cyclicGraph.AddEdge(3, 1, true);
            
            Console.WriteLine($"Grafo 1→2→3→1 tiene ciclos? {cyclicGraph.HasCycle()}");
            
            Console.WriteLine("\n✅ Programa completado!");
        }
    }
}
