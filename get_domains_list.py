import requests

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/domains/"

headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': "a751637279msh471694ff49027bdp12e2d2jsn7c878ea74949"
}

response = requests.request("GET", url, headers=headers)

print(response.text())
