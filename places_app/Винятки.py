import json

json_text = """
{
    "name": "Anna",
    "age": 24,
}
"""

try:
    data = json.loads(json_text)
    print("Рядок декодовано:", data)
except json.JSONDecodeError as error:
    print("Рядок не є валідним JSON")