"""
Ejercicio 2: Transformación Guiada
Transformación paso a paso de recursión ingenua a DP
"""

# PASO 1: Versión ingenua (recursiva pura)
def formas_ingenuo(n):
    """
    Cuenta de cuántas formas se puede formar el número n
    usando pasos de 1 o 2.
    
    Ejemplo: n=3 → 3 formas (1+1+1, 1+2, 2+1)
    """
    # Casos base
    if n <= 0: return 1
    if n == 1: return 1
    
    # Relación de recurrencia:
    # Para formar n, puedo venir de (n-1) dando un paso de 1,
    # o de (n-2) dando un paso de 2
    return formas_ingenuo(n-1) + formas_ingenuo(n-2)


# PASO 3: Versión con memoización (Top-Down)
def formas_memo(n, memo=None):
    """
    Versión optimizada con memoización.
    Guarda resultados ya calculados para evitar recalcularlos.
    """
    if memo is None:
        memo = {}
    
    # Casos base
    if n <= 0: return 1
    if n == 1: return 1
    
    # ¿Ya lo calculé antes?
    if n in memo:
        return memo[n]
    
    # Calcularlo y guardarlo
    resultado = formas_memo(n-1, memo) + formas_memo(n-2, memo)
    memo[n] = resultado
    return resultado


# PASO 4: Versión Bottom-Up (Tabulación)
def formas_tabla(n):
    """
    Versión iterativa usando una tabla.
    Construye la solución desde los casos base hacia arriba.
    """
    if n <= 1: return 1
    
    # Crear tabla
    dp = [0] * (n + 1)
    
    # Casos base
    dp[0] = 1
    dp[1] = 1
    
    # Llenar tabla iterativamente
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


# Función para visualizar el árbol de llamadas
def visualizar_arbol_formas(n, nivel=0, memo_visual=None):
    """
    Visualiza el árbol de llamadas recursivas para formas(n)
    """
    if memo_visual is None:
        memo_visual = {}
    
    indent = "  " * nivel
    
    if n in memo_visual:
        print(f"{indent}formas({n}) [YA CALCULADO] = {memo_visual[n]}")
        return memo_visual[n]
    
    if n <= 0:
        print(f"{indent}formas({n}) = 1 (caso base)")
        return 1
    if n == 1:
        print(f"{indent}formas({n}) = 1 (caso base)")
        return 1
    
    print(f"{indent}formas({n})")
    print(f"{indent}├─ calculando formas({n-1})")
    r1 = visualizar_arbol_formas(n-1, nivel+1, memo_visual)
    print(f"{indent}└─ calculando formas({n-2})")
    r2 = visualizar_arbol_formas(n-2, nivel+1, memo_visual)
    
    resultado = r1 + r2
    memo_visual[n] = resultado
    print(f"{indent}formas({n}) = {r1} + {r2} = {resultado}")
    return resultado


if __name__ == "__main__":
    import time
    
    print("=" * 70)
    print("EJERCICIO 2: TRANSFORMACIÓN GUIADA")
    print("=" * 70)
    
    # PASO 2: Identificar repeticiones
    print("\n📊 PASO 2: Visualización del árbol para formas(4)")
    print("=" * 70)
    visualizar_arbol_formas(4)
    
    print("\n" + "=" * 70)
    print("🔍 ANÁLISIS DE REPETICIONES:")
    print("=" * 70)
    print("Como puedes ver en el árbol:")
    print("  - formas(2) se calcula 2 veces")
    print("  - formas(1) se calcula 3 veces")
    print("  - formas(0) se calcula 2 veces")
    print("\n¡Esto es ineficiente! DP puede ayudar.")
    
    # Comparación de rendimiento
    print("\n" + "=" * 70)
    print("⚡ COMPARACIÓN DE RENDIMIENTO:")
    print("=" * 70)
    
    test_values = [10, 20, 30]
    
    for n in test_values:
        print(f"\nn = {n}:")
        
        # Versión ingenua (solo para n pequeños)
        if n <= 30:
            start = time.perf_counter()
            res_ingenuo = formas_ingenuo(n)
            time_ingenuo = (time.perf_counter() - start) * 1000
            print(f"  Ingenua:     {res_ingenuo:>10} formas ({time_ingenuo:>8.4f} ms)")
        
        # Versión memoización
        start = time.perf_counter()
        res_memo = formas_memo(n)
        time_memo = (time.perf_counter() - start) * 1000
        print(f"  Memoización: {res_memo:>10} formas ({time_memo:>8.4f} ms)")
        
        # Versión tabla
        start = time.perf_counter()
        res_tabla = formas_tabla(n)
        time_tabla = (time.perf_counter() - start) * 1000
        print(f"  Tabulación:  {res_tabla:>10} formas ({time_tabla:>8.4f} ms)")
    
    print("\n" + "=" * 70)
    print("📝 CONCLUSIONES:")
    print("=" * 70)
    print("1. La versión ingenua crece exponencialmente O(2^n)")
    print("2. Memoización y Tabulación son O(n)")
    print("3. Tabulación suele ser más rápida (menos overhead)")
    print("4. Memoización es más fácil de implementar desde recursión")
    
    # Verificar tabla paso a paso
    print("\n" + "=" * 70)
    print("📋 CONSTRUCCIÓN DE LA TABLA (n=6):")
    print("=" * 70)
    n = 6
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    print(f"Inicialización: dp = {dp}")
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"Paso {i-1}: dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
        print(f"         dp = {dp}")
    
    print(f"\nResultado final: formas({n}) = {dp[n]}")
