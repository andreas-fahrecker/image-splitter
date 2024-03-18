import argparse
import os

from PIL import Image


def split_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Get the image size
    width, height = img.size

    # Calculate the width of each split
    split_width = width // 2

    img1 = img.crop((0, 0, split_width, height))
    img2 = img.crop((split_width, 0, width, height))

    # Get the parent directory of the original image
    parent_directory = os.path.dirname(os.path.dirname(image_path))

    # Create a new directory to save the split images
    left_dir = os.path.join(parent_directory, "left")
    right_dir = os.path.join(parent_directory, "right")

    # Create the directories if they don't exist
    os.makedirs(left_dir, exist_ok=True)
    os.makedirs(right_dir, exist_ok=True)

    # Prepare the file paths for the split images
    base_filename, ext = os.path.splitext(os.path.basename(image_path))
    img1_path = os.path.join(left_dir, base_filename + "_left" + ext)
    img2_path = os.path.join(right_dir, base_filename + "_right" + ext)

    # Save the split images
    img1.save(img1_path)
    img2.save(img2_path)


def main():
    parser = argparse.ArgumentParser(description="Split an image into two halves")
    parser.add_argument("image_path", help="Path to the image file")
    args = parser.parse_args()
    split_image(args.image_path)


if __name__ == "__main__":
    main()
