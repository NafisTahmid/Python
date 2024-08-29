def wpp(paragraph):
    code = f"<!-- wp:paragraph --><p>{paragraph}</p><!-- /wp:paragraph -->"
    return code

def wp_h2(h2):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{h2}</h2><!-- /wp:heading -->'

data = input("Please enter data: ")
# print(wp_h2(data))

def wp_button(button_text):
    code = f"""<!-- wp:buttons {{"layout":{{"type":"flex","justifyContent":"center"}}}} -->
    <div class="wp-block-buttons">
        <!-- wp:button -->
        <div class="wp-block-button">
            <a class="wp-block-button__link wp-element-button">{button_text}</a>
        </div>
        <!-- /wp:button -->
    </div>
    <!-- /wp:buttons -->"""
    return code


print(wp_button(data))