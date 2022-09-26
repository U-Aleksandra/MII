#Лабораторная работа №2
#Выполнил студент группы ИСТбд-42
#Ушкова Александра
#Вариант - 18

import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

size_N  = input("Введите размерность квадратной матрицы: ")
N = int(size_N )
A = np.random.randint(-10,11,size=(N,N))
F = A.copy()
print("Матрица A:")
print(A)

print("\n")
K = input("Введите K: ")
K = int(K)
print("\n")

size = math.floor(N/2)
C = F[size:,size:].copy() #создаем матрицу С
nechCol = np.array(C)[:,1::2] #создаем матрицу с нечетными столбцами матрицы С

#определяем количество элементов > K
count = 0
for i in nechCol:
    if (i>K).any():
        count+=1

nechRow = np.array(C)[1::2,:]#создаем матрицу с нечетными строками матрицы С

#находим произведение элементов
mult = 1
rows, columns = nechRow.shape
for i in range(rows):
    for j in range(columns):
        mult *= nechRow[i][j]

#матрица B
if (N % 2 == 0):
    B = F[:size,size:].copy()
else:
    B = F[:size + 1,size:].copy()
    
#симетричный обмен элементов С и В
if (count > mult):
    print("Симметрично меняем С и В")
    rows, columns = B.shape
    for i in range(rows):
        for j in range(columns):
            B[i][j], C[rows - (1 + i)][j] = C[rows - (1 + i)][j], B[i][j]
    if (N % 2 == 0):
        F[:size,size:] = B
        F[size:,size:] = C
    else:
        F[:size + 1, size:] = B
        F[size:, size:] = C
        
#несимметричный обмен элементов С и Е
else:
    print("Не симметрично меняем С и Е")
    for i in range(0,math.ceil(N/2)):
        for j in range(0,math.ceil(N/2)):
            F[i][j],F[math.floor(N/2)+i][math.floor(N/2)+j]=F[math.floor(N/2)+i][math.floor(N/2)+j],F[i][j]

print("\n Матрица F после преобразования \n")
print(F)

detA = np.linalg.det(A)#определитель матрицы А
sumDiagF = np.trace(F)#сумма диагональных элементов матрицы F

#вычисление выражений
if(detA > sumDiagF):
    print("\n Определитель А больше суммы диагональных элементов F\n")
    result = np.dot(A,A.transpose())-(K*np.linalg.inv(F))
    print("Результат вычисления: ")
    print(result)
else:
     print("\n Определитель А меньше суммы диагональных элементов F\n")
     result = (np.linalg.inv(A)+np.tril(A)-F.transpose())*K
     print("Результат вычисления: ")
     print(result)

#вывод графика F
plt.matshow(F)
plt.title("График матрицы №1",fontsize=12)
plt.show()

ax = sns.heatmap(F, annot=True, fmt="d")
plt.title("График матрицы №2",fontsize=12)
plt.savefig("visual_numpy_array.png", bbox_inches='tight', dpi=100)
plt.show()

plt.imshow(F,vmin=0,vmax=1)
plt.colorbar()
plt.title("График матрицы №3",fontsize=12)
plt.show()

