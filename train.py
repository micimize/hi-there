'''
Stub file
'''
from alphabet_scramble import AlphabetScramble
from tensor_translator import TensorTranslator
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
        tf.contrib.layers.real_valued_column('phrase', dimension=2) ])

def train(model, *args):
    model.fit(input_fn=training_fn(*args), steps=100)
    return model

def evaluate(model, *args):
    return model.evaluate(input_fn=training_fn(*args), steps=1)

if __name__ == '__main__':
    print( evaluate( train( regressor_model() ) ) )
