import requests 

endpoint = "https://api.linkedin.com/v2/shares"

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