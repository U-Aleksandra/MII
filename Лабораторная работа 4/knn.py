import math

# евклидовое расстояние
def euclidean_distance(data1, data2):
    distance = 0
    for i in range(len(data1)-1):
        distance += (data1[i] - data2[i])**2
    return math.sqrt(distance)

# расстояние до всех точек обучающей выборки и отбор k соседей
def get_neighbors(train, test, k=1):
    distances = [(train[i][-1], euclidean_distance(train[i],test))
                 for i in range(len(train))]
    distances.sort(key = lambda elem: elem[1])

    neighbors = [distances[i][0] for i in range (k)]
    return neighbors

# прогноз на основе классов соседей
def prediction(neighbors):
    count = {}
    for instance in neighbors:
        if instance in count:
            count[instance] +=1
        else :
            count[instance] = 1
    target = max(count.items(), key=lambda x: x[1])[0]
    return target

# оценка точности прогнозов
def accuracy(test, test_prediction):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == test_prediction[i]:
            correct += 1
    return (correct / len(test))

