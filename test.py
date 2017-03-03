import numpy as np


arr = np.array([1, 2, 3, 4, 5])
#print(arr.dtype)

float_arr = arr.astype(np.float64)
#print(float_arr.dtype)

test = np.array([3.7, -1.2, 0.5, 10.1])
test2 = test.astype(np.int32)
#print(test2)

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr*0.5)
print(arr**0.5)

tt = np.array([[1, 2, 3], [4, 5, 6]])
print(tt.shape)
print(len(tt))

print("test")