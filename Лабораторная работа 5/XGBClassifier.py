import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.datasets import load_breast_cancer

#Загрузка Dataset
cancer = load_breast_cancer()

#Просмотр данных
print("Название функций")
print(cancer.feature_names)
print('\n')
print("Имена целевых классов")
print(cancer.target_names)

#создание Dataframe
df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns = np.append(cancer['feature_names'], ['target']))

#Объединение функций и цели в один большой фрейм данных
X = df_cancer.drop('target',axis=1)
y = df_cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=66)

#Инициализация модели
model = xgboost.XGBClassifier()

#Обучение модели
model.fit(X_train,y_train)

#Прогнозирование на основе модели
y_pred = model.predict(X_test)

#Вывод результата
cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True)
plt.show()

print(classification_report(y_test,y_pred))
