import requests
import json


body = {
    "name": "Bernardo da Cunha Borges",
    "mail": "bernardodcborges@gmail.com",
    "github_url": "https://github.com/BernardoCunhaB/TraineeLatam/tree/master",
    "api_url": "https://BernardoCunhaB.api"
}

# Convert the dictionary to a JSON string
json_body = json.dumps(body)

# URL to send the POST request
url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/software-engineer"

# Send the POST request
response = requests.post(url, data=json_body)

# Get the response
print(response.json())