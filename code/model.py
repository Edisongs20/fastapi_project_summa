import os
import pickle
import json
import pandas as pd
from dotenv import load_dotenv
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

# Obtener las rutas desde las variables de entorno
path_dataset_model = os.getenv("DATASET_MODEL")
path_json_output = os.getenv("DATASET_JSON")

# Validación de variables de entorno
if path_dataset_model is None:
    raise ValueError("La variable de entorno 'DATASET_MODEL' no está definida.")
if path_json_output is None:
    raise ValueError("La variable de entorno 'DATASET_JSON' no está definida.")

# Función para leer el dataset
def read_dataset(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo en la ruta {path} no existe.")
    try:
        df = pd.read_csv(path)
        logger.info("Dataset leído correctamente.")
        return df
    except Exception as e:
        logger.error(f"Error al leer el archivo: {e}")
        raise

# Clase del modelo
class Model:
    def __init__(self, model_path: str):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"El archivo del modelo en la ruta {model_path} no existe.")
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        logger.info("Modelo cargado correctamente.")

    def predict(self, data):
        return self.model.predict(data)

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función para convertir DataFrame a JSON
def dataframe_to_json(df: pd.DataFrame, output_path: str):
    try:
        # Convertir DataFrame a JSON con el formato deseado -- pendiente para modificar el formato
        json_data = df.to_json(orient='records', lines=False)
        json_data = "[" + json_data.replace("}{", "},{") + "]"

        # Guardar el JSON en el archivo de salida
        with open(output_path, 'w') as f:
            f.write(json_data)

        logger.info(f"Archivo JSON guardado en: {output_path}")
    except Exception as e:
        logger.error(f"Error al convertir DataFrame a JSON: {e}")
        raise

# Leer el dataset
df_dataset_model = read_dataset(path_dataset_model)

# Convertir el DataFrame a JSON
dataframe_to_json(df_dataset_model, path_json_output)
