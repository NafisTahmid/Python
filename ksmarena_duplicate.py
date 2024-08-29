from requests import get, post
import base64
import json

wp_user = "NafisT"
wp_password = "tSKG GrFu KoYI oIKV kQUV wbOS"
wp_credential = f"{wp_user}:{wp_password}"
wp_token = base64.b64encode(wp_credential.encode())
wp_authorization = {"Authorization": f"Basic {wp_token.decode('utf-8')}"}

server_url = "https://mobile-phone-server.vercel.app/phones"
res = get(server_url)
print(res)

if res.status_code == 200:
    data = res.json()
    phones = data.get("RECORDS")

    def wp_paragraph(text):
        """
        This will generate wordpress gutenberg paragraph code
        """
        return f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->"

    def wp_heading_2_text(heading_two):
        """
        This will generate wordpress gutenberg heading 2 code
        """
        return f'<!-- wp:heading --><h2 class="wp-block-heading">{heading_two}</h2><!-- /wp:heading -->'

    def slugify(phone):
        code = phone.strip().replace(' ', '-')

    demo = {
        'name': 'phone',
        'brand': 'phone brand',
        'model': 'phone model'
    }

    def wp_table_dictionary(dictionary):
        """
        This will generate dictionary to wp table
        """
        codes = '<!-- wp:table --><figure class="wp-block-table"><table class="has-fixed-layout"><tbody>'

        for key, value in dictionary.items():
            tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
            codes += tr_data
        codes += '</tbody></table></figure><!-- /wp:table -->'
        return codes

    def media_from_url(img_src, phone_name):
        """
        This will return gutenberg image code
        :param img_src: image url
        :param phone_name: phone name
        :return: image code
        """
        codes = f'<!-- wp:image {{"sizeSlug":"large","align":"center"}} --><figure class="wp-block-image aligncenter size-large"><img src="{img_src}" alt="{phone_name}"/></figure><!-- /wp:image -->'

        return codes

    src = 'https://fdn2.gsmarena.com/vv/bigpic/ulefone-note-7t.jpg'
    name = 'Phone name'
    # print(media_from_url(src, name))

    # phone = phones[0]
    for phone in phones:

        phone_name = phone.get("name")
        specification_str = phone.get('specifications')
        specification = json.loads(specification_str)
        release_date = phone.get("released_at")
        chipset = phone.get("chipset")
        body = phone.get("body")
        os = phone.get("os")
        picture = phone.get("picture")
        # print(specification)
        title = f"{phone_name} price in Bangladesh"
        paragraph = f"{phone_name} has been released on {release_date}. It comes with {chipset} chipset. The body of this mobile is {body}"
    

        first_heading = f'{phone_name} brand data'
        first_dictionary = {
            'name':phone_name,
            'Release date':'released_at',
            'chipset': chipset,
            'body':body,
            'Operating system':os
        }

        post_paragraph = wp_paragraph(paragraph)
        image = media_from_url(picture, phone_name)
        wp_table_one = wp_table_dictionary(first_dictionary)
        wp_heading_one = wp_heading_2_text(first_heading)
        wp_table_two = wp_table_dictionary(specification)
        content = post_paragraph + image + wp_table_one + wp_heading_one + wp_table_two
        data = {
            'title':title,
            'content':content,
            'slug':slugify(title),
            'status':'publish',
            'category':'3'
        }
        url = "https://localhost/PythonWordpress/wp-json/wp/v2/posts"
        res = post(url, headers = wp_authorization, json = data, verify=False)
        print(res)
    
