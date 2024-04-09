import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
  
X = np.array([1, 2, 3]) # 2d array named X    ....how is it 2d array ..
Y  = np.array([4 ,5 ,6])# 2d array named Y
print(f'{X} \t X={X.shape} \n {Y} \t {Y.shape} \n\n')
X ,Y = np.meshgrid(X, Y)
print(f'{X} \t X={X.shape} \n\n {Y} \t {Y.shape}')
# # surface plot for X + Y
# fig = plt.figure()
# axes = fig.gca(projection ='3d')
# axes.plot_surface(X, Y, X)
  
# plt.show()