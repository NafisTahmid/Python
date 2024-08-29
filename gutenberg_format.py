from requests import post
import base64

def wpp(text):
    data = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return data
def slugify(text):
    slug_word = text.strip().replace(' ','-')
    return slug_word

def wpp_image(url):
    img_code = f'<!-- wp:image {{"id":119,"sizeSlug":"full","linkDestination":"none"}} --><figure class="wp-block-image size-full"><img src="{url}" alt="" class="wp-image-119"/></figure><!-- /wp:image -->'
    return img_code

wp_user = "NafisT"
wp_password = "tSKG GrFu KoYI oIKV kQUV wbOS"
wp_credential = f"{wp_user}:{wp_password}"
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

def post_wp(title, content, image_url, authorization, status="publish"):
    api_url = 'https://localhost/PythonWordpress/wp-json/wp/v2/posts'
    
    # Combine image block with content
    combined_content = f"{wpp_image(image_url)}\n{content}"

    data = {
        'title': title,
        'content': combined_content,  # Include the image directly in the content
        'status': status,  # Ensure the post status is included (default is "publish")
    }
    
    res = post(api_url, json=data, headers=authorization, verify=False)
    print(res.status_code)
    print(res.json())  # Print the response for debugging

title = input("Please enter title")
content = input("Please enter content")
image_url = input("Please provide an image url")

post_wp(title, content, image_url, wp_headers)