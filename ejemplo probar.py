import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
iris = datasets.load_iris()
X = iris.data
y = iris.target
print(X)
print(y)