import pickle

data = {"key": "value"}
with open('test.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('test.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
print(loaded_data)