import os
from base_b import convert
from random import randint
from sklearn.svm import SVC
from sklearn import preprocessing
from time import time
import argparse


DATA_DIR = "./data/"
RESULTS_DIR = "./results/"

def train(base, kernel, min_C, max_C, min_class_weight, max_class_weight):

	seed = int(time())

	for root, dirs, files in os.walk(DATA_DIR):

		for dataset in files:
			#dataset = os.path.join(root, filename)

			result = RESULTS_DIR + "%f_%s" % (time(), dataset)
			with open(result, "w") as f:

				data = get_space(dataset, base)
				min_max_scaler = preprocessing.MinMaxScaler()
				X_train = min_max_scaler.fit_transform(data["train.X"])
				y_train = data["train.y"]
				X_test = min_max_scaler.fit_transform(data["test.X"])
				y_test = data["test.y"]

				C = min_C

				while C <= max_C:
					for weight in range(min_class_weight, max_class_weight + 1):
						c_weight = {1: weight}
						clf = SVC(C=C, kernel=kernel, cache_size=1000, class_weight=c_weight, random_state=seed)
						clf.fit(X_train, y_train)
						score = clf.score(X_test, y_test)
						f.write("%d, %d, %f, %s, %d, %f\n" % (seed, base, C, kernel, weight, score))
						print("%d, %d, %f, %s, %d, %f\n" % (seed, base, C, kernel, weight, score))
					C += 0.1


def get_data(dataset_filename):
    with open(DATA_DIR + dataset_filename) as f:
        lines = f.readlines()

    nums = list()
    labs = list()

    for line in lines:
        num, lab = line.split(",")
        nums.append(int(num))
        labs.append(int(lab))

    return [nums, labs]

def get_space(dataset, base, part=0.7):

    data = get_data(dataset)

    bound = int(part * len(data[0]))

    max_vec_len = 0

    y_train = data[1][:bound]

    X_train_1 = data[0][:bound]
    X_train_2 = list()

    for n in X_train_1:
        vec = convert(n, base)
        if len(vec) > max_vec_len:
            max_vec_len = len(vec)
        X_train_2.append(vec)

    y_test = data[1][bound:]

    X_test_1 = data[0][bound:]
    X_test_2 = list()

    for n in X_test_1:
        vec = convert(n, base)
        if len(vec) > max_vec_len:
            max_vec_len = len(vec)
        X_test_2.append(vec)

    X_train = list()
    for vec in X_train_2:
        while len(vec) < max_vec_len:
            vec = [0] + vec
        X_train.append(vec)

    X_test = list()
    for vec in X_test_2:
        while len(vec) < max_vec_len:
            vec = [0] + vec
        X_test.append(vec)


    return {"train.X": X_train, "train.y": y_train, "test.X": X_test, "test.y": y_test}


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Support Vector Machine Classifier")
	parser.add_argument('-b', metavar='base', dest='base', type=int, nargs='?', help='base b representation of integers')
	parser.add_argument('-k', metavar="kernel", dest="kernel", type=str, nargs='?', help="must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable")
	parser.add_argument('--min_c', metavar='min_c', dest='min_c', type=int, nargs='?', help='min penalty parameter C of the error term.')
	parser.add_argument('--max_c', metavar='max_c', dest='max_c', type=int, nargs='?', help='max penalty parameter C of the error term.')
	parser.add_argument('--min_w', metavar='min_weight', dest='min_weight', type=int, nargs='?', help='min weight of primes class')
	parser.add_argument('--max_w', metavar='max_weight', dest='max_weight', type=int, nargs='?', help='max weight of primes class')

	args = parser.parse_args()

	# train(base, kernel, min_C, max_C, min_class_weight, max_class_weight):

	train(base=args.base, kernel=args.kernel, min_C=args.min_c, max_C=args.max_c, min_class_weight=args.min_weight, max_class_weight=args.max_weight)


