import os
from PIL import Image

image = Image.open("C:/Users/suche/Downloads/client-server.jpg")

new_image = image.resize((500, 500))
new_image = new_image.rotate(90)
new_image = new_image.convert('L')

# new_image.show()
image.close()



image_dir = 'c:/Users/suche/Downloads/test_image'

for name in os.listdir(image_dir):
    if name.endswith(('.png', '.jpeg', '.jpg')):
        image_path = os.path.join(image_dir, name)

        print(image_path)
        # print(os.path.isfile(image_path))
        image = Image.open(image_path) # dá se použít s context managerem with
        print(image.size)
        image.close()
        if image.size[0] > 1000:
            os.remove(image_path)