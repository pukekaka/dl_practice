import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

def step_function3(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def softmax2(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

#x = np.arange(-5.0, 5.0, 0.1)
#y = step_function3(x)
#y = sigmoid(x)
#plt.plot(x,y)
#plt.ylim(-0.1, 1.1)
#plt.show()

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],
              [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print(A1)
print(Z1)

W2 = np.array([[0.1,0.4],
               [0.2, 0.5],
               [0.3,0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3],
               [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

print(Y)