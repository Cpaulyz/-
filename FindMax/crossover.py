import random
import copy


def crossover(newPop, crossPopSize):
    count = 0
    copyPop = copy.deepcopy(newPop)
    lenPop = len(newPop)
    crossPop = []
    while count < crossPopSize:
        point1 = random.randint(0, lenPop - 1)
        point2 = random.randint(0, lenPop - 1)
        while point2 == point1:
            point2 = random.randint(0, lenPop - 1)
        crossPoint = random.randint(0, len(newPop[0]) - 1)
        temp1 = copyPop[point1][:crossPoint]
        temp2 = copyPop[point2][crossPoint:]
        crossPop.append(temp1 + temp2)
        count += 1

    return crossPop
