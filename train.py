'''
Stub file
'''
from alphabet_scramble import AlphabetScramble
from tensor_translator import TensorTranslator
import tensorflow as tf

scramble = AlphabetScramble([
        'hi',
        'hello',
        'well hi',
        'well hello',
        'hi there',
        'hello there',
        'well hi there',
        'well hello there' ])

translator = TensorTranslator(scramble.alphabet)


# Declare list of features, we only have one real-valued feature
def model(features, labels, mode):
  # Build a linear model and predict values
  W = tf.get_variable('W', [1], dtype=tf.float64)
  b = tf.get_variable('b', [1], dtype=tf.float64)
  y = W*features['x'] + b
  # Loss sub-graph
  loss = tf.reduce_sum(tf.square(y - labels))
  # Training sub-graph
  global_step = tf.train.get_global_step()
  optimizer = tf.train.GradientDescentOptimizer(0.01)
  train = tf.group(optimizer.minimize(loss),
                   tf.assign_add(global_step, 1))
  # ModelFnOps connects subgraphs we built to the
  # appropriate functionality.
  return tf.contrib.learn.ModelFnOps(
      mode=mode, predictions=y,
      loss=loss,
      train_op=train)

estimator = tf.contrib.learn.Estimator(model_fn=model)
input_fn = tf.contrib.learn.io.numpy_input_fn({'x': x}, y, 4, num_epochs=1000)

# train
estimator.fit(input_fn=input_fn, steps=1000)
# evaluate our model
print(estimator.evaluate(input_fn=input_fn, steps=10))
