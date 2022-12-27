from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.style.use("ggplot")

#используем встроенный набор данных о раке
dataset = datasets.load_breast_cancer()

#целевой столбец target, определяет к какому типу относиться рак
#набор признаков data, по этим признакам определяется тип рака

X = dataset.data
y = dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)


model = GradientBoostingClassifier()
model.fit(X_train, y_train)
print(model)

expected_y  = y_test
predicted_y = model.predict(X_test)


print(metrics.classification_report(expected_y, predicted_y))
print(metrics.confusion_matrix(expected_y, predicted_y))


fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(X_test[:100, 0]+X_test[:100, 1]+X_test[:100, 2],
X_test[:100, 3]+X_test[:100, 4]+X_test[:100, 5], c=predicted_y[:100])
ax.set_title('Классификатор градиентного бустинга')

plt.show()
