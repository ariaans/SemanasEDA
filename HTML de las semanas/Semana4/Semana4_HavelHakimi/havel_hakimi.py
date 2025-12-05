# -*- coding: utf-8 -*-
"""
Semana 4: Algoritmo de Havel-Hakimi
Validación de secuencias gráficas
"""

from typing import List

def is_graphical_sequence(degrees: List[int]) -> bool:
    """
    Valida secuencia gráfica con Havel-Hakimi.
    Complejidad: O(n² log n) por reordenamiento en cada iteración.
    """
    if not degrees:
        return True
    
    # Crear copia para no modificar original
    seq = sorted(degrees, reverse=True)
    
    # Verificar suma par y máx grado
    total_sum = sum(seq)
    if total_sum % 2 != 0 or seq[0] >= len(seq):
        return False
    
    while seq:
        d1 = seq.pop(0)
        
        if d1 == 0:
            return True
        
        if d1 > len(seq):
            return False
        
        # Restar 1 de los siguientes d1
        for i in range(d1):
            seq[i] -= 1
            if seq[i] < 0:
                return False
        
        # CRÍTICO: Reordenar después de modificar
        seq.sort(reverse=True)
    
    return True


def trace_havel_hakimi(degrees: List[int]):
    """Traza paso a paso la ejecución del algoritmo"""
    print(f"Validando secuencia: {degrees}")
    print("=" * 60)
    
    seq = sorted(degrees, reverse=True)
    step = 1
    
    while seq:
        print(f"\nPaso {step}: {seq}")
        
        d1 = seq[0]
        if d1 == 0:
            print("✓ Todos los grados son 0 → GRÁFICA")
            return
        
        print(f"  Eliminar d₁={d1}, restar 1 de los siguientes {d1} elementos")
        seq.pop(0)
        
        if d1 > len(seq):
            print(f"✗ Error: d₁={d1} > elementos restantes={len(seq)} → NO GRÁFICA")
            return
        
        for i in range(d1):
            seq[i] -= 1
            if seq[i] < 0:
                print(f"✗ Error: Grado negativo en posición {i} → NO GRÁFICA")
                return
        
        print(f"  Resultado: {seq}")
        seq.sort(reverse=True)
        print(f"  Reordenado: {seq}")
        
        step += 1
    
    print("\n✓ Secuencia reducida a vacía → GRÁFICA")


if __name__ == "__main__":
    print("🌐 Semana 4 - Algoritmo de Havel-Hakimi")
    print("Validación de Secuencias Gráficas\n")
    
    # Casos de prueba oficiales
    test_cases = [
        ([4, 3, 3, 2, 2, 2, 1, 1], True, "Suma=18 (par), max=4≤7, converge a ceros"),
        ([3, 2, 2, 1], True, "Ejemplo del documento, converge correctamente"),
        ([4, 3, 3, 2, 2, 2], True, "n=6, suma=16 (par), max=4≤5"),
        ([0, 0, 0, 0], True, "Grafo vacío (sin aristas)"),
        ([3, 3, 3, 3], True, "Grafo completo K₄ (todos conectados)"),
        ([3, 3, 3, 1], False, "Reduce a [2,2,0] → [1,-1] (negativo)"),
        ([5, 5, 4, 3, 2, 1], False, "Suma=20 (par), pero estructura imposible"),
        ([3, 2, 1], False, "Early exit: max=3 > n-1=2"),
        ([6, 1, 1, 1, 1, 1, 1], False, "Estructura imposible"),
        ([5, 3, 2, 2, 1], False, "Suma=13 (impar)")
    ]
    
    print("🧪 Ejecutando casos de prueba...\n")
    passed = 0
    failed = 0
    
    for i, (seq, expected, reason) in enumerate(test_cases, 1):
        result = is_graphical_sequence(seq)
        success = result == expected
        
        status = "✓ PASS" if success else "✗ FAIL"
        result_str = "Gráfica" if result else "No Gráfica"
        expected_str = "Gráfica" if expected else "No Gráfica"
        
        print(f"Caso {i}: {status}")
        print(f"  Secuencia: {seq}")
        print(f"  Resultado: {result_str} (Esperado: {expected_str})")
        print(f"  Razón: {reason}\n")
        
        if success:
            passed += 1
        else:
            failed += 1
    
    print("=" * 60)
    print(f"Resultados: {passed}/{len(test_cases)} casos pasados")
    print("=" * 60)
    
    # Ejemplo de traza detallada
    print("\n📊 Traza detallada del caso [3, 2, 2, 1]:")
    print("=" * 60)
    trace_havel_hakimi([3, 2, 2, 1])
    
    print("\n\n📊 Traza detallada del caso NO gráfico [3, 3, 3, 1]:")
    print("=" * 60)
    trace_havel_hakimi([3, 3, 3, 1])
    
    print("\n🎉 ¡Programa completado!")
