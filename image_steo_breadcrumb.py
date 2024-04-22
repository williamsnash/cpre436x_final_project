"""
This is my totally really work scripts, no need to keep reading
"""
import sys


def read_file(path: str, mode: str = 'rb'):
    with open(path, mode=mode) as f:
        data = f.read()
    return data


def steganography(image_path: str, image_data: str, text_data: str):
    new_data = image_data + text_data
    with open(image_path, 'wb') as image:
        image.write(new_data)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Please provide the image file and path of the text file to hide in the image")
        exit()
    image_path = sys.argv[1]
    image_data = read_file(image_path)

    text_path = sys.argv[2]
    text_data = f"\n{read_file(text_path, mode='r')}"
    text_data = bytes(text_data, 'utf-8')

    steganography(image_path, image_data, text_data)
