import pandas as pd
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from knn import *

#ДОБИВИЛИ НОВЫЙ КЛАСС
data1 = pd.read_csv('lab_4_2.csv', delimiter=',',encoding="windows-1251")

# Отображение исходных данных
classColormap  = ListedColormap(['#f9fc44', '#fc30da', '#1ae8d0','#e81a3f'])
pl.scatter([data1['сладость'] for i in range(len(data1))],
               [data1['хруст'] for i in range(len(data1))],
               c=[data1['класс'] for i in range(len(data1))],
               cmap=classColormap)
pl.show()

# Разделение данных
X = data1[['сладость','хруст']]
Y = data1['класс']

# Получение 20% от набора данных для обучения
test_size = int(np.round(25 * 0.2, 0))

# Разделение набора данных на обучающие и тестовые наборы
X_train = X[:-test_size].values
Y_train = Y[:-test_size].values

X_test = X[-test_size:].values
Y_test = Y[-test_size:].values

# Объединение обучающих и тестовых данных для удобства
X_train_concat = np.concatenate((X_train, Y_train.reshape(20, 1)), axis=1)
X_test_concat = np.concatenate((X_test, Y_test.reshape(5,1)),axis=1)

# решение методом kNN
pred = []
for x in range (len(X_test_concat)):
    neighbors = get_neighbors(X_train_concat, X_test_concat[x], k=1)
    result = prediction(neighbors)
    pred.append(result)

Accuracy = accuracy(X_test_concat, pred)
print("Добавили новый класс")
print()
print("Расчет без библиотеки sklearn")
print(f'Точность: ', Accuracy)
print()

# с помощью библиотеки sklearn

knn = KNeighborsClassifier(n_neighbors=5)
knn_model = knn.fit(X_train, Y_train)
knn_predictions = knn.predict(X_test)
accuracy = accuracy_score(Y_test, knn_predictions)
print("Расчет с библиотекой sklearn")
print(f'Точность: {accuracy}')

