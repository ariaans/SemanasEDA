"""
Ejercicio 1: Detección de Patrones
Análisis de funciones recursivas para identificar subproblemas repetidos
"""

# Función A: Tribonacci
def misterio_A(n):
    if n <= 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    return misterio_A(n-1) + misterio_A(n-2) + misterio_A(n-3)

# Función B: Suma acumulativa
def misterio_B(n):
    if n <= 1: return n
    return misterio_B(n-1) + n

# Función C: Factorial
def misterio_C(n):
    if n <= 1: return 1
    return n * misterio_C(n-1)

# Análisis de repeticiones
def analizar_repeticiones():
    print("=" * 60)
    print("EJERCICIO 1: DETECCIÓN DE PATRONES")
    print("=" * 60)
    
    print("\n📊 Análisis de Función A (Tribonacci):")
    print("Árbol de llamadas para n=4:")
    print("""
    misterio_A(4)
    ├─ misterio_A(3) [REPETIDO]
    │  ├─ misterio_A(2) [REPETIDO]
    │  │  ├─ misterio_A(1) → 1
    │  │  └─ misterio_A(0) → 0
    │  ├─ misterio_A(1) → 1
    │  └─ misterio_A(0) → 0
    ├─ misterio_A(2) [REPETIDO]
    │  ├─ misterio_A(1) → 1
    │  └─ misterio_A(0) → 0
    └─ misterio_A(1) → 1
    """)
    print("✅ TIENE SUBPROBLEMAS REPETIDOS")
    print("   - misterio_A(2) se calcula 2 veces")
    print("   - misterio_A(1) se calcula 4 veces")
    print("   - misterio_A(0) se calcula 3 veces")
    print("🎯 SE BENEFICIARÍA DE DP")
    
    print("\n" + "=" * 60)
    print("📊 Análisis de Función B (Suma acumulativa):")
    print("Árbol de llamadas para n=4:")
    print("""
    misterio_B(4) = misterio_B(3) + 4
    └─ misterio_B(3) = misterio_B(2) + 3
       └─ misterio_B(2) = misterio_B(1) + 2
          └─ misterio_B(1) → 1
    """)
    print("❌ NO TIENE SUBPROBLEMAS REPETIDOS")
    print("   - Cada valor se calcula exactamente una vez")
    print("   - Es una cadena lineal, no un árbol")
    print("⚠️ NO SE BENEFICIARÍA DE DP (ya es O(n))")
    
    print("\n" + "=" * 60)
    print("📊 Análisis de Función C (Factorial):")
    print("Árbol de llamadas para n=4:")
    print("""
    misterio_C(4) = 4 * misterio_C(3)
    └─ misterio_C(3) = 3 * misterio_C(2)
       └─ misterio_C(2) = 2 * misterio_C(1)
          └─ misterio_C(1) → 1
    """)
    print("❌ NO TIENE SUBPROBLEMAS REPETIDOS")
    print("   - Cada factorial se calcula exactamente una vez")
    print("   - Es una cadena lineal, no un árbol")
    print("⚠️ NO SE BENEFICIARÍA DE DP (ya es O(n))")
    
    print("\n" + "=" * 60)
    print("📝 CONCLUSIÓN:")
    print("=" * 60)
    print("Solo la Función A (Tribonacci) tiene subproblemas repetidos.")
    print("Las funciones B y C son lineales y no necesitan DP.")
    print("\nCRITERIO: Una función se beneficia de DP si:")
    print("  1. Tiene múltiples llamadas recursivas")
    print("  2. Los mismos valores se calculan más de una vez")
    print("  3. El árbol de llamadas tiene ramas que se solapan")

if __name__ == "__main__":
    analizar_repeticiones()
    
    # Verificar resultados
    print("\n" + "=" * 60)
    print("🧪 VERIFICACIÓN DE RESULTADOS:")
    print("=" * 60)
    print(f"Tribonacci(4) = {misterio_A(4)}")
    print(f"Suma acumulativa(4) = {misterio_B(4)}")
    print(f"Factorial(4) = {misterio_C(4)}")
