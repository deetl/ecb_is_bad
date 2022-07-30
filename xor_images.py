#!/usr/bin/python3
# (c) 2022 Alexander Schinner

import argparse

from PIL import Image, ImageChops

# Parse commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', dest='verbose', help="verbose output", action='store_true')
parser.add_argument('-s', '--show', dest='show', help="show result", action='store_true')
parser.add_argument('-a', '--all', dest='all', help="Paste all images (inpout, padded key, tresult) to output file",
                    action='store_true')
parser.add_argument('file_input', help="Source image")
parser.add_argument('file_key', help="Key image")
parser.add_argument('file_output', help="Output image")
args = parser.parse_args()

# Open images
try:
    image_input = Image.open(args.file_input).convert("1")
except:
    print("Can't read file {}!".format(args.file_input))
    exit(1)

try:
    image_key = Image.open(args.file_key).convert("1")
except:
    print("Can't read file {}!".format(args.file_key))
    exit(1)

i_width, i_height = image_input.size
k_width, k_height = image_key.size

if args.verbose:
    print("Input Dimension: {}x{}".format(i_width, i_height))
    print("Key Dimension  : {}x{}".format(k_width, k_height))

# Padding key
real_key = image_input.copy()
x_pos = 0
while x_pos < i_width:
    y_pos = 0
    while y_pos < i_height:
        real_key.paste(image_key, (x_pos, y_pos))
        y_pos = y_pos + k_height
    x_pos = x_pos + k_width

# XOR input image and padded key
result = ImageChops.logical_xor(image_input, real_key)

if args.all:
    img = Image.new("1", (i_width * 3 + 20, i_height))
    img.paste(image_input, (0, 0))
    img.paste(real_key, (i_width + 10, 0))
    img.paste(result, (2 * i_width + 20, 0))
    result = img

# Save result
try:
    result.save(args.file_output)
except:
    print("Can't write to file {}!".format(args.file_output))

# Display resulting image
if args.show:
    result.show()

exit()
