from __future__ import print_function
from digits_sequencer_api import digits_Sequencer_API
import sys, ast


def main():
    arguments = list(sys.argv[1:])
    if len(arguments) == 3:
        digits = ast.literal_eval(arguments[0])
        spacing_range = eval(arguments[1])
        image_width = arguments[2]

        sequence, min_spacing = list(map(int, ast.literal_eval(arguments[0]))), int(spacing_range[0])
        max_spacing, image_width = int(spacing_range[1]), int(image_width)
        print("##########################")
        print("#     MNIST SEQUENCER    #")
        print("##########################")
        print("Inputs:")
        print(" - Digits:" + str(digits))
        print(" - spacing_range:" + str(spacing_range))
        print(" - image_width:" + str(image_width))
        api_object = digits_Sequencer_API()
        img_data = api_object.generate_mnist_sequence(sequence, spacing_range, image_width)
        api_object.save_image(img_data, sequence)
    else:
        print("Incorrect number of arguments.")
        print("Usage: python mnist_sequence_cli.py <sequence(no spaces) " +
              "min_spacing max_spacing image_width>")

if __name__ == "__main__":
    main()
