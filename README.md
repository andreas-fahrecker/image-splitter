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

### For Usage as a Windows Executable
You can either download a prebuilt executable from the releases section of the repository, or you can build it yourself the building instructions are further down the `README.md`

### For Usage as a Python Script

1. Clone this repository.
2. Install the required Python packages using pip:

```sh
pip install -r requirements.txt
```

## Usage

### As Windows Executable
You can run the program with either the path to a single image you want to split or a directory containing multiple images.

#### Single Image Mode
```sh
main.exe --image_path path_to_your_image.jpg
```
The program will create two new images in the "left" and "right" directories with the suffixes _left and _right added to the original file name.

#### Directory Mode
```sh
main.exe --directory path_to_your_directory
```

The program will iterate over all images in the directory, and for each image, it will create two new images in the "left" and "right" directories with the suffixes _left and _right added to the original file name.

### As a Python Script
You can run the script with either the path to a single image you want to split or a directory containing multiple images.

To split a single image:

```sh
python main.py --image_path path_to_your_image.jpg
```
The script will create two new images in the "left" and "right" directories with the suffixes _left and _right added to the original file name.

To split all images in a directory:

```sh
python main.py --directory path_to_your_directory
```

The script will iterate over all images in the directory, and for each image, it will create two new images in the "left" and "right" directories with the suffixes _left and _right added to the original file name.

## Build from Source

### Windows Executable

1. Clone this repository.
2. Navigate into the cloned repository.
```sh
cd image-splitter
```
3. Install the required Python packages.
```sh
pip install -r requirements.txt
```
4. Build the Executable with PyInstaller
```sh
pyinstaller --onefile --name image-splitter main.py
```

## License
This project is licensed under the terms of the MIT license.

## Source Code

The source code for this project is available on [Gitea](https://gitea.fahrecker.com/andreas-personal/image-splitter) and mirrored on [GitHub](https://github.com/andreas-fahrecker/image-splitter).