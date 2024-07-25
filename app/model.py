import pickle

class Model:
    def __init__(self, model_path: str):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, data):
        return self.model.predict(data)

# Inicializa el modelo
model = Model('path/to/your/model.pkl')
