import os
import pandas as pd
import numpy as np

# Asegurar que las carpetas existan usando 'os'
os.makedirs(os.path.join('data', 'raw'), exist_ok=True)
os.makedirs(os.path.join('data', 'processed'), exist_ok=True)

print("⏳ Generando datasets con datos sucios del mundo real...")

# 1. GENERAR VENTAS.CSV (Con duplicados, nulos y valores inválidos)
data_ventas = {
    'id_transaccion': [1001, 1002, 1003, 1004, 1002, 1005, 1006, 1007],
    'id_cliente': [501, 502, 503, 504, 502, 505, 506, 507],
    'id_producto': ['P001', 'P002', 'P001', 'P003', 'P002', 'P004', 'P001', 'P003'],
    'id_sucursal': [1, 2, 1, 3, 2, 1, 2, 99], # 99 es una sucursal inválida/inexistente
    'cantidad': [1, 2, 1, -5, 2, 1, 3, 1],    # Cantidad negativa (-5) por error de sistema
    'monto_total': [15000.0, 700.0, np.nan, 4500.0, 700.0, 600.0, 45000.0, 600.0] # Un nulo crítico
}
df_ventas = pd.DataFrame(data_ventas)
df_ventas.to_csv(os.path.join('data', 'raw', 'ventas.csv'), index=False)

# 2. GENERAR INVENTARIO.JSON (Con stocks vacíos)
data_inventario = {
    'id_producto': ['P001', 'P002', 'P003', 'P004'],
    'nombre_producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado'],
    'categoria': ['Electrónica', 'Accesorios', 'Electrónica', 'Accesorios'],
    'precio_base': [15000.0, 350.0, 4500.0, 600.0],
    'stock': [5.0, np.nan, 7.0, 20.0] # El Mouse tiene stock nulo (NaN)
}
df_inventario = pd.DataFrame(data_inventario)
df_inventario.to_json(os.path.join('data', 'raw', 'inventario.json'), orient='records', indent=4)

# 3. GENERAR SUCURSALES.XLSX (Datos maestros limpios)
data_sucursales = {
    'id_sucursal': [1, 2, 3],
    'ciudad': ['Guadalajara', 'Zapopan', 'Tlaquepaque']
}
df_sucursales = pd.DataFrame(data_sucursales)
df_sucursales.to_excel(os.path.join('data', 'raw', 'sucursales.xlsx'), index=False)

print("✅ Archivos generados exitosamente en 'data/raw/':")
print("   - ventas.csv (Contiene nulos, duplicados y cantidades negativas)")
print("   - inventario.json (Contiene stocks faltantes)")
print("   - sucursales.xlsx (Mapeo de ciudades)")