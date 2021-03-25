from __future__ import print_function
import numpy as np
from load import MNIST
from random import choice, randint


class digits_Sequencer(object):

    def __init__(self, path='data', name_img='images.byte',name_lbl='labels.byte'):
        self.dataset = MNIST(path, name_img, name_lbl)
        self.images, self.labels = self.dataset.load()
        self.label_map = [[] for i in range(10)]
        self.__generate_label_map()

    def __calculate_uniform_spacing(self, size_sequence, minimum_spacing, maximum_spacing,total_width, image_width=28):
        if size_sequence <= 1:
            return 0
        ''' Pick random value from given space range '''
        allowed_spacing = float(randint(minimum_spacing,maximum_spacing))
        #allowed_spacing = (total_width - size_sequence * image_width) / ((size_sequence - 1) * 1.0)
        if not allowed_spacing.is_integer() or allowed_spacing < minimum_spacing or allowed_spacing > maximum_spacing:
            print("Allowed spacing is invalid for the given set of values, Please increase total_width or tweak your min/max spacing value.")
            print("Either it meet below conditions:")
            print(" - allowed_spacing is a decimal value.")
            print(" - allowed_spacing < min_spacing("+ str(minimum_spacing) +")")
            print(" - allowed_spacing > max_spacing("+ str(maximum_spacing) +")")
            print("Allowed_spacing value:" + str(allowed_spacing))
            exit()
        print("Allowed_spacing value:" + str(allowed_spacing) +" is acceptable, proceeding.")
        return int(allowed_spacing)

    def __generate_label_map(self):
        num_labels = len(self.labels)
        for i in range(num_labels):
            self.label_map[self.labels[i]].append(i)

    def __select_random_label(self, label):
        if len(self.label_map[label]) > 0:
            return choice(self.label_map[label])
        else:
            print("No images for the number " + str(label) +
                  " is available. Please try with a different number.")
            exit()

    def generate_image_sequence(self, sequence, minimum_spacing, maximum_spacing,
                                total_width, image_height=28):
        sequence_length = len(sequence)
        allowed_spacing = self.__calculate_uniform_spacing(sequence_length, minimum_spacing,
                                                           maximum_spacing, total_width)
        spacing = np.ones(image_height * allowed_spacing,
                          dtype='float32').reshape(image_height, allowed_spacing)
        random_label_number = self.__select_random_label(sequence[0])
        image = self.images[random_label_number]
        for i in range(1, sequence_length):
            if i < sequence_length:
                image = np.hstack((image, spacing))
            random_label_number = self.__select_random_label(sequence[i])
            image = np.hstack((image, self.images[random_label_number]))
        return image
