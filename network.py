import matplotlib.pyplot as plt
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

class Network:
    def __init__(self, in_neurons=list(), out_neurons=list()):
        self.in_neurons = in_neurons
        self.out_neurons = out_neurons

        for in_neuron in self.in_neurons:
            in_neuron.outs = list()  # why is this necessary?
            for out_neuron in self.out_neurons:
                in_neuron.project_to(out_neuron, distance=1)

    def update_inputs(self, activations):
        i = 0
        for neuron in self.in_neurons:
            neuron.activation = activations[i]
            i += 1

    def print_ins(self):
        out_str = "Inputs: "

        for neuron in self.in_neurons:
            out_str += str(neuron.activation) + " "

        print(out_str)

    def draw_network(self):
        dot = Digraph()
        dot.node('A', 'A')
        dot.node('B', 'B')
        dot.node('C', 'C')
        dot.edges(['AB', 'AB', 'AB', 'BC', 'BA', 'CB'])

        print(dot.source)
        dot.render("graph.png", view=True)
