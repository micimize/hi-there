'''
Stub file
'''
from alphabet_scramble import AlphabetScramble
from translators.one_hot_vector import TensorTranslator
import tensorflow as tf
import numpy as np

scramble = AlphabetScramble([
        'hi              ',
        'hello           ',
        'well hi         ',
        'well hello      ',
        'hi there        ',
        'hello there     ',
        'well hi there   ',
        'well hello there'],
        rejection=
        'reeeeeeeeeeeeeee')

translator = TensorTranslator(scramble.alphabet)

def training_data(samples=100):
    inputs = []
    outputs = []
    for input, output in [scramble.scramble() for i in range(samples)]:
        inputs.append(translator.to_tensor(input))
        outputs.append(output) #translator.to_tensor(output))
    return { 'phrase': np.array(inputs) }, np.array(outputs)

def training_fn(samples=100, num_epochs=10):
    inputs, outputs = training_data(samples)
    return tf.contrib.learn.io.numpy_input_fn(
            inputs,
            y=outputs,
            num_epochs=num_epochs)

def regressor_model():
    return tf.contrib.learn.LinearRegressor(feature_columns=[
        tf.contrib.layers.real_valued_column('phrase', dimension=16) ])

def cluster_model():
    return tf.contrib.learn.KMeansClustering(len(scramble.alphabet) + 1)

def train(model, steps=100, **kwargs):
    model.fit(input_fn=training_fn(**kwargs), steps=steps)
    return model

def evaluate(model, steps, **kwargs):
    return model.evaluate(input_fn=training_fn(**kwargs), steps=steps)

def fractional_values(dictionary, fraction=10):
    return { k: int(v / 10) for k, v in dictionary.items() }

if __name__ == '__main__':
    params = dict(steps=10000, samples=10000, num_epochs=100000)
    model = train( cluster_model(), **params)
    performance = evaluate( model, **fractional_values(params, 10))
    print(performance, params)

