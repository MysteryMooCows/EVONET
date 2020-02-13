import gym
import numpy
from neuron import Neuron
from neuron import neurize_param
from network import Network

env = gym.make("CartPole-v1")
observation = env.reset()

print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)

max_pos, max_vel, max_angle, max_angle_rate = env.observation_space.high
min_pos, min_vel, min_angle, min_angle_rate = env.observation_space.low


def norm_pos(pos):  # return range is [-1, 1]
    pos_range = max_pos - min_pos
    return (pos / (pos_range / 2)) * 2


def norm_vel(vel, horiz_scale=1):  # return range is [-1, 1]
    return numpy.tanh(vel * horiz_scale)


def norm_angle(angle):  # return range is [-1, 1]
    angle_range = max_angle - min_angle
    return (angle / (angle_range / 2)) * 2


def norm_angle_rate(angle_rate, horiz_scale=1):  # return range is [-1, 1]
    return numpy.tanh(angle_rate * horiz_scale)


in_neurons = list()
for i in range(env.observation_space.shape[0]):
    in_neurons.extend([Neuron(is_input=True), Neuron(is_input=True)])

network = Network(in_neurons=in_neurons, out_neurons=[Neuron(is_output=True, name="Left"), Neuron(is_output=True, name="Right")])


for in_neuron in network.in_neurons:
    print(in_neuron.outs)


network.draw_network()


for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    pos, vel, angle, angle_rate = observation

    normed_inputs = [norm_pos(pos), norm_vel(vel, horiz_scale=1), norm_angle(angle), norm_angle_rate(angle_rate, horiz_scale=1)]
    neurized_input_activations = list()

    for normed_param in normed_inputs:
        neurized_input_activations.extend(neurize_param(normed_param))

    network.update_inputs(neurized_input_activations)

    if done:
        observation = env.reset()
        break
    else:
        print(normed_inputs)
        network.print_ins()

env.close()
