# membaca json
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data[0]["nama"])

# menulis json
data = {"model": "RandomForest", "accuracy": 0.92, "trained": True}

with open("model_info.json", "w") as file:
    json.dump(data, file, indent=4)
