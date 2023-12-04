import requests

endpoint = "http://localhost:8000/api/products/1/update/"  #http://127.0.0.1:8000/

data = {
    "title":"Hello World again",
    "price": 25.00
}
get_response = requests.put(endpoint, json=data)

print(get_response.json())