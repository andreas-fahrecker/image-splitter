import argparse
import os

from PIL import Image


def prepare_file_paths(image_path):
    # Get the parent directory of the original image
    parent_directory = os.path.dirname(os.path.dirname(image_path))

    # Prepare the file paths for the split images
    base_filename, ext = os.path.splitext(os.path.basename(image_path))
    left_image_path = os.path.join(
        parent_directory, "left", base_filename + "_left" + ext
    )
    right_image_path = os.path.join(
        parent_directory, "right", base_filename + "_right" + ext
    )

    return left_image_path, right_image_path


def is_image_split(image_path):
    # Prepare the file paths for the split images using the function
    left_image_path, right_image_path = prepare_file_paths(image_path)

    # Check if the split images exist
    return os.path.exists(left_image_path) and os.path.exists(right_image_path)


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

    # Prepare the file paths for the split images using the function
    left_image_path, right_image_path = prepare_file_paths(image_path)

    # Save the split images
    img1.save(left_image_path)
    img2.save(right_image_path)


def split_images_in_directory(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Filter the list to get only the image files
    image_files = [f for f in files if f.endswith(".jpg") or f.endswith(".png")]

    # Split each image
    for image_file in image_files:
        image_path = os.path.join(directory, image_file)
        if not is_image_split(image_path):
            split_image(image_path)


def main():
    parser = argparse.ArgumentParser(
        description="Split an image or all images in a directory into two halves"
    )
    parser.add_argument("--image_path", help="Path to the image file")
    parser.add_argument("--directory", help="Path to the directory containing images")
    args = parser.parse_args()

    if args.image_path:
        if is_image_split(args.image_path):
            print("The image is already split.")
        else:
            split_image(args.image_path)
    elif args.directory:
        split_images_in_directory(args.directory)
    else:
        print("Please provide either --image_path or --directory")


if __name__ == "__main__":
    main()
