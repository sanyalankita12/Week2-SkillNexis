import json


with open(r"C:\Users\Ishit\PycharmProjects\PythonProject2\assignments\data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Print formatted JSON
print(json.dumps(data, indent=4, ensure_ascii=False))