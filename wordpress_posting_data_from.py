import requests
import base64
json_data_url = 'https://jsonplaceholder.typicode.com/posts'
posts = requests.get(json_data_url).json()

wp_user = "NafisT"
wp_password = "tSKG GrFu KoYI oIKV kQUV wbOS"
wp_credential = f"{wp_user}:{wp_password}"
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization':f"Basic {wp_token.decode("utf-8")}"}

def slugify(text):
    slug_word = text.strip().replace(' ', '-')
    return slug_word

for post in posts:
    end_points = 'https://localhost/PythonWordpress/wp-json/wp/v2/posts'
    data = {
        'title': post['title'],
        'content': post['body'],
        'slug':slugify(post['title']),
        'status':'publish'
    }
    response = requests.post(end_points, headers=wp_headers, json=data, verify=False)
    print(response)
