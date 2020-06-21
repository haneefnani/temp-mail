import requests

api_key = open(r'C:\Users\haneef\Documents\Credentials\temp_mail_api.txt').read()


url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/domains/"

headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
}

response = requests.request("GET", url, headers=headers)

print(response.text())
