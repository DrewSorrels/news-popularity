import tensorflow as tf
import numpy as np

from tensorflow.contrib.learn.python.learn import metric_spec
from tensorflow.contrib.tensor_forest.client import eval_metrics
from tensorflow.contrib.tensor_forest.client import random_forest
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources

import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# Read data
data = np.loadtxt(open(sys.argv[1]), delimiter = ", ", skiprows = 1, usecols = range(1,61))
features, labels = np.hsplit(data, [59]) # TODO: refactor with dataset.map
print('Features: ', features.shape)
print('Labels: ', labels.shape)

train_input_fn = tf.estimator.inputs.numpy_input_fn(
	x = {'x': features},
	y = labels,
	num_epochs = None,
	shuffle = True)

# Parameters
num_classes = 4
num_features = 59
num_trees = 4
max_nodes = 1000

# Random forest parameters
hparams = tensor_forest.ForestHParams(
			num_classes = num_classes,
			num_features = num_features,
			num_trees = num_trees,
			max_nodes = max_nodes).fill()

classifier = random_forest.TensorForestEstimator(hparams)

classifier.fit(input_fn = train_input_fn, steps = None)

# Verify results
metric_name = 'accuracy'
metric = {
	metric_name:
		metric_spec.MetricSpec(
			eval_metrics.get_metric(metric_name),
			prediction_key=eval_metrics.get_prediction_key(metric_name))
}

test_input_fn = tf.estimator.inputs.numpy_input_fn(
	x = {'x': features[0:10]},
	y = labels[0:10],
	num_epochs = None,
	shuffle = True)
results = classifier.evaluate(input_fn = test_input_fn, metrics = metric)

for key in sorted(results):
	print('%s: %s' % (key, results[key]))