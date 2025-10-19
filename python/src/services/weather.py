import os
import requests
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener la API Key de las variables de entorno
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_HOST = os.getenv("WEATHER_API_HOST")


def fetch_data_from_api_weather(lat: str, lon: str):
    """
    Realiza una solicitud GET a la URL especificada y procesa la respuesta.
    """
    WEATHER_API_URL = f"{WEATHER_API_HOST}?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    print(f"[*] Haciendo solicitud GET a: {WEATHER_API_URL}")
    
    try:
        # 1. Realizar la solicitud HTTP GET
        # La solicitud es síncrona: el programa espera aquí hasta que la API responde.
        response = requests.get(WEATHER_API_URL)
        
        # 2. Verificar el estado de la respuesta
        # .raise_for_status() lanzará una excepción (HTTPError) para códigos de error 4xx/5xx
        response.raise_for_status() 
        
        # 3. Extraer y retornar los datos JSON
        # .json() automáticamente parsea la respuesta de texto a un diccionario/lista de Python
        data = response.json()
        
        return data

    except requests.exceptions.HTTPError as err_http:
        # Manejo de errores HTTP (404 Not Found, 500 Internal Server Error, etc.)
        print(f"[ERROR HTTP]: La API devolvió un error. Código: {response.status_code}")
        print(f"Detalles: {err_http}")
        return None
        
    except requests.exceptions.ConnectionError:
        # Manejo de errores de conexión (ej. no hay internet, DNS falló)
        print("[ERROR CONEXIÓN]: No se pudo conectar a la URL. Verifique su conexión y la URL.")
        return None
        
    except requests.exceptions.Timeout:
        # Manejo de errores de timeout
        print("[ERROR TIMEOUT]: La solicitud expiró.")
        return None
        
    except requests.exceptions.RequestException as e:
        # Manejo de cualquier otro error de requests
        print(f"[ERROR INESPERADO]: Ocurrió un error en la solicitud: {e}")
        return None
