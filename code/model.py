import pickle
import os
from dotenv import load_dotenv
import pandas as pd

_ = load_dotenv()

path_model = os.getenv("DATASET_MODEL")

print(path_model)
df_model = pd.read_csv(path_model)

# class Model:
#     def __init__(self, model_path: str):
#         with open(model_path, 'rb') as f:
#             self.model = pickle.load(f)

#     def predict(self, data):
#         return self.model.predict(data)

# Inicializa el modelo
#model = Model('DATASET_MODEL')


