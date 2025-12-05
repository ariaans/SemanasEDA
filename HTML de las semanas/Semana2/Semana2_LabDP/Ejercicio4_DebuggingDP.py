"""
Ejercicio 4: Debugging DP
Encontrar y corregir errores comunes en implementaciones de DP
"""

# ❌ CÓDIGO CON ERRORES
def fibonacci_dp_roto(n):
    """
    Esta función tiene 3 errores comunes en DP.
    ¿Puedes encontrarlos?
    """
    dp = [0] * n  # Error 1: Tamaño insuficiente
    dp[1] = 1
    for i in range(2, n):  # Error 2: Rango incorrecto
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]  # Error 3: Acceso fuera de límites


# ✅ CÓDIGO CORREGIDO
def fibonacci_dp_correcto(n):
    """
    Versión corregida de Fibonacci con DP.
    """
    # Manejar casos especiales
    if n <= 0: return 0
    if n == 1: return 1
    
    # Error 1 CORREGIDO: Array de tamaño n+1 para acceder a dp[n]
    dp = [0] * (n + 1)
    
    # Casos base
    dp[0] = 0
    dp[1] = 1
    
    # Error 2 CORREGIDO: Bucle hasta n+1 para incluir n
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    # Error 3 CORREGIDO: Ya no hay acceso fuera de límites
    return dp[n]


def analizar_errores():
    """
    Análisis detallado de cada error
    """
    print("=" * 70)
    print("EJERCICIO 4: DEBUGGING DP")
    print("=" * 70)
    
    print("\n🔍 ANÁLISIS DE ERRORES:")
    print("=" * 70)
    
    print("\n❌ ERROR 1: Tamaño de array insuficiente")
    print("-" * 70)
    print("CÓDIGO ROTO:")
    print("  dp = [0] * n")
    print("\nPROBLEMA:")
    print("  Si n=5, el array tiene índices [0,1,2,3,4]")
    print("  Pero luego intentamos acceder dp[5] → ¡IndexError!")
    print("\nSOLUCIÓN:")
    print("  dp = [0] * (n + 1)")
    print("  Ahora el array tiene índices [0,1,2,3,4,5] ✓")
    
    print("\n" + "=" * 70)
    print("❌ ERROR 2: Rango del bucle incorrecto")
    print("-" * 70)
    print("CÓDIGO ROTO:")
    print("  for i in range(2, n):")
    print("\nPROBLEMA:")
    print("  Si n=5, el bucle va de 2 a 4 (no incluye 5)")
    print("  Entonces dp[5] nunca se calcula y queda en 0")
    print("\nSOLUCIÓN:")
    print("  for i in range(2, n + 1):")
    print("  Ahora el bucle va de 2 a 5 (incluye 5) ✓")
    
    print("\n" + "=" * 70)
    print("❌ ERROR 3: Acceso fuera de límites")
    print("-" * 70)
    print("CÓDIGO ROTO:")
    print("  return dp[n]  # cuando dp tiene tamaño n")
    print("\nPROBLEMA:")
    print("  Este error es consecuencia del Error 1")
    print("  Si dp tiene tamaño n, los índices válidos son [0, n-1]")
    print("  Acceder a dp[n] causa IndexError")
    print("\nSOLUCIÓN:")
    print("  Corregir el Error 1 automáticamente corrige este")
    print("  Con dp de tamaño (n+1), dp[n] es válido ✓")
    
    print("\n" + "=" * 70)
    print("❌ ERROR ADICIONAL: No manejar casos especiales")
    print("-" * 70)
    print("PROBLEMA:")
    print("  ¿Qué pasa si n=0?")
    print("  dp = [0] * (0 + 1) = [0]")
    print("  dp[1] = 1 → ¡IndexError!")
    print("\nSOLUCIÓN:")
    print("  Agregar validación al inicio:")
    print("  if n <= 0: return 0")
    print("  if n == 1: return 1")


def demostrar_errores():
    """
    Demostración práctica de los errores
    """
    print("\n" + "=" * 70)
    print("🧪 DEMOSTRACIÓN DE ERRORES")
    print("=" * 70)
    
    n = 5
    
    print(f"\nIntentando calcular Fibonacci({n}) con código ROTO:")
    print("-" * 70)
    try:
        resultado = fibonacci_dp_roto(n)
        print(f"Resultado: {resultado}")
        print("⚠️ No hubo error, pero el resultado puede ser incorrecto")
    except IndexError as e:
        print(f"❌ IndexError: {e}")
        print("El código falló como se esperaba")
    
    print(f"\nCalculando Fibonacci({n}) con código CORREGIDO:")
    print("-" * 70)
    resultado = fibonacci_dp_correcto(n)
    print(f"✅ Resultado: {resultado}")
    
    # Verificar con varios valores
    print("\n" + "=" * 70)
    print("✅ VERIFICACIÓN CON MÚLTIPLES VALORES")
    print("=" * 70)
    
    print(f"{'n':<5} {'Fibonacci(n)':<15} {'Verificación':<20}")
    print("-" * 70)
    
    # Valores esperados de Fibonacci
    fibonacci_esperado = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    for i in range(11):
        resultado = fibonacci_dp_correcto(i)
        esperado = fibonacci_esperado[i]
        check = "✓" if resultado == esperado else "✗"
        print(f"{i:<5} {resultado:<15} {check} (esperado: {esperado})")


def errores_comunes_dp():
    """
    Lista de errores comunes en DP y cómo evitarlos
    """
    print("\n" + "=" * 70)
    print("📝 ERRORES COMUNES EN DP Y CÓMO EVITARLOS")
    print("=" * 70)
    
    errores = [
        {
            "error": "Tamaño de array incorrecto",
            "ejemplo": "dp = [0] * n  # cuando necesitas dp[n]",
            "solucion": "dp = [0] * (n + 1)",
            "como_evitar": "Siempre pregúntate: ¿cuál es el índice máximo que voy a acceder?"
        },
        {
            "error": "Rango de bucle incorrecto",
            "ejemplo": "for i in range(2, n):  # no incluye n",
            "solucion": "for i in range(2, n + 1)",
            "como_evitar": "Recuerda que range(a, b) NO incluye b"
        },
        {
            "error": "Casos base no inicializados",
            "ejemplo": "dp[1] = 1  # pero olvidaste dp[0]",
            "solucion": "Inicializar TODOS los casos base explícitamente",
            "como_evitar": "Haz una lista de todos los casos base antes de codificar"
        },
        {
            "error": "Orden incorrecto de llenado",
            "ejemplo": "for i in range(n, 0, -1):  # de mayor a menor",
            "solucion": "for i in range(1, n + 1):  # de menor a mayor",
            "como_evitar": "Asegúrate de que cuando calculas dp[i], dp[i-1] ya esté calculado"
        },
        {
            "error": "No manejar casos especiales",
            "ejemplo": "No verificar n=0, n=1, n negativo",
            "solucion": "Agregar validación al inicio de la función",
            "como_evitar": "Siempre prueba con casos extremos: 0, 1, valores negativos"
        }
    ]
    
    for i, err in enumerate(errores, 1):
        print(f"\n{i}. {err['error']}")
        print(f"   Ejemplo del error: {err['ejemplo']}")
        print(f"   Solución: {err['solucion']}")
        print(f"   Cómo evitarlo: {err['como_evitar']}")


def checklist_dp():
    """
    Checklist para validar implementaciones de DP
    """
    print("\n" + "=" * 70)
    print("✅ CHECKLIST DE VALIDACIÓN DE DP")
    print("=" * 70)
    
    checklist = [
        "¿Definí correctamente qué significa dp[i]?",
        "¿Inicialicé TODOS los casos base?",
        "¿El tamaño del array es suficiente para el índice máximo?",
        "¿El bucle llena la tabla en el orden correcto?",
        "¿La recurrencia usa solo valores ya calculados?",
        "¿Manejé casos especiales (n=0, n=1, negativos)?",
        "¿Probé con casos pequeños (n=0,1,2,3)?",
        "¿Verifiqué que no haya accesos fuera de límites?"
    ]
    
    for i, item in enumerate(checklist, 1):
        print(f"  [{' '}] {i}. {item}")
    
    print("\n💡 Usa este checklist ANTES de ejecutar tu código DP")


if __name__ == "__main__":
    analizar_errores()
    demostrar_errores()
    errores_comunes_dp()
    checklist_dp()
    
    print("\n" + "=" * 70)
    print("🎓 REFLEXIÓN FINAL")
    print("=" * 70)
    print("\n¿Qué tipos de errores son más comunes en DP?")
    print("  1. Errores de índices (tamaño de array, acceso fuera de límites)")
    print("  2. Errores de inicialización (olvidar casos base)")
    print("  3. Errores de orden (llenar la tabla en orden incorrecto)")
    print("\n¿Cómo los puedes evitar en el futuro?")
    print("  1. Dibuja la tabla antes de codificar")
    print("  2. Escribe los casos base primero")
    print("  3. Prueba con valores pequeños (n=0,1,2,3)")
    print("  4. Usa el checklist de validación")
    print("\n" + "=" * 70)
