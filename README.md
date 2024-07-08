# Description
Ultimage is an Image processing software developed for PCP SoSe2024
It allows the user to process and modify images using several functions: crop, blur, text overlay, etc.



# Installation instructions
Download the latest version of Ultimage available at https://github.com/PCP2024/ultimage
--

Can also be run on Docker.Docker image available at
https://hub.docker.com/repository/docker/jpseabra/ultimage/general



# Usage 

In your local IDE, you can use any of the Ultimage functions with
	maincmd.py [-h] [-n] [--angle ANGLE] [--coords COORDS COORDS COORDS COORDS] [--scale SCLALE] image_path {rotate, crop, resize}

Example: ultimage % python3 maincmd.py demodata/testimg.jpg crop -coords 2 100 4 200



- Basic Command Line Interface
Positional Arguments:
	image_path			The path to the image file
	{rotate, crop, resize} 		The operation to be performed

Options:
	-h, --help				Shows this help message and exits
	-n, --noshow				Stops the display of the image
	--angle AGLE				The angle of rotation in degrees (for rotate operation).
	-- coords COORDS COORDS COORDS COORDS	The coordinates of the crop region in the form [x_start, x_end, y_start, y_end] (only for crop operation).
	--scale SCALE				The scaling factor (only for resize operation)
 


#License: GNU Affero General Public License v3.0
https://github.com/PCP2024/ultimage/blob/main/LICENSE



# Version 0.1.4 
https://github.com/PCP2024/ultimage/blob/main/VERSION