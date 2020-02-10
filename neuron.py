import numpy

class Neuron:
    def __init__(self, activation=0, outs=None, is_output=False, name=None):
        self.activation = activation
        self.outs = outs

    def project_to(self, target_neuron, distance=1):
        self.outs.append((target_neuron, distance))

    def print_outs(self):
        print(self.outs)


def neurize_param(normed_param):
    signbit = 1 if normed_param < 0 else 0

    return [signbit, abs(normed_param)]