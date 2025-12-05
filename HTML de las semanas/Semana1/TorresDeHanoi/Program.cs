using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Torres de Hanoi - Comparación Recursiva vs Iterativa");
        
        // Run benchmark for n=10, 15, 20
        // Warning: n=20 takes a while (~300ms per run * 5 runs * 2 algos = ~3s)
        // n=25 takes ~10s per run, so we might skip it for quick testing.
        int[] testValues = { 10, 15, 20 };
        
        foreach (var n in testValues)
        {
            AnalisisComparativo(n);
            Console.WriteLine();
        }
    }

    static List<string> HanoiRecursivo(int n, char origen, char destino, char auxiliar)
    {
        var moves = new List<string>();
        
        void Solve(int k, char from, char to, char aux)
        {
            if (k == 0) return;
            
            Solve(k - 1, from, aux, to);
            moves.Add($"{from} -> {to}");
            Solve(k - 1, aux, to, from);
        }
        
        Solve(n, origen, destino, auxiliar);
        return moves;
    }

    static List<string> HanoiIterativo(int n, char A, char B, char C)
    {
        var moves = new List<string>();

        var cicloImpar = new (char from, char to)[] { (A, C), (C, B), (B, A) };
        var cicloPar   = new (char from, char to)[] { (A, B), (B, C), (C, A) };
        var ciclo = (n % 2 == 1) ? cicloImpar : cicloPar;

        var pos = new Dictionary<int, char>();
        for (int d = 1; d <= n; d++) pos[d] = A;

        int total = (1 << n) - 1;
        int idxCiclo = 0;

        int TopDisk(char peg)
        {
            int best = int.MaxValue;
            for (int d = 1; d <= n; d++)
                if (pos[d] == peg) { best = d; break; }
            return best;
        }

        bool MoverLegal(char p1, char p2)
        {
            int top1 = TopDisk(p1), top2 = TopDisk(p2);
            if (top1 == int.MaxValue && top2 == int.MaxValue) return false;
            
            if (top2 == int.MaxValue || (top1 < top2))
            {
                pos[top1] = p2;
                moves.Add($"{p1} -> {p2}");
            }
            else
            {
                pos[top2] = p1;
                moves.Add($"{p2} -> {p1}");
            }
            return true;
        }

        for (int move = 1; move <= total; move++)
        {
            if (move % 2 == 1)
            {
                var (from, to) = ciclo[idxCiclo];
                idxCiclo = (idxCiclo + 1) % 3;
                pos[1] = to;
                moves.Add($"{from} -> {to}");
            }
            else
            {
                var pegs = new HashSet<char> { A, B, C };
                pegs.Remove(pos[1]);
                var it = pegs.GetEnumerator();
                it.MoveNext(); char pX = it.Current;
                it.MoveNext(); char pY = it.Current;
                MoverLegal(pX, pY);
            }
        }

        return moves;
    }

    static void AnalisisComparativo(int n)
    {
        const int Warmups = 1;
        const int Runs = 5;
        var sw = new Stopwatch();
        
        for (int i = 0; i < Warmups; i++)
        {
            _ = HanoiRecursivo(n, 'A', 'C', 'B');
            _ = HanoiIterativo(n, 'A', 'C', 'B');
        }
        
        long ticksRec = 0, ticksIte = 0;
        
        for (int r = 0; r < Runs; r++)
        {
            sw.Restart();
            _ = HanoiRecursivo(n, 'A', 'C', 'B');
            sw.Stop();
            ticksRec += sw.ElapsedTicks;
            
            sw.Restart();
            _ = HanoiIterativo(n, 'A', 'C', 'B');
            sw.Stop();
            ticksIte += sw.ElapsedTicks;
        }
        
        double msRec = (ticksRec / (double)Runs) * 1000.0 / Stopwatch.Frequency;
        double msIte = (ticksIte / (double)Runs) * 1000.0 / Stopwatch.Frequency;
        
        Console.WriteLine($"ANÁLISIS COMPARATIVO (n={n}):");
        Console.WriteLine($"Recursivo: {msRec:F3} ms - {(1 << n) - 1} movimientos");
        Console.WriteLine($"Iterativo: {msIte:F3} ms");
        Console.WriteLine("Complejidad temporal (ambas): O(2^n)");
        Console.WriteLine("Complejidad espacial: recursivo O(n); iterativo O(1) si es bitwise, O(n) si usa pila.");
    }
}
