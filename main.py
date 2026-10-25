# código escrito después de haber definido las pruebas del archivo test.py.
def calcular_nomina(horas):
    # 1. Validar que la entrada sea numérica
    try:
        h = float(horas)
    except (ValueError, TypeError):
        return "número no válido"
        
    # 2. Validar rango permitido (0 a 64 horas)
    if h < 0 or h > 64:
        return "número no válido"
        
    # 3. Lógica de cálculo de nómina
    pago_base = 200
    
    if h <= 40:
        # Pago normal
        return h * pago_base
    elif h <= 56:
        # Pago normal (primeras 40 hrs) + pago doble (excedente hasta 56)
        pago_normal = 40 * pago_base
        horas_dobles = h - 40
        return pago_normal + (horas_dobles * pago_base * 2)
    else:
        # Pago normal (primeras 40 hrs) + doble (siguientes 16 hrs) + triple (restantes)
        pago_normal = 40 * pago_base
        pago_doble_max = 16 * (pago_base * 2)
        horas_triples = h - 56
        return pago_normal + pago_doble_max + (horas_triples * pago_base * 3)

if __name__ == '__main__':
    print("--- Sistema de Cálculo de Nómina Semanal ---")
    horas_input = input("Ingresa las horas trabajadas en la semana: ")
    
    resultado = calcular_nomina(horas_input)
    
    if isinstance(resultado, str):
        print(f"Resultado: {resultado}")
    else:
        print(f"El pago total correspondiente es: ${resultado:,.2f}")