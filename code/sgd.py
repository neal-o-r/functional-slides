import toolz as tz
import random
import itertools
import math


def until_convergence(it):
    """
    takes a (potentially infinite) iterator and returns the
    first value at which it repeats itself.
    zips the iterator to its own tail and the moves through it
    looking for equal pairs
    """
    it2 = tz.drop(1, it)
    pairs = zip(it, it2)
    zip_eq = lambda x: x[0] != x[1]
    return tz.first(itertools.dropwhile(zip_eq, pairs))[0]


def get_data(n):
    """
    return n draws from a linear function
    """
    m, c = 2.4, 5.9
    x = [random.random() * 10 for i in range(n)]
    return x, list(map(lambda xi: m * xi + c, x))


def model(theta, x):
    m, c = theta
    return m * x + c


def err(theta, x, y):
    return y - model(theta, x)


def grad(theta, x, y):
    m, c = theta
    N = len(x)
    c_g = 0
    m_g = 0
    for xi, yi in zip(x, y):
        e = err(theta, xi, yi)
        c_g -= (2 / N) * e
        m_g -= (2 / N) * xi * e

    return [m_g, c_g]


def sgd_step(x, y, theta):
    lr = 0.001
    m, c = theta
    m_g, c_g = grad(theta, x, y)
    m_ = m - lr * m_g
    c_ = c - lr * c_g
    return [m_, c_]


def sgd(theta, x, y):
    step = tz.curry(sgd_step)(x)(y)
    return until_convergence(tz.iterate(step, theta))


if __name__ == "__main__":

    x, y = get_data(100)
    print(sgd((1, 1), x, y))
