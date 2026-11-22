# ------------------------------------------------------------------
# Nombre del estudiante: Juan Camilo Blanco Sierra
# Grupo: XXXXXX  (reemplazar por el número de su grupo)
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (213022) - Fase 5 Evaluación Final POA
# Problema 3: Reabastecimiento de inventario
# Código fuente: autoría propia
# ------------------------------------------------------------------

# Índices de las columnas de la matriz de inventario
# Formato de cada fila: [Código, Nombre, Stock actual, Stock mínimo requerido]
COL_CODIGO = 0
COL_NOMBRE = 1
COL_STOCK_ACTUAL = 2
COL_STOCK_MINIMO = 3


def crear_inventario():
    """R1: Crea y retorna la matriz de inventario con 6 artículos."""
    inventario = [
        ["A001", "Cuaderno", 15, 40],
        ["A002", "Lapicero", 120, 100],
        ["A003", "Resma de papel", 8, 20],
        ["A004", "Marcador", 30, 30],   # caso borde: stock igual al mínimo
        ["A005", "Carpeta", 5, 25],
        ["A006", "Borrador", 60, 50],
    ]
    return inventario


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """R2: Determina la cantidad exacta a pedir de un artículo.

    Si stock_actual < stock_minimo  -> stock_minimo - stock_actual
    Si stock_actual >= stock_minimo -> 0
    """
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad


def validar_fila(fila):
    """Valida que una fila tenga 4 datos y que los stocks sean enteros >= 0."""
    if len(fila) != 4:
        return False
    stock_actual = fila[COL_STOCK_ACTUAL]
    stock_minimo = fila[COL_STOCK_MINIMO]
    if not isinstance(stock_actual, int) or not isinstance(stock_minimo, int):
        return False
    if stock_actual < 0 or stock_minimo < 0:
        return False
    return True


def mostrar_reporte(inventario):
    """R3: Recorre la matriz y muestra el nombre de cada artículo con la
    cantidad exacta que debe solicitarse. Retorna cuántos artículos
    necesitan reabastecimiento."""
    print("=" * 52)
    print("      REPORTE DE REABASTECIMIENTO DE INVENTARIO")
    print("=" * 52)
    print(f"{'Artículo':<22}{'Stock':>8}{'Mínimo':>9}{'A pedir':>11}")
    print("-" * 52)

    total_a_reabastecer = 0
    for fila in inventario:
        if not validar_fila(fila):
            print(f"Fila inválida omitida: {fila}")
            continue

        nombre = fila[COL_NOMBRE]
        stock_actual = fila[COL_STOCK_ACTUAL]
        stock_minimo = fila[COL_STOCK_MINIMO]
        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        print(f"{nombre:<22}{stock_actual:>8}{stock_minimo:>9}{cantidad:>11}")
        if cantidad > 0:
            total_a_reabastecer += 1

    print("-" * 52)
    print(f"Artículos que requieren reabastecimiento: {total_a_reabastecer}")
    return total_a_reabastecer


def main():
    inventario = crear_inventario()
    mostrar_reporte(inventario)


if __name__ == "__main__":
    main()
