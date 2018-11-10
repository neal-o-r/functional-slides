from toolz import curry, nth, iterate
from sgd import until_convergence

"""
Functions to compute sqrt by Newton's method

* newton() : procedural, applies eqn in loop
* newton_recur() : uses recursion to abstract the loop
* newton_f() : purely functional form, uses iterate
               to create an infinite sequence of approximations
               and takes the nth
* newton_converge() : same as above but works until convergence
"""

def newton(n, a=2, steps=10):
    for i in range(steps):
        a = (a + n/a)/2
    return a

def newton_recur(n, a=2, i=0, steps=10):
    if i == steps:
        return a
    return newton_recur(n, a=(a + n/a)/2, i=i+1, steps=steps)

def newton_f(n, guess=2, step=10):
    next_step = lambda a: (a + n/a)/2
    return nth(step, iterate(next_step, guess))

def newton_converge(n, guess):
    next_step = lambda a: (a + n/a)/2
    return until_convergence(iterate(next_step, guess))
