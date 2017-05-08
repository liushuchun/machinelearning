import numpy as np
import math


def get_y(x):
    value = pow((x+2), 2) - 16*math.exp(-x*(x-2))
    return value


def get_grad(x):
    return (2*x+4)-16*(-2*x+4)*np.exp(-((x-2)**2))


def gradient_descent(start_x, func, grad):
    # precission of the solution
    prec = 0.00001
    step_size = 0.1
    max_iter = 100
    x_new = start_x
    res = []
    for i in xrange(max_iter):
        x_old = x_new
        x_new = x_old - step_size*get_grad(x_new)
        f_x_new = get_y(x_new)
        f_x_old = get_y(x_old)
        res.append([x_new, f_x_new])
        if(abs(f_x_new-f_x_old) < prec):
            print "change in function values to small, leaving"

            return np.array(res)
    print "exceeded maximum number of iterations,leaving"
    return np.array(res)

if __name__ == "__main__":
    x=-8
    print gradient_descent(x, get_y, get_grad)

