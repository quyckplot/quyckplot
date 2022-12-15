import pandas as pd
import numpy as np

def linear_f_factory(a, b):
    def f(x):
        return a * x + b
    return f

def gaussian_f_factory(a, b, c, d):
    def f(x):
        return a * np.exp(-((x - b) / c) ** 2) + d
    return f

xs = np.linspace(-10, 10, 100)

for a in np.linspace(0, 10, 5):
    for c in np.linspace(0, 10, 5):
        if c == 0:
            continue
        ys = gaussian_f_factory(a, 0, c, 0)(xs)
        ys += np.random.normal(0, 0.1, len(ys))
        df = pd.DataFrame({'x': xs, 'y': ys})
        df.to_csv(f'data/gaussian_a={a}_c={c}.csv', index=False, header=False)

