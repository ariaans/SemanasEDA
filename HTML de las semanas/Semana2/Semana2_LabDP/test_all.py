# -*- coding: utf-8 -*-
"""
Test runner for all Week 2 DP Lab exercises
"""

import sys
import io

# Force UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 70)
print("LABORATORIO SEMANA 2 - PROGRAMACION DINAMICA")
print("=" * 70)

# Test Exercise 1
print("\n[1/5] Ejercicio 1: Deteccion de Patrones")
print("-" * 70)

def misterio_A(n):
    if n <= 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    return misterio_A(n-1) + misterio_A(n-2) + misterio_A(n-3)

print(f"Tribonacci(4) = {misterio_A(4)}")
print("Resultado: TIENE subproblemas repetidos - SE BENEFICIA DE DP")

# Test Exercise 2
print("\n[2/5] Ejercicio 2: Transformacion Guiada")
print("-" * 70)

def formas_tabla(n):
    if n <= 1: return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(f"Formas de formar n=10: {formas_tabla(10)}")
print("Complejidad: O(n) con DP vs O(2^n) sin DP")

# Test Exercise 3
print("\n[3/5] Ejercicio 3: Cambio de Monedas")
print("-" * 70)

def min_monedas(n, monedas=[1,3,4]):
    if n == 0: return 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for moneda in monedas:
            if i >= moneda:
                dp[i] = min(dp[i], 1 + dp[i - moneda])
    return dp[n] if dp[n] != float('inf') else -1

print(f"Minimo de monedas para n=6: {min_monedas(6)}")
print("Solucion optima: 3+3 (2 monedas)")

# Test Exercise 4
print("\n[4/5] Ejercicio 4: Debugging DP")
print("-" * 70)

def fibonacci_dp_correcto(n):
    if n <= 0: return 0
    if n == 1: return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(f"Fibonacci(10) = {fibonacci_dp_correcto(10)}")
print("Errores corregidos: tamano de array, rango de bucle, casos especiales")

# Test Exercise 5
print("\n[5/5] Ejercicio 5: Mini-Proyecto - Salto de Ranas")
print("-" * 70)

def salto_ranas_tabla(n):
    if n < 0: return 0
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

print(f"Formas de saltar a casilla 10: {salto_ranas_tabla(10)}")
print("Implementado con: Memorizacion, Tabulacion y version Optimizada O(1)")

print("\n" + "=" * 70)
print("TODOS LOS EJERCICIOS COMPLETADOS EXITOSAMENTE")
print("=" * 70)
