import pandas as pd
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from knn import *

#Подготовка данных
data = pd.read_csv('lab_4.csv', delimiter=',',encoding="windows-1251")

# Отображение исходных данных
classColormap  = ListedColormap(['#FF0000', '#00FF00', '#4910e5'])
pl.scatter([data['сладость'] for i in range(len(data))],
               [data['хруст'] for i in range(len(data))],
               c=[data['класс'] for i in range(len(data))],
               cmap=classColormap)
pl.show()

# Разделение данных
X = data[['сладость','хруст']]
Y = data['класс']

# Получение 20% от набора данных для обучения
test_size = int(np.round(20 * 0.2, 0))

# Разделение набора данных на обучающие и тестовые наборы
x_train = X[:-test_size].values
y_train = Y[:-test_size].values

x_test = X[-test_size:].values
y_test = Y[-test_size:].values

# Объединение обучающих и тестовых данных для удобства
x_train_concat = np.concatenate((x_train, y_train.reshape(16, 1)), axis=1)
x_test_concat = np.concatenate((x_test, y_test.reshape(4,1)),axis=1)

# решение методом kNN
predictions = []
neigh = []
for x in range (len(x_test_concat)):
    neighbors = get_neighbors(x_train_concat, x_test_concat[x], k=1)
    neigh.append(neighbors)
    result = prediction(neighbors)
    predictions.append(result)

accuracy = accuracy(x_test_concat, predictions)
print("Расчет без библиотеки sklearn")
print(f'Точность: ', accuracy)
print()


# с помощью библиотеки sklearn

knn = KNeighborsClassifier(n_neighbors=5)
knn_model = knn.fit(x_train, y_train)
knn_predictions = knn.predict(x_test)
accuracy = accuracy_score(y_test, knn_predictions)
print("Расчет с библиотекой sklearn")
print(f'Точность: {accuracy}')




