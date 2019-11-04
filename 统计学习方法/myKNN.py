#%%
import numpy as np
def load_data():
    x = np.array([[5, 4],[9, 6],[4, 7],[2, 3], [8, 1], [7, 2]])
    y = np.array([1, 1, 1, 0, 0, 0])
    return x, y
X, Y = load_data()

# %%
def KNN(test, X ,Y):
    dif = X - test
    dis = np.sum(dif**2, axis=1)
    return Y[np.argmin(dis)]

%timeit KNN((5,3), X, Y)

# %%
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X, Y)
%timeit neigh.predict([[5, 3]]) #我的比他快呀

