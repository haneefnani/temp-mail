import requests
import json

from useful_functions import *


api_key = open(r'C:\Users\haneef\Documents\Credentials\temp_mail_api.txt').read()

mail_hash = computeMD5hash('thomas@rcmails.com')
url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/" + mail_hash + "/"

headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

response = requests.request("GET", url, headers=headers)

data = response.json()

print(data)

