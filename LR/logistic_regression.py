# Author:Liushuchun
# Date: 2017-5-7
# Email:liuscgood@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
from pandas import Series, DataFrame


def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))


def logistic_regression(train, labelY, alpha=0.2, maxIter=1000, opt_method="graddesc"):

    start = time.time()
    train_x = np.mat(train)
    label = np.mat(labelY).transpose()
    numSamples, numFeatures = train_x.shape
    print numSamples, numFeatures
    weights = np.ones((numFeatures, 1))

    for k in range(maxIter):
        if opt_method == "graddesc":
            output = sigmoid(train_x * weights)
            error = label - output
            weights = weights + alpha * train_x.transpose() * error

        elif opt_method == "stocgrad":
            for i in range(numSamples):
                output = sigmoid(train[i, :] * weights)
                error = label[i, 0] - output
                weights = weights + alpha * train_x[i, :].transpose() * error

        else:
            raise NameError("Not Support Optimize Method types")

    print "Congratulations,training complete"

    return weights


def plot_best_fit(weights):
    import matplotlib.pyplot as plt
    data, label = load_data()
    data_matrix = np.array(data)
    n = np.shape(data_matrix)[0]
    xcord1 = []
    xcord2 = []
    ycord1 = []
    ycord2 = []
    for i in xrange(n):
        if int(label[i]) == 1:
            xcord1.append(data_matrix[i, 1])
            ycord1.append(data_matrix[i, 2])
        else:
            xcord2.append(data_matrix[i, 1])
            ycord2.append(data_matrix[i, 2])

    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()


def load_data():
    data = []
    label = []
    with open('testSet.txt') as fr:
        for line in fr.readlines():
            lineList = line.strip().split()
            data.append([1.0, float(lineList[0]), float(lineList[1])])
            label.append(int(lineList[2]))

    return data, label


if __name__ == "__main__":
    matrix, label = load_data()
    w = logistic_regression(matrix, label)
    print w
    plot_best_fit(w.getA())
