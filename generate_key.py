#!/usr/bin/python3
import argparse
from random import random
from random import seed

from PIL import Image

# Parse commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', dest='verbose', help="verbose output", action='store_true')
parser.add_argument('-s', '--show', dest='show', help="show result", action='store_true')
parser.add_argument('-p', '--probability', dest='probability', help="Probability for a black pixel", type=float,
                    default='0.5')
parser.add_argument('size_x', type=int, help="Width")
parser.add_argument('size_y', type=int, help="Height")
parser.add_argument('file_output', help="Output image")
args = parser.parse_args()

# seed random number generator
seed(1)

key = Image.new('1', (args.size_x, args.size_y))  # create a new black image
pixels = key.load()  # create the pixel map
for i in range(key.size[0]):  # for every pixel:
    for j in range(key.size[1]):
        if random() > args.probability:
            pixels[i, j] = 255

# Save result
try:
    key.save(args.file_output)
except:
    print("Can't write to file {}!".format(args.file_output))

# Display resulting image
if args.show:
    key.show()

exit()
