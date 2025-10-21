
import pandas as pd
from pathlib import Path

def read_orders_csv(file_name: str = "orders.csv"):
    """
    Lee un archivo CSV del directorio actual y lo carga en un DataFrame de Pandas.

    Args:
        file_name (str): El nombre del archivo CSV a leer. Por defecto, 'orders.csv'.

    Returns:
        pd.DataFrame | None: El DataFrame con los datos de las órdenes, 
                             o None si el archivo no se encuentra o hay un error.
    """
    # 1. Definir la ruta del archivo (asume que está en el mismo directorio)
    file_path = Path.cwd() / file_name  # Path.cwd() obtiene el directorio de trabajo actual
    
    print(f"[*] Intentando leer el archivo: {file_path}")
    
    try:
        # 2. Leer el archivo CSV usando Pandas
        df = pd.read_csv(file_path,sep=r"\s*[;,]\s*",engine="python")
        
        df_sorted = df.sort_values(by="Rep").reset_index(drop=True)
        
        # 3. Reportar éxito
        print(f"[ÉXITO] Archivo '{file_name}' cargado correctamente.")
        print(f"[*] Filas leídas: {len(df_sorted)}. Columnas: {len(df_sorted.columns)}.")
        
        return df_sorted
        
    except FileNotFoundError:
        # Manejo de error si el archivo no existe
        print("-" * 50)
        print(f"[ERROR] Archivo NO encontrado: '{file_name}'")
        print(f"[SUGERENCIA] Asegúrate de que el archivo exista en la ruta: {file_path}")
        return None
        
    except pd.errors.EmptyDataError:
        # Manejo de error si el archivo existe pero está vacío
        print(f"[ERROR] Archivo encontrado, pero está vacío: '{file_name}'")
        return None
        
    except Exception as e:
        # Manejo de otros errores (ej. problemas de codificación)
        print(f"[ERROR INESPERADO] Ocurrió un error al leer el CSV: {e}")
        return None