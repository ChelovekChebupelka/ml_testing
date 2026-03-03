import numpy as np


M = np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])

D = np.ones((3,3))
D*=2

new_m = D@M
a=np.linalg.inv(M)
print(new_m)

