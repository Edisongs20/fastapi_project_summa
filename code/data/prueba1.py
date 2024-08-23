from dotenv import load_dotenv
import os
import json

load_dotenv()

# Ajusta la ruta si detecta el problema del duplicado
path_json_output = os.getenv("DATASET_JSON")

if path_json_output.startswith("code\\"):
    path_json_output = path_json_output[5:]  # Eliminar "code\\"

# Convertir a ruta absoluta
path_json_output = os.path.abspath(path_json_output)
print(f"Ruta absoluta corregida del archivo JSON: {path_json_output}")

if not os.path.exists(path_json_output):
    print(f"Archivo NO encontrado en la ruta: {path_json_output}")
else:
    print(f"Archivo encontrado en la ruta: {path_json_output}")

# Leer el archivo y verificar si es un JSON válido
try:
    with open(path_json_output, 'r') as file:
        data = json.load(file)
    print("Archivo JSON válido")
except json.JSONDecodeError as e:
    print(f"Error en la estructura del archivo JSON: {e}")
except Exception as e:
    print(f"Otro error al leer el archivo: {e}")
