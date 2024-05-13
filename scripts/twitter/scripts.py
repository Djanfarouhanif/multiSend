import requests 
import base64
from urllib.parse import urlencode

endpoint = "https://api.linkedin.com/v2/shares"
url = "https://www.linkedin.com/oauth/v2/authorization"

def generate_authorization_url(client_id, redirect_uri, state):
    params = {
        'response_type':"code",
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'state': state
    }

    autho_url = "https://www.linkedin.com/oauth/v2/authorization?" +urlencode(params)

    return autho_url

client_id = "78p12y4agb23q6"
redirect_uri = "https://hanifcode.pythonanywhere.com/"
state = "aRandomString"
auth_url = generate_authorization_url(client_id, redirect_uri, state)
print(auth_url)

post_data = {
     "author":"urn:li:person:78r7fo4kbu8ke5",
    "text": "Si je vois un animal qui vole comme un cannard qui nage, comme un cannard et qui cancanne comme un cannard alors cet animale est un canard",
     "visibility": {
         "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
     }
 }

headers = {
    "Authorization": "Bearer ********** Mon_JETON *********",
     "Content-Type": "application/json"
 }


response = requests.post(endpoint, json=post_data, headers=headers)

if response.status_code == 201:
    print('POST LinkedIn crée avec succes')
else:
    print("echec de la creations du post LinkedIn ", response.text)