import toolz as tz
from numpy import random as rd
import itertools
from operator import sub
import matplotlib.pyplot as plt
from typing import (List, Tuple,
                    Callable, Iterator)

Vector = List[float]
Params = Tuple[float, float]


def model(theta: Params, x: float) -> float:
    m, c = theta
    return m * x + c


def get_data(n: int) -> (Vector, Vector):
    m, c = 2.4, 5.9
    x = [rd.random() * 10 for i in range(n)]
    f = lambda x: model((m, c), x) + rd.normal()
    return x, list(map(f, x))


def err(theta: Params, x: float, y: float) -> float:
    return y - model(theta, x)


def grad(theta: Params, x: Vector, y:Vector) -> Params:
    N = len(x)

    e = [err(theta, xi, yi) for xi, yi in zip(x, y)]
    c_g = sum(-2 / N * ei for ei in e)
    m_g = sum(-2 / N * ei * xi for ei, xi in zip(e, x))
    return m_g, c_g


def sgd_step(x: Vector, y: Vector, theta: Params) -> Params:
    lr = 0.001
    m_g, c_g = grad(theta, x, y)
    m, c = theta
    m_ = m - lr * m_g
    c_ = c - lr * c_g
    return m_, c_


def until_convergence(it: Iterator[Params],
                      eq: Callable = lambda x: x[0] != x[1]) -> Params:
    it2 = tz.drop(1, it)
    pairs = zip(it, it2)
    return tz.first(itertools.dropwhile(eq, pairs))[0]


def sgd(theta: Params,  x:Vector, y: Vector) -> Params:
    step = tz.curry(sgd_step)(x, y)
    converge = lambda x: abs(sum(map(sub, x[0], x[1]))) > 1e-5
    return until_convergence(tz.iterate(step, theta))


if __name__ == "__main__":
    x, y = get_data(100)
    m, c = sgd((1, 1), x, y)
    plt.plot(x, [m*xi + c for xi in x])
    plt.plot(x, y, '.')
