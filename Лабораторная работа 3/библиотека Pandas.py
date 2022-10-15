import pandas as pd
import matplotlib.pyplot as plt
import plotly
import numpy as np

data = pd.read_csv('file.csv', delimiter=',',encoding="windows-1251")

#расчеты над количеством проектов
dataCountProj = data['Количество выполненных проектов']
maxProject = dataCountProj.max()#определяется максимум
minProject = dataCountProj.min()#определяется минимум
meanProject = dataCountProj.mean()#определяется среднее
dispProject = dataCountProj.var()#определяется дисперсия
stdProject = dataCountProj.std()#определяется стандартное отклонение
medianProject = dataCountProj.median()#расчитывается медиана

print("Статистические характеристики для количества выполненных проектов")
print("Максимум:",maxProject)
print("Минимум:",minProject)
print("Среднее:",meanProject)
print("Дисперсия:",dispProject)
print("Стандартное отклонение:",stdProject)
print("Медиана",medianProject)
print()

#расчеты над годом рождения
dataYearBirth = data['Год рождения']
maxYear = dataYearBirth.max()#определяется максимум
minYear = dataYearBirth.min()#определяется минимум
meanYear = dataYearBirth.mean()#определяется среднее

print("Статистические характеристики для года рождения сотрудника")
print("Самый старый сотрудник родился в", minYear)
print("Самый молодой сотрудник родился в", maxYear)
print("Средний год рождения сотрудника:", int(meanYear))
print()

#расчеты над табельным номером
dataTabNum = data['Табельный номер']
dispTab = dataTabNum.var()#определяется дисперсия
stdTab = dataTabNum.std()#определяется стандартное отклонение
medianTab = dataTabNum.median()#расчитывается медиана

print("Статистические характеристики для табельного номера")
print("Дисперсия:", dispTab)
print("Стандартное отклонение:", stdTab)
print("Медиана:", medianTab)

 
#грифики
graf1 = data['Год начала работы в компании'].hist()
plt.xlabel('Год начала работы')
plt.ylabel('Количество сотрудников')
plt.title('Анализ прибытия сотрудников')
plt.show()

data[['Оклад','Должность']].plot(
    kind='scatter',
    x='Оклад',
    y='Должность',
    figsize=(12,8))
plt.show()

plt.plot(data['Количество выполненных проектов'], label = 'Проекты')
plt.axhline (y=np.nanmean(data['Количество выполненных проектов'].mean()), color = 'red', linestyle = '--', linewidth = 2 , label = 'Mean')
plt.title('Среднее количество выполненных проектов', loc = 'center')
plt.show()

