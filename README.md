# Ultimage 1.0
<img src="https://raw.githubusercontent.com/PCP2024/ultimage/main/demodata/logo.png" height="100" width="100">

## Overview
Ultimage is a command-line image processing software that allows users to perform basic image manipulations. The software can load images, apply specified operations, and optionally display or save the processed images.

### Features
- Rotation
- Mirroring
- Cropping
- Scaling
- Text overlay

## Installation
Ultimage can be installed either by cloning this repository and installing dependencies, or using Docker.
### Using Python
To install Ultimage using Python, ensure you have Python installed. Clone the repository and install the required dependencies.
```
git clone https://github.com/PCP2024/ultimage.git
cd ultimage
pip install -r requirements.txt
```

### Using Docker
Ultimage is also on [Docker Hub](https://hub.docker.com/r/gerapago/ultimage) and can be installed and run using Docker.

1. Ensure you have Docker installed on your system. If not, download and install it from [here](https://www.docker.com/get-started/).

2. Pull the Docker image:
```
docker pull gerapago/ultimage:latest
```
3. Run the Docker container interactively
```
docker run -it ultimage /bin/bash
```

## Usage 
Ultimage provides a command-line interface with various options to process images. Below are the available arguments and their descriptions:
```
main_ultimage.py [-h] [-v] [-n] [-s] [-i IN_PATH] [-o OUT_PATH] [-r ANGLE] [-m {-1,1}] [-c X0 Y0 X1 X1] [-rs SCALE] [-t TEXT X Y COLOR SIZE]
```

### Arguments
- `-v`, `--version`: Show the software version.
- `-n`, `--noshow`: Stops the display of the image.
- `-s`, `--save`: Saves the image to the output directory.
- `-i IN_PATH`, `--in_path IN_PATH`: The path to the image file.
- `-o OUT_PATH`, `--out_path OUT_PATH`: The path to the output file.
- `-r ANGLE`, `--rotate ANGLE`: The angle of rotation in degrees.
- `-m {-1,1}`, `--mirror {-1,1}`: The axis of mirroring (-1 for vertical, 1 for horizontal).
- `-c [X0 X1 Y0 Y1]`, `--crop [X0 X1 Y0 Y1]`: The coordinates of the crop region in the form [x_start, x_end, y_start, y_end].
- `-rs SCALE`, `--scale SCALE`: The factor to rescale the image by (out of 1).
- `-t [TEXT X Y COLOR SIZE]`, `--text [TEXT X Y COLOR SIZE]`: The text to overlay on the image, the coordinates, and font size and color in the form ['text', left, top, color, size].

## Examples
- Display version
```
python3 main_ultimage.py -v
```
- Rotate an image by 45 degrees and display it
```
python3 main_ultimage.py -i demodata/demo.jpg -r 45
```
- Rotate an image by 45 degrees and save it without displaying
```
python3 main_ultimage.py -i demodata/demo.jpg -o demodata/output.jpg -r 45 -n
```
- Crop an image to the upper leftmost 100 x 200 pixels and prevent it from displaying
```
python3 main_ultimage.py -i demodata/demo.jpg --crop 0 100 0 200 -n
```
- Rescale an image to 50% of its original size and add text overlay
```
python3 main_ultimage.py -i demodata/demo.jpg -rs 0.5 -t 'Hello, world' 30 15 '#fff' 25
```

### Docker Examples
- Display version
```
docker run ultimage -v
```
- Run interactively, rotate an image by 45 degrees, and save it
```
docker run -it ultimage /bin/bash
root@dc7b867b4c58:/app#>> python3 main_ultimage.py -i demodata/demo.jpg -r 45 -o demodata/output.jpg
```
### Exporting images generated when running via Docker
To export images generated when running ultimage via Docker:
1. Run the Docker container:
```
docker run -it ultimage /bin/bash
```
2. Process an image (without displaying it)
```
python3 main_ultimage.py -rs 2 -i input.jpg -o output.jpg -n
```
3. Find the container ID with `docker ps -a`
4. Commit the container to a new image and run a new temporary container:
```
docker commit friendly_fermat temp_image
docker run -it --rm --name temp_container temp_image /bin/bash
```
5. In a new terminal window, copy the file from the temporary container to the host:
```
docker cp temp_container:/full/path/to/file /path/to/host/destination
```

## License
This project is licensed under the GNU Affero General Public License v3.0. See [LICENSE](https://github.com/PCP2024/ultimage/blob/main/LICENSE) for more details.

## Authors
Ultimage was developed by Joana Seabra and Gerardo Parra, with contributions from Benjamin Stephenson. This project was part of the BCCN SoSe 2024 Programming Course and Project (PCP) with instructors Dr. Matthias Haberl and Dr. Henning Sprekeler. 
