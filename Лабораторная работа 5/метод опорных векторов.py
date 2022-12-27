import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm

dataset = pd.read_csv('iris_csv.csv', delimiter=',')

#целевой столбец - класс ириса
#набор признаков - длина чашелистика и длина лепестка
#т.к от этих признаков зависит к какому классу относится ирис


feature = dataset[['sepallength','petallength']]
label = dataset['class']

#получение 20% от набора данных для обучения
size = len(dataset.axes[0])
test_size = int(np.round(size * 0.2, 0))

#разделение набора данных на обучающие и тестовые наборы
x_train = feature[:-test_size].values
y_train = label[:-test_size].values

x_test = feature[-test_size:].values
y_test = label[-test_size:].values

# Построение графика для обучающего набора
fig, ax = plt.subplots(figsize=(16, 9))
# Удаление верхней и правой границ
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
# Добавление основных линий сетки
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
ax.scatter(feature[:-test_size]['sepallength'], feature[:-test_size]['petallength'], color="#8C7298")
plt.show()

model = svm.SVC(kernel='linear')
model.fit(x_train, y_train)

from sklearn.metrics import accuracy_score
predictions_poly = model.predict(x_test)
accuracy_poly = accuracy_score(y_test, predictions_poly)
print("2nd degree polynomial Kernel\nAccuracy (normalized): " + str(accuracy_poly))


fig, ax = plt.subplots(figsize=(12, 7))

# Удаление верхней и правой границ
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# Создание сетки для оценки модели
xx = np.linspace(-1, max(feature['sepallength']) + 1, len(x_train))
yy = np.linspace(0, max(feature['petallength']) + 1, len(y_train))
YY, XX = np.meshgrid(yy, xx)

train_size = len(feature[:-test_size]['sepallength'])

# Присвоение классам различных цветов
colors = y_train
colors = np.where(colors == 1, '#8C7298', '#4786D1')

# Построение графика набора данных
ax.scatter(feature[:-test_size]['sepallength'], feature[:-test_size]['petallength'], c=colors)


# Выделение опорных векторов окружностями
ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=100, linewidth=1, facecolors='none', edgecolors='k')

plt.show()

