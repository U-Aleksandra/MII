import csv
import numpy as np

with open('file.csv') as scvfile:

    project = []
    yearBirth = []
    tabNum = []
    
    reader = csv.reader(scvfile)
    for row in reader:
        project.append(row[8])#добавляем количество проектов в массив
        yearBirth.append(row[3])#добавляем год рождения в массив
        tabNum.append(row[0])#добавляем табельный номер в массив

    #расчеты над количеством проектов
    project.pop(0)#удаление заголовка
    projectInt = list(map(int,project))#конвертирование в int

    maxProject = np.max(projectInt)#определяется максимум
    minProject = np.min(projectInt)#определяется минимум
    meanProject = np.mean(projectInt)#определяется среднее
    dispProject = np.var(projectInt)#определяется дисперсия
    stdProject = np.std(projectInt)#определяется стандартное отклонение
    medianProject = np.median(projectInt)#расчитывается медиана
    
    print("Статистические характеристики для количества выполненных проектов")
    print("Максимум:", maxProject)
    print("Минимум:", minProject)
    print("Среднее:", meanProject)
    print("Дисперсия:", dispProject)
    print("Стандартное отклонение:", stdProject)
    print("Медиана:", medianProject)
    print()

    #расчеты над годом рождения
    yearBirth.pop(0)#удаление заголовка
    yearBirthInt = list(map(int,yearBirth))#конвертирование в int

    maxYear = np.max(yearBirthInt)#определяется максимум
    minYear = np.min(yearBirthInt)#определяется минимум
    meanYear = np.mean(yearBirthInt)#определяется среднее

    print("Статистические характеристики для года рождения сотрудника")
    print("Самый старый сотрудник родился в", minYear)
    print("Самый молодой сотрудник родился в", maxYear)
    print("Средний год рождения сотрудника:", int(meanYear))
    print()

    #расчеты над табельным номером
    tabNum.pop(0)#удаление заголовка
    tabNumInt = list(map(int,tabNum))#конвертирование в int

    dispTab = np.var(tabNumInt)#определяется дисперсия
    stdTab = np.std(tabNumInt)#определяется стандартное отклонение
    medianTab = np.median(tabNumInt)#расчитывается медиана

    print("Статистические характеристики для табельного номера")
    print("Дисперсия:", dispTab)
    print("Стандартное отклонение:", stdTab)
    print("Медиана:", medianTab)

    
