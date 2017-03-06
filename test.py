import numpy as np

'''
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))
'''
'''
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = np.sum(test)
print(s)
'''

'''
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
'''


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    #return -np.sum(t * np.log(y)) / batch_size
    return -np.sum(np.log(y[np.arrange(batch_size), t])) / batch_size

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t)))


