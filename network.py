from mpl_toolkits import mplot3d
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
                in_neuron.project_to(out_neuron)

    def update_inputs(self, activations):
        for i in range(len(activations)):
            self.in_neurons[i] = activations[i]


    def print_ins(self):
        out_str = "Inputs: "

        for neuron in self.in_neurons:
            out_str += str(neuron) + " "

        print(out_str)

    def draw_network(self):
        '''
        dot = Digraph()
        dot.node('A', 'A')
        dot.node('B', 'B')
        dot.node('C', 'C')
        dot.edges(['AB', 'AB', 'AB', 'BC', 'BA', 'CB'])

        print(dot.source)
        dot.render("graph.png", view=True)
        '''

        fig = plt.figure()
        ax = plt.axes(projection='3d')

        xdata = []
        ydata = []
        zdata = []
        cdata = []

        neurons = self.in_neurons.copy()
        neurons.extend(self.out_neurons)

        print(len(neurons))

        for neuron in neurons:
            xdata.append(neuron.pos[0])
            ydata.append(neuron.pos[1])
            zdata.append(neuron.pos[2])
            if neuron.is_input:
                cdata.append('blue')
            elif neuron.is_output:
                cdata.append('red')

        ax.scatter3D(xdata, ydata, zdata, color=cdata)
        plt.show()


