from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import json
from dotenv import load_dotenv
load_dotenv()

path_json_output = os.getenv("DATASET_JSON")

if path_json_output.startswith("code\\"):
    path_json_output = path_json_output[5:]

# Convertir a ruta absoluta
path_json_output = os.path.abspath(path_json_output)
print(f"Ruta absoluta corregida del archivo JSON: {path_json_output}")

if not os.path.exists(path_json_output):
    print(f"Archivo NO encontrado en la ruta: {path_json_output}")
else:
    print(f"Archivo encontrado en la ruta: {path_json_output}")

app = FastAPI()

@app.get("/")
async def get_json():
    if not os.path.exists(path_json_output):
        raise HTTPException(status_code=404, detail="Archivo JSON no encontrado")
    
    try:
        with open(path_json_output, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error al leer el archivo JSON")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")

    return JSONResponse(content=data)

@app.post("/dataset")
async def upload_dataset(file: UploadFile = File(...)):
    # Guardar el archivo JSON recibido
    file_path = path_json_output
    try:
        with open(file_path, 'w') as f:
            content = await file.read()
            f.write(content.decode('utf-8'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {e}")

    return {"filename": file.filename, "detail": "File uploaded successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

