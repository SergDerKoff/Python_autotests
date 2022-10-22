import requests

url = "https://petstore.swagger.io/v2/pet"
response = requests.post(url, json={
  "id": 5,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "puma",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

url = "https://petstore.swagger.io/v2/pet"
response = requests.put(url, json={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "grey",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/123")
print(response.text)