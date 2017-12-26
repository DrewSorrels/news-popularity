import tensorflow as tf
import numpy as np
import load_data

from tensorflow.contrib import data
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources

import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# Read data
data = load_data.load_dataset(sys.argv[1])

# Parameters
num_steps = 500
batch_size = 1024
num_classes = 4
num_features = 59
num_trees = 4
max_nodes = 1000

# Input and Target data
X = tf.placeholder(tf.float32, shape = [None, num_features])

# Labels must be integers in random forest
Y = tf.placeholder(tf.int32, shape = [None])

# Random forest parameters
hparams = tensor_forest.ForestHParams(
			num_classes = num_classes,
			num_features = num_features,
			num_trees = num_trees,
			max_nodes = max_nodes).fill()

# Build the Random Forest
forest_graph = tensor_forest.RandomForestGraphs(hparams)

# Get training graph and loss
train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

# Measure the accuracy
infer_op, _ = forest_graph.inference_graph(X)
correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64)) # maybe switch this to check if in bucket
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Initialize the variables and forest resources
init_vars = tf.group(tf.global_variables_initializer())
# init_vars = tf.group(tf.global_variables_initializer(), resources.initialize_resources(resources.shared_resources()))

# Start TensorFlow session
sess = tf.Session()

sess.run(init_vars)

# Training
for i in range(1, num_steps + 1):
	# Prepare data
	# batch_x, batch_y = dataset.batch(batch_size)
	_, l = sess.run([train_op, loss_op], feed_dict={X: batch_x, Y: batch_y})
	if i % 50 == 0:
		accuracy = sess.run(accuracy_op, feed_dict = {X: batch_x, Y: batch_y})
		print('Step %i, Loss: %f, Accuracy: %f' % (i, l, accuracy))

# Test model
# test_x, test_y = 
print("Test Accuracy:", sess.run(accuracy_op, feed_dict = {X: test_x, Y: test_y}))