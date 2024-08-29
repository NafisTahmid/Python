import base64
import requests
wp_user = "NafisT"
wp_password = "tSKG GrFu KoYI oIKV kQUV wbOS"
wp_credential = f'{wp_user}:{wp_password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
url = 'https://localhost/PythonWordpress/wp-json/wp/v2/posts'
data = {
    'title': 'This is awesome title two',
    'content': 'This is demo content new',
    'slug':'this-is-slug-two',
    'status':'publish'
}

response = requests.post(url, headers=wp_headers, json=data, verify=False)
print(response)