import numpy as np
np_2d = np.array([[1.73,1.68,1.71,1.89,1.79],
                [65.4,59.2,63.6,88.4,68.7]])
print(type(np_2d))
print(np_2d[0][1])
print(np_2d[0,1])
print(np_2d[:,1:3])
