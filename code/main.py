from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import os

app = FastAPI() 

# Cargar el modelo de manera segura
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
              
# Obtener la ruta del modelo desde una variable de entorno o usar un valor por defecto
model_path = os.getenv('DATASET_MODEL', 'trained_model.pkl')

try:
    model = Model(model_path)
except RuntimeError as e:
    print(f"Error loading model: {e}")
    model = None

# Define las solicitudes y respuestas
class PredictRequest(BaseModel):
    feature1: float
    feature2: float

# Añade aquí todas las características necesarias
class PredictResponse(BaseModel):
    prediction: str
    
#metodo post    
@app.post("/", response_model=PredictResponse)
async def predict(request: PredictRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not available")
    
    try:
        # Preprocesa los datos si es necesario
        data = [request.feature1, request.feature2]
        prediction = model.predict([data])
        return PredictResponse(prediction=str(prediction[0]))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

#metodo get
@app.get("/") 
async def root():     
    
    return {"Servidor corriendo FastAPI"} 
    
if __name__ =="__main__":     
    import uvicorn    
    uvicorn.run(app, host="0.0.0.0", port=8000)