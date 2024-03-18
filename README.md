# Image Splitter

This is a simple command-line tool that splits an image into two halves. The left half of the image is saved in a directory named "left", and the right half is saved in a directory named "right". These directories are created in the parent directory of the original image's directory.

## Directory Structure

For example, if you have a directory structure like this:

- Wallpapers/
  - original/
    - image1.jpg

After running the script with `image1.jpg` as the input, the directory structure will look like this:

- Wallpapers/
  - original/
    - image1.jpg
  - left/
    - image1_left.jpg
  - right/
    - image1_right.jpg

The "left" directory contains the left half of the original image, and the "right" directory contains the right half.

## Requirements

- Python 3
- Pillow library

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:

```sh
pip install -r requirements.txt
```

## Usage
Run the script with the path to the image you want to split as an argument:

```sh
python main.py path_to_your_image.jpg
```

The script will create two new images in the "left" and "right" directories with the suffixes _left and _right added to the original file name.

## License
This project is licensed under the terms of the MIT license.