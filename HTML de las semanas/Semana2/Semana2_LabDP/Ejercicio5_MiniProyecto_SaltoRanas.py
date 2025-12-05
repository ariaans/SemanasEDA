"""
Ejercicio 5: Mini-Proyecto - Salto de Ranas
Implementación completa con memoización y tabulación
"""

# ============================================================================
# PROBLEMA: SALTO DE RANAS
# ============================================================================
# Una rana puede saltar 1, 2 o 3 casillas.
# ¿Cuántas formas hay de llegar a la casilla n?
# ============================================================================

def salto_ranas_memo(n, memo=None):
    """
    Versión con memoización (Top-Down).
    
    La rana puede saltar 1, 2 o 3 casillas.
    Para llegar a la casilla n, puede venir de:
    - casilla n-1 (dando un salto de 1)
    - casilla n-2 (dando un salto de 2)
    - casilla n-3 (dando un salto de 3)
    
    Recurrencia: f(n) = f(n-1) + f(n-2) + f(n-3)
    """
    if memo is None:
        memo = {}
    
    # Casos base
    if n < 0: return 0
    if n == 0: return 1  # Una forma de estar en el inicio
    if n == 1: return 1  # Solo un salto de 1
    if n == 2: return 2  # 1+1 o 2
    
    # ¿Ya lo calculé?
    if n in memo:
        return memo[n]
    
    # Calcular y guardar
    resultado = (salto_ranas_memo(n-1, memo) + 
                 salto_ranas_memo(n-2, memo) + 
                 salto_ranas_memo(n-3, memo))
    memo[n] = resultado
    return resultado


def salto_ranas_tabla(n):
    """
    Versión con tabulación (Bottom-Up).
    
    Construye la solución desde los casos base hacia arriba.
    """
    if n < 0: return 0
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    
    # Crear tabla
    dp = [0] * (n + 1)
    
    # Casos base
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    # Llenar tabla
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]


def salto_ranas_optimizado(n):
    """
    Versión optimizada en espacio O(1).
    
    Solo necesitamos los últimos 3 valores, no toda la tabla.
    """
    if n < 0: return 0
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    
    # Solo guardamos los últimos 3 valores
    a, b, c = 1, 1, 2  # dp[0], dp[1], dp[2]
    
    for i in range(3, n + 1):
        nuevo = a + b + c
        a, b, c = b, c, nuevo
    
    return c


if __name__ == "__main__":
    import time
    
    print("=" * 70)
    print("MINI-PROYECTO: SALTO DE RANAS")
    print("=" * 70)
    
    print("\n📖 DESCRIPCIÓN DEL PROBLEMA:")
    print("-" * 70)
    print("Una rana puede saltar 1, 2 o 3 casillas a la vez.")
    print("¿De cuántas formas diferentes puede llegar a la casilla n?")
    
    print("\n📊 CASOS PEQUEÑOS:")
    print("-" * 70)
    print("n=0: 1 forma (estar en el inicio)")
    print("n=1: 1 forma (salto de 1)")
    print("n=2: 2 formas (1+1, 2)")
    print("n=3: 4 formas (1+1+1, 1+2, 2+1, 3)")
    print("n=4: 7 formas (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 1+3, 3+1, 2+2)")
    
    # Verificar casos pequeños
    print("\n✅ VERIFICACIÓN DE CASOS PEQUEÑOS:")
    print("-" * 70)
    esperados = [1, 1, 2, 4, 7, 13, 24, 44, 81]
    
    print(f"{'n':<5} {'Memoización':<15} {'Tabulación':<15} {'Optimizado':<15} {'Esperado':<10} {'✓'}")
    print("-" * 70)
    
    for i in range(len(esperados)):
        memo_res = salto_ranas_memo(i)
        tabla_res = salto_ranas_tabla(i)
        opt_res = salto_ranas_optimizado(i)
        check = "✓" if memo_res == tabla_res == opt_res == esperados[i] else "✗"
        print(f"{i:<5} {memo_res:<15} {tabla_res:<15} {opt_res:<15} {esperados[i]:<10} {check}")
    
    # Comparación de rendimiento
    print("\n⚡ COMPARACIÓN DE RENDIMIENTO:")
    print("-" * 70)
    
    test_values = [10, 20, 30, 50, 100]
    
    print(f"{'n':<8} {'Memoización (ms)':<20} {'Tabulación (ms)':<20} {'Optimizado (ms)':<20}")
    print("-" * 70)
    
    for n in test_values:
        # Memoización
        start = time.perf_counter()
        res_memo = salto_ranas_memo(n)
        time_memo = (time.perf_counter() - start) * 1000
        
        # Tabulación
        start = time.perf_counter()
        res_tabla = salto_ranas_tabla(n)
        time_tabla = (time.perf_counter() - start) * 1000
        
        # Optimizado
        start = time.perf_counter()
        res_opt = salto_ranas_optimizado(n)
        time_opt = (time.perf_counter() - start) * 1000
        
        print(f"{n:<8} {time_memo:<20.4f} {time_tabla:<20.4f} {time_opt:<20.4f}")
    
    # Análisis de complejidad
    print("\n📊 ANÁLISIS DE COMPLEJIDAD:")
    print("-" * 70)
    print("Memoización:")
    print("  - Tiempo: O(n)")
    print("  - Espacio: O(n) para el diccionario + O(n) para la pila de recursión")
    print("\nTabulación:")
    print("  - Tiempo: O(n)")
    print("  - Espacio: O(n) para la tabla")
    print("\nOptimizado:")
    print("  - Tiempo: O(n)")
    print("  - Espacio: O(1) - solo 3 variables")
    
    # Explicación detallada
    print("\n" + "=" * 70)
    print("📝 EXPLICACIÓN DETALLADA")
    print("=" * 70)
    
    print("\n🔍 ¿Por qué funciona?")
    print("-" * 70)
    print("Para llegar a la casilla n, la rana debe haber estado en:")
    print("  - casilla n-1 (y dar un salto de 1)")
    print("  - casilla n-2 (y dar un salto de 2)")
    print("  - casilla n-3 (y dar un salto de 3)")
    print("\nEntonces, el número total de formas es la SUMA de las formas")
    print("de llegar a cada una de esas casillas previas.")
    
    print("\n🎯 ¿Cuál enfoque es mejor?")
    print("-" * 70)
    print("MEMOIZACIÓN:")
    print("  ✅ Fácil de implementar desde la versión recursiva")
    print("  ✅ Solo calcula los subproblemas necesarios")
    print("  ❌ Usa más memoria (diccionario + pila de recursión)")
    print("  ❌ Más lento por el overhead de las llamadas recursivas")
    print("\nTABULACIÓN:")
    print("  ✅ Más rápida (sin overhead de recursión)")
    print("  ✅ Fácil de optimizar el espacio")
    print("  ❌ Calcula todos los subproblemas (incluso los innecesarios)")
    print("  ❌ Requiere pensar en el orden de llenado")
    print("\nOPTIMIZADO:")
    print("  ✅ Mínimo uso de memoria O(1)")
    print("  ✅ Más rápido")
    print("  ❌ Solo funciona cuando solo necesitas los últimos k valores")
    
    print("\n💭 MI PREFERENCIA:")
    print("-" * 70)
    print("Para APRENDER y PROTOTIPAR: Memoización")
    print("  - Es más natural pensar recursivamente")
    print("  - Fácil de derivar de la definición del problema")
    print("\nPara PRODUCCIÓN: Tabulación u Optimizado")
    print("  - Mejor rendimiento")
    print("  - Más predecible (sin riesgo de stack overflow)")
    print("  - Optimizado si solo necesitas el resultado final")
    
    print("\n" + "=" * 70)
    print("✅ MINI-PROYECTO COMPLETADO")
    print("=" * 70)
