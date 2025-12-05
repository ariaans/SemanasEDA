"""
Ejercicio 3: Problema del Cambio de Monedas Simplificado
Monedas: [1, 3, 4] centavos
Objetivo: Encontrar el número MÍNIMO de monedas para formar n centavos
"""

def min_monedas(n, monedas=[1, 3, 4]):
    """
    Encuentra el número mínimo de monedas necesarias para formar n centavos.
    
    Args:
        n: cantidad a formar
        monedas: lista de denominaciones disponibles
    
    Returns:
        Número mínimo de monedas, o -1 si es imposible
    """
    # Casos base
    if n == 0: return 0
    if n < 0: return float('inf')  # Imposible
    
    # Crear tabla DP
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 0 monedas para formar 0
    
    # Llenar tabla
    for i in range(1, n + 1):
        for moneda in monedas:
            if i >= moneda:
                # Si uso una moneda de valor 'moneda',
                # necesito dp[i - moneda] monedas para el resto
                dp[i] = min(dp[i], 1 + dp[i - moneda])
    
    return dp[n] if dp[n] != float('inf') else -1


def min_monedas_con_solucion(n, monedas=[1, 3, 4]):
    """
    Versión que también retorna qué monedas usar.
    """
    if n == 0: return 0, []
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    parent = [-1] * (n + 1)  # Para reconstruir la solución
    
    for i in range(1, n + 1):
        for moneda in monedas:
            if i >= moneda and dp[i - moneda] + 1 < dp[i]:
                dp[i] = dp[i - moneda] + 1
                parent[i] = moneda
    
    if dp[n] == float('inf'):
        return -1, []
    
    # Reconstruir solución
    solucion = []
    actual = n
    while actual > 0:
        moneda_usada = parent[actual]
        solucion.append(moneda_usada)
        actual -= moneda_usada
    
    return dp[n], solucion


def resolver_casos_manuales():
    """
    PASO 1: Resolver casos manuales para n=1,2,3,4,5,6
    """
    print("=" * 70)
    print("PASO 1: CASOS MANUALES")
    print("=" * 70)
    print("Monedas disponibles: [1, 3, 4]\n")
    
    casos = [
        (1, "1", 1),
        (2, "1+1", 2),
        (3, "3", 1),
        (4, "4", 1),
        (5, "4+1", 2),
        (6, "3+3", 2),
    ]
    
    print(f"{'n':<5} {'Combinación óptima':<25} {'Número de monedas':<20}")
    print("-" * 70)
    for n, combinacion, num_monedas in casos:
        print(f"{n:<5} {combinacion:<25} {num_monedas:<20}")
    
    print("\n💡 OBSERVACIONES:")
    print("  - Para n=3 y n=4, es mejor usar una sola moneda")
    print("  - Para n=5, usamos 4+1 (2 monedas) en lugar de 3+1+1 (3 monedas)")
    print("  - Para n=6, usamos 3+3 (2 monedas) en lugar de 4+1+1 (3 monedas)")


def explicar_recurrencia():
    """
    PASO 2: Explicar la relación de recurrencia
    """
    print("\n" + "=" * 70)
    print("PASO 2: RELACIÓN DE RECURRENCIA")
    print("=" * 70)
    
    print("\n📐 FÓRMULA:")
    print("  min_monedas(n) = 1 + min(")
    print("      min_monedas(n-1),  # si uso moneda de 1")
    print("      min_monedas(n-3),  # si uso moneda de 3")
    print("      min_monedas(n-4)   # si uso moneda de 4")
    print("  )")
    
    print("\n🤔 ¿POR QUÉ EL '+1'?")
    print("  Porque estamos usando UNA moneda, más el número óptimo")
    print("  de monedas para formar el resto.")
    
    print("\n📝 EJEMPLO: min_monedas(5)")
    print("  Opción 1: Usar moneda de 1 → 1 + min_monedas(4) = 1 + 1 = 2")
    print("  Opción 2: Usar moneda de 3 → 1 + min_monedas(2) = 1 + 2 = 3")
    print("  Opción 3: Usar moneda de 4 → 1 + min_monedas(1) = 1 + 1 = 2")
    print("  Mínimo: min(2, 3, 2) = 2 ✓")


def visualizar_construccion_tabla(n=10):
    """
    PASO 3: Visualizar la construcción de la tabla DP
    """
    print("\n" + "=" * 70)
    print(f"PASO 3: CONSTRUCCIÓN DE LA TABLA (n={n})")
    print("=" * 70)
    
    monedas = [1, 3, 4]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    print(f"\nInicialización: dp[0] = 0 (caso base)")
    print(f"dp = {[0 if x == 0 else '∞' for x in dp[:n+1]]}\n")
    
    for i in range(1, n + 1):
        opciones = []
        for moneda in monedas:
            if i >= moneda:
                valor = dp[i - moneda]
                if valor != float('inf'):
                    opciones.append((moneda, valor + 1))
        
        if opciones:
            mejor_moneda, mejor_valor = min(opciones, key=lambda x: x[1])
            dp[i] = mejor_valor
            
            print(f"i={i:2d}: ", end="")
            for moneda, valor in opciones:
                marca = "✓" if moneda == mejor_moneda else " "
                print(f"[moneda {moneda}: 1+dp[{i-moneda}]={valor}]{marca} ", end="")
            print(f"→ dp[{i}] = {dp[i]}")
    
    print(f"\nTabla final: {[x if x != float('inf') else '∞' for x in dp]}")
    print(f"\nResultado: min_monedas({n}) = {dp[n]}")


if __name__ == "__main__":
    print("=" * 70)
    print("EJERCICIO 3: PROBLEMA DEL CAMBIO DE MONEDAS")
    print("=" * 70)
    
    # Paso 1: Casos manuales
    resolver_casos_manuales()
    
    # Paso 2: Explicar recurrencia
    explicar_recurrencia()
    
    # Paso 3: Visualizar construcción de tabla
    visualizar_construccion_tabla(10)
    
    # Pruebas adicionales
    print("\n" + "=" * 70)
    print("🧪 PRUEBAS ADICIONALES")
    print("=" * 70)
    
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
    
    for n in test_cases:
        num_monedas, solucion = min_monedas_con_solucion(n)
        solucion_str = "+".join(map(str, sorted(solucion, reverse=True)))
        print(f"n={n:2d}: {num_monedas} monedas → {solucion_str}")
    
    print("\n" + "=" * 70)
    print("📊 ANÁLISIS DE COMPLEJIDAD")
    print("=" * 70)
    print("Complejidad temporal: O(n × m)")
    print("  donde n = cantidad a formar")
    print("        m = número de denominaciones de monedas")
    print("\nComplejidad espacial: O(n)")
    print("  para almacenar la tabla dp")
    
    print("\n" + "=" * 70)
    print("✅ EJERCICIO COMPLETADO")
    print("=" * 70)
