import numpy

class Neuron:
    def __init__(self, activation=0, outs=list(), is_output=False, is_input=False, pos=(0, 0, 0), name=None):
        self.activation = activation
        self.outs = outs
        self.is_output = is_output
        self.is_input = is_input
        self.pos = pos
        self.name = name
        self.is_drawn = False

    def project_to(self, target_neuron):
        self.outs.append(target_neuron)

    def print_outs(self):
        print(self.outs)


def neurize_param(normed_param):
    signbit = 1 if normed_param < 0 else 0

    return [signbit, abs(normed_param)]