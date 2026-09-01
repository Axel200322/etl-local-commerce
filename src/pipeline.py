import os
import pandas as pd

def ejecutar_pipeline():
    print("🚀 Iniciando Pipeline ETL...")
    
    # ==========================================
    # FASE 1: EXTRACCIÓN (E)
    # ==========================================
    print("\n⏳ Cargando fuentes de datos...")
    
    # 1. Construye las rutas usando os.path.join
    ruta_ventas = os.path.join('data', 'raw', 'ventas.csv')
    ruta_inventario = os.path.join('data','raw', 'inventario.json' )
    ruta_sucursales = os.path.join('data','raw', 'sucursales.xlsx' )
    
    # 2. Lee cada archivo con su función correspondiente de Pandas
    df_ventas = pd.read_csv(ruta_ventas)
    df_inventario = pd.read_json(ruta_inventario)
    df_sucursales = pd.read_excel(ruta_sucursales)
    print("Columnas reales en el CSV de ventas:", df_ventas.columns.tolist())

    
    # 3. Verificamos las dimensiones usando .shape
    print(f"✅ Ventas cargadas correctamente. Dimensiones: {df_ventas.shape}")
    print(f"✅ Inventario cargado correctamente. Dimensiones: {df_inventario.shape}")
    print(f"✅ Sucursales cargadas correctamente. Dimensiones: {df_sucursales.shape}")
    
    # Aquí se guardarán las siguientes fases (Limpieza, Transformación, Carga)

    df_ventas = df_ventas.drop_duplicates()
    df_ventas = df_ventas.dropna(subset=['monto_total'])
    df_ventas = df_ventas[df_ventas['cantidad'] > 0]

    df_inventario['stock'] = df_inventario['stock'].fillna(0)

    print("✅ Datos limpios y listos para integrarse.")
    print(f"   Nuevas dimensiones de Ventas: {df_ventas.shape}")

    # ==========================================
    # FASE 3: ENRIQUECIMIENTO Y RESUMEN (T)
    # ==========================================
    print("\n📊 Cruzando datos y generando reporte...")
    
    # 1. Unimos Ventas con Sucursales usando el 'id_sucursal'
    df_unido = pd.merge(df_ventas, df_sucursales, on='id_sucursal', how='inner')
    
    # 2. Unimos el resultado con Inventario usando el 'id_producto'
    df_final = pd.merge(df_unido, df_inventario, on='id_producto', how='inner')

    # 3. Agrupamos por ciudad para el reporte financiero
    # Pista: Usa .agg() con un diccionario para aplicar 'sum' y 'mean' a 'monto_total'
    reporte_ciudad = df_final.groupby('ciudad').agg(
    total=('monto_total', 'sum'),
    promedio=('monto_total', 'mean')
    )
    
    # 4. Cambiamos los nombres de las columnas para que se vea profesional
    reporte_ciudad.columns = ['ventas_totales', 'promedio_ticket']
    
    # 5. Ordenamos de mayor a menor por 'ventas_totales'
    reporte_ciudad = reporte_ciudad.sort_values(by='ventas_totales', ascending=False)
    
    print("\n🏆 REPORTE EJECUTIVO POR CIUDAD:")
    print(reporte_ciudad)
    
    # ==========================================
    # FASE 4: CARGA (L)
    # ==========================================
    print("\n💾 Guardando resultados en 'data/processed/'...")
    
    # 1. Definimos las rutas de destino
    ruta_salida_csv = os.path.join('data', 'processed', 'reporte_ventas_ciudad.csv')
    ruta_salida_json = os.path.join('data', 'processed', 'datos_maestros_limpios.json')
    
    # 2. Exportamos el reporte (dejamos index=True porque las ciudades están en el índice)
    reporte_ciudad.to_csv(ruta_salida_csv, index=True)
    
    # 3. Exportamos todo el DataFrame unificado a JSON
    df_final.to_json(ruta_salida_json, orient='records', indent=4)
    
    print("🚀 ¡ETL PIPELINE EJECUTADO CON ÉXITO DE EXTREMO A EXTREMO! 🎉\n")

if __name__ == "__main__":
    ejecutar_pipeline()
   