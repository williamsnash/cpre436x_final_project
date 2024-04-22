"""
This script is used to hide text data into an image file.
Basic steganography is used to hide the data into the image.
"""
import argparse


def setup():
    """
    Setups the argument parser for the script
    """
    parser = argparse.ArgumentParser(description='Image Steganography Creator')
    parser.add_argument(
        "--image", help='Path image where the data will be hidden')
    parser.add_argument("-o", "--out_image", help='New image path')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file", help="Path to txt file containing the data to hide in the image")
    group.add_argument(
        "-t", "--text", help="Add text directly to hide in the image, without a file")
    group.add_argument("-r", "--retrieve",
                       help="Retrieve the data from the image")

    args = parser.parse_args()
    if args.retrieve:
        return args
    if args.image is None:
        print("Please provide the path to the image")
        exit()
    if args.text is None and args.file is None:
        print("Please provide the text or file to hide in the image")
        exit()
    return args


def read_file(path: str, mode: str = 'rb'):
    """
    Read the file as binary data and return it

    :param str path: Path to the file
    :return bytes: Binary data of the file
    """
    with open(path, mode=mode) as f:
        data = f.read()
    return data


def retrieve_data(path: str):
    """
    Retrieve the data from the image file

    :param str path: Path to the file
    """
    file = read_file(path).hex()

    offset = file.rindex('ffd9') + 4
    text = bytearray.fromhex(file[offset:]).decode()
    print(f"Message: {text}")


def steganography(image_path: str, image_data: str, text_data: str):
    """
    Combine the image data and text data and write it into a new image file

    :param str image_path: Path to the image
    :param str image_data: Image data
    :param str text_data: Text to write into the image
    """
    new_data = image_data + text_data
    with open(image_path, 'wb') as image:
        image.write(new_data)


if __name__ == "__main__":
    args = setup()

    if args.file or args.text:
        image_data = read_file(args.image)

        if args.file:
            text_data = f"\n{read_file(args.file, mode='r')}"
            text_data = bytes(text_data, 'utf-8')
        elif args.text:
            text_data = bytes(f"\n{args.text}", 'utf-8')

        if args.new_image:
            steganography(args.new_image, image_data, text_data)
        else:
            steganography(args.image, image_data, text_data)

    elif args.retrieve:
        retrieve_data(args.retrieve)
