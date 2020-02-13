import numpy

class Neuron:
    def __init__(self, activation=0, outs=list(), is_output=False, is_input=False, name=None):
        self.activation = activation
        self.outs = outs
        self.is_output = is_output
        self.name = name
        self.is_drawn = False

    def project_to(self, target_neuron, distance=1):
        self.outs.append((target_neuron, distance))

    def print_outs(self):
        print(self.outs)


def neurize_param(normed_param):
    signbit = 1 if normed_param < 0 else 0

    return [signbit, abs(normed_param)]