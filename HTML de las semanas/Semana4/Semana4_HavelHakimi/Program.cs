using System;
using System.Collections.Generic;
using System.Linq;

namespace Semana4_HavelHakimi
{
    public static class GraphValidator
    {
        /// <summary>
        /// Valida si una secuencia es gráfica usando el algoritmo de Havel-Hakimi.
        /// Complejidad: O(n² log n) por ordenamientos repetidos en cada iteración.
        /// </summary>
        public static bool IsGraphicalSequence(List<int> degrees)
        {
            if (degrees == null || degrees.Count == 0) return true;
            
            // Crear copia para no modificar original
            var seq = new List<int>(degrees);
            
            // Ordenar no creciente
            seq.Sort((a, b) => b.CompareTo(a));
            
            // Verificar suma par y máx grado
            int sum = seq.Sum();
            if (sum % 2 != 0 || seq[0] >= seq.Count) return false;
            
            while (seq.Count > 0)
            {
                int d1 = seq[0];
                seq.RemoveAt(0); // Eliminar d1
                
                if (d1 == 0) return true; // Todos cero
                
                if (d1 > seq.Count) return false;
                
                // Restar 1 de los siguientes d1 elementos
                for (int i = 0; i < d1; i++)
                {
                    seq[i]--;
                    if (seq[i] < 0) return false;
                }
                
                // CRÍTICO: Reordenar después de modificar
                seq.Sort((a, b) => b.CompareTo(a));
            }
            return true;
        }
        
        /// <summary>
        /// Traza paso a paso la ejecución del algoritmo (para debugging)
        /// </summary>
        public static void TraceHavelHakimi(List<int> degrees)
        {
            Console.WriteLine($"Validando secuencia: [{string.Join(", ", degrees)}]");
            Console.WriteLine(new string('=', 60));
            
            var seq = new List<int>(degrees);
            seq.Sort((a, b) => b.CompareTo(a));
            
            int step = 1;
            while (seq.Count > 0)
            {
                Console.WriteLine($"\nPaso {step}: [{string.Join(", ", seq)}]");
                
                int d1 = seq[0];
                if (d1 == 0)
                {
                    Console.WriteLine("✓ Todos los grados son 0 → GRÁFICA");
                    return;
                }
                
                Console.WriteLine($"  Eliminar d₁={d1}, restar 1 de los siguientes {d1} elementos");
                seq.RemoveAt(0);
                
                if (d1 > seq.Count)
                {
                    Console.WriteLine($"✗ Error: d₁={d1} > elementos restantes={seq.Count} → NO GRÁFICA");
                    return;
                }
                
                for (int i = 0; i < d1; i++)
                {
                    seq[i]--;
                    if (seq[i] < 0)
                    {
                        Console.WriteLine($"✗ Error: Grado negativo en posición {i} → NO GRÁFICA");
                        return;
                    }
                }
                
                Console.WriteLine($"  Resultado: [{string.Join(", ", seq)}]");
                seq.Sort((a, b) => b.CompareTo(a));
                Console.WriteLine($"  Reordenado: [{string.Join(", ", seq)}]");
                
                step++;
            }
            
            Console.WriteLine("\n✓ Secuencia reducida a vacía → GRÁFICA");
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("🌐 Semana 4 - Algoritmo de Havel-Hakimi");
            Console.WriteLine("Validación de Secuencias Gráficas\n");
            
            // Casos de prueba oficiales
            var testCases = new List<(List<int> seq, bool expected, string reason)>
            {
                (new List<int> {4, 3, 3, 2, 2, 2, 1, 1}, true, "Suma=18 (par), max=4≤7, converge a ceros"),
                (new List<int> {3, 2, 2, 1}, true, "Ejemplo del documento, converge correctamente"),
                (new List<int> {4, 3, 3, 2, 2, 2}, true, "n=6, suma=16 (par), max=4≤5"),
                (new List<int> {0, 0, 0, 0}, true, "Grafo vacío (sin aristas)"),
                (new List<int> {3, 3, 3, 3}, true, "Grafo completo K₄ (todos conectados)"),
                (new List<int> {3, 3, 3, 1}, false, "Reduce a [2,2,0] → [1,-1] (negativo)"),
                (new List<int> {5, 5, 4, 3, 2, 1}, false, "Suma=20 (par), pero estructura imposible"),
                (new List<int> {3, 2, 1}, false, "Early exit: max=3 > n-1=2"),
                (new List<int> {6, 1, 1, 1, 1, 1, 1}, false, "Estructura imposible"),
                (new List<int> {5, 3, 2, 2, 1}, false, "Suma=13 (impar)")
            };
            
            Console.WriteLine("🧪 Ejecutando casos de prueba...\n");
            int passed = 0;
            int failed = 0;
            
            for (int i = 0; i < testCases.Count; i++)
            {
                var (seq, expected, reason) = testCases[i];
                bool result = GraphValidator.IsGraphicalSequence(seq);
                bool success = result == expected;
                
                string status = success ? "✓ PASS" : "✗ FAIL";
                string resultStr = result ? "Gráfica" : "No Gráfica";
                
                Console.WriteLine($"Caso {i + 1}: {status}");
                Console.WriteLine($"  Secuencia: [{string.Join(", ", seq)}]");
                Console.WriteLine($"  Resultado: {resultStr} (Esperado: {(expected ? "Gráfica" : "No Gráfica")})");
                Console.WriteLine($"  Razón: {reason}\n");
                
                if (success) passed++; else failed++;
            }
            
            Console.WriteLine(new string('=', 60));
            Console.WriteLine($"Resultados: {passed}/{testCases.Count} casos pasados");
            Console.WriteLine(new string('=', 60));
            
            // Ejemplo de traza detallada
            Console.WriteLine("\n📊 Traza detallada del caso [3, 2, 2, 1]:");
            Console.WriteLine(new string('=', 60));
            GraphValidator.TraceHavelHakimi(new List<int> {3, 2, 2, 1});
            
            Console.WriteLine("\n\n📊 Traza detallada del caso NO gráfico [3, 3, 3, 1]:");
            Console.WriteLine(new string('=', 60));
            GraphValidator.TraceHavelHakimi(new List<int> {3, 3, 3, 1});
            
            Console.WriteLine("\n🎉 ¡Programa completado!");
        }
    }
}
