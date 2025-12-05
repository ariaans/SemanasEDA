using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Problema de las Escaleras (1, 2, 3 pasos)");
        Console.WriteLine("Reto: Modificar para permitir saltos de 1, 2 o 3 escalones.");
        
        int n = 35; // A reasonably large number to see performance
        Console.WriteLine($"\nCalculando formas para n={n} escalones...");

        // Recursive Memoization
        memo.Clear();
        var sw = Stopwatch.StartNew();
        long resMemo = EscalerasMemo(n);
        sw.Stop();
        Console.WriteLine($"Memoization (Top-Down): {resMemo} formas (Tiempo: {sw.Elapsed.TotalMilliseconds:F4} ms)");

        // Bottom-Up
        sw.Restart();
        long resTabla = EscalerasTabla(n);
        sw.Stop();
        Console.WriteLine($"Tabulación (Bottom-Up): {resTabla} formas (Tiempo: {sw.Elapsed.TotalMilliseconds:F4} ms)");
        
        // Verify correctness for small n
        Console.WriteLine("\nVerificación de primeros valores:");
        for(int i=1; i<=5; i++)
        {
             Console.WriteLine($"n={i}: {EscalerasTabla(i)} formas");
        }
    }

    // Memoization
    static Dictionary<int, long> memo = new Dictionary<int, long>();
    static long EscalerasMemo(int n)
    {
        if (n < 0) return 0;
        if (n == 0) return 1; // Caso base: 1 forma de estar en el suelo (no hacer nada)
        
        if (memo.ContainsKey(n)) return memo[n];
        
        // Recurrencia: f(n) = f(n-1) + f(n-2) + f(n-3)
        long res = EscalerasMemo(n - 1) + EscalerasMemo(n - 2) + EscalerasMemo(n - 3);
        memo[n] = res;
        return res;
    }

    // Bottom-Up
    static long EscalerasTabla(int n)
    {
        if (n < 0) return 0;
        if (n == 0) return 1;
        
        long[] dp = new long[n + 1];
        dp[0] = 1; // Caso base
        
        for (int i = 1; i <= n; i++)
        {
            // Sumar formas de llegar desde 1, 2 o 3 escalones abajo
            if (i - 1 >= 0) dp[i] += dp[i - 1];
            if (i - 2 >= 0) dp[i] += dp[i - 2];
            if (i - 3 >= 0) dp[i] += dp[i - 3];
        }
        
        return dp[n];
    }
}
