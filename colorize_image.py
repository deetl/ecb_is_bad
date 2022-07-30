#!/usr/bin/python3
# (c) 2022 Alexander Schinner

import argparse

from PIL import Image

# Parse commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', dest='verbose', help="verbose output", action='store_true')
parser.add_argument('-s', '--show', dest='show', help="show result", action='store_true')
parser.add_argument('file_input', help="Source image")
parser.add_argument('file_output', help="Destination image")
parser.add_argument('red', help="Red (0-255)", type=int)
parser.add_argument('green', help="Green (0-255", type=int)
parser.add_argument('blue', help="Green (0-255", type=int)
args = parser.parse_args()

# Open images
try:
    image_input = Image.open(args.file_input).convert("1")
except:
    print("Can't read file {}!".format(args.file_input))
    exit(1)

i_width, i_height = image_input.size

if args.verbose:
    print("Input Dimension: {}x{}".format(i_width, i_height))

# Colored output image
image_output = Image.new("RGB", (i_width, i_height), (args.red, args.green, args.blue))
pixels_input = image_input.load()  # create the pixel map
pixels_output = image_output.load()  # create the pixel map

# Set all white pixels to white
for i in range(i_width):  # for every pixel:
    for j in range(i_height):
        if pixels_input[i, j] > 0:
            pixels_output[i, j] = (255, 255, 255)

# Save file
try:
    image_output.save(args.file_output)
except:
    print("Can't write to file {}!".format(args.file_output))

# Display resulting image
if args.show:
    image_output.show()
