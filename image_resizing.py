from PIL import Image


def resize_image(width, height):
    img = Image.open(
        "C:/Users/a459367/Desktop/python projects/rose-flower-flowers-red-rose.jpg")
    print(f'CurrentSize:{img.size}')
    resized_img = img.resize((width, height))
    resized_img.save('rose-flower-flowers-red-rose.jpg')
    img1 = Image.open("rose-flower-flowers-red-rose.jpg")
    img1.show()


w, h = map(int, input("Enter Width and Height").split(" "))
resize_image(w, h)
