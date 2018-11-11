import toolz as tz
import random
import itertools
import math
from operator import sub


def until_convergence(it, eq=lambda x: x[0] != x[1]):
    """
    takes a (potentially infinite) iterator and returns the
    first value at which it repeats itself.
    zips the iterator to its own tail and the moves through it
    looking for equal pairs
    """
    it2 = tz.drop(1, it)
    pairs = zip(it, it2)
    return tz.first(itertools.dropwhile(eq, pairs))[0]


def get_data(n):
    """
    return n draws from a linear function
    """
    m, c = 2.4, 5.9
    x = [random.random() * 10 for i in range(n)]
    return x, list(map(lambda xi: m * xi + c, x))


def model(theta, x):
    """
    apply linear model
    """
    m, c = theta
    return m * x + c


def err(theta, x, y):
    return y - model(theta, x)


def grad(theta, x, y):
    """
    compute the gradient of the loss function
    over all data
    """
    N = len(x)
    e = [err(theta, xi, yi) for xi, yi in zip(x, y)]
    c_g = [-2 / N * ei for ei in e]
    m_g = [-2 / N * ei * xi for ei, xi in zip(e, x)]

    return [sum(m_g), sum(c_g)]


def sgd_step(x, y, theta):
    """
    take a single gradient step
    """
    lr = 0.001
    m, c = theta
    m_g, c_g = grad(theta, x, y)
    m_ = m - lr * m_g
    c_ = c - lr * c_g
    return [m_, c_]


def sgd(theta, x, y):
    """
    continue taking grad steps until conevrgence, ie. until grad == 0
    """
    step = tz.curry(sgd_step)(x)(y)
    converge = lambda x: abs(sum(map(sub, x[0], x[1]))) > 1e-5
    return until_convergence(tz.iterate(step, theta), converge)


if __name__ == "__main__":

    x, y = get_data(100)
    print(sgd((1, 1), x, y))
