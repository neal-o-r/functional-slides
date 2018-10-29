from toolz import curry, nth, iterate

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
