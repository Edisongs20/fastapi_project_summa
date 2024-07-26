from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import os

app = FastAPI() 

# Cargar el modelo de manera segura
class Model:
    def __init__(self, model_path: str):
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            raise RuntimeError(f"Model file not found: {model_path}")
        except pickle.PickleError:
            raise RuntimeError(f"Error loading model from: {model_path}")

    def predict(self, data):
        try:
            return self.model.predict(data)
        except Exception as e:
            raise RuntimeError("Error during prediction: " + str(e))
        
# Obtener la ruta del modelo desde una variable de entorno
model_path = os.getenv('DATASET_MODEL')

@app.get("/") 
async def root():     
    
    return {"Servidor corriendo FastAPI"} 
    
if __name__ =="__main__":     
    import uvicorn    
    uvicorn.run(app, host="0.0.0.0", port=8000)