from base_b import convert
from random import randint
from sklearn.svm import SVC
from sklearn import preprocessing

DATA_DIR = "./data/"
RESULTS_DIR = "./results/"

def train(dataset, max_base, max_C, kernel, max_class_weight):
    for base in range(2, max_base):

        data = get_space(dataset, base)
        min_max_scaler = preprocessing.MinMaxScaler()
        X_train = min_max_scaler.fit_transform(data["train.X"])
        y_train = data["train.y"]
        X_test = min_max_scaler.fit_transform(data["test.X"])
        y_test = data["test.y"]

        C = 0.1

        while C <= max_C:
            for weight in range(1, max_class_weight + 1):
                c_weight = {1: weight}
                clf = SVC(C=C, kernel=kernel, cache_size=1000, class_weight=c_weight)
                clf.fit(X_train, y_train)
                score = clf.score(X_test, y_test)
                print(score)
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
