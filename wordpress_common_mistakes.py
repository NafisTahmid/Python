import requests
import base64

wp_user = "NafisT"
wp_password = "tSKG GrFu KoYI oIKV kQUV wbOS"
wp_credential = f"{wp_user}:{wp_password}"
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {"Authorization": f"Basic {wp_token.decode('utf-8')}"}

url = "https://localhost/PythonWordpress/wp-json/wp/v2/posts"


def slugify(text):
    code = text.strip().replace(' ', '-')
data = {
    'title': 'This is the title',
    'content': 'Content goes here',
    'slug': slugify('title'),
    'status':'publish'
}

res = requests.post(url, json = data, headers=wp_headers, verify=False)
print(res.status_code)
print(res.json())