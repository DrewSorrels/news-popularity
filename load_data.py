import numpy as np

def load_dataset(data_file):
	data = np.loadtxt(open(data_file), delimiter = ", ", skiprows = 1, usecols = range(1,61))
	features, labels = np.hsplit(data, [59]) # TODO: refactor with dataset.map

	dataset = tf.data.Dataset.from_tensor_slices((features, labels))
	dataset = dataset.shuffle(buffer_size=10000)
	dataset = dataset.repeat()