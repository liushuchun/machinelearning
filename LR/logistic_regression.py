# Author:Liushuchun
# Date: 2017-5-7
# Email:liuscgood@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import time


def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))


def logistic_regression(train, label, alpha=0.2, maxIter=1000, opt_method="graddesc"):

    start = time.time()

    numSamples, numFeatures = np.shape(train_x)

    weights = np.ones((numFeatures, 1))

    for k in range(maxIter):
        if opt_method == "graddesc":
            output = sigmoid(train * weights)
            error = label - output
            weights = weights + alpha * train.transpose() * error

        elif opt_method == "stocgrad":
            for i in range(numSamples):
                output = sigmoid(train[i, :] * weights)
                error = label[i, 0] - output
                weights = weights + alpha * train[i, :].transpose() * error

        else:
            raise NameError("Not Support Optimize Method types")

    print "Congratulations,training complete"

    return weights



