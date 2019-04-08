import random
import copy


def abandon(fValue):
    selectedValue = []
    for i in fValue:
        if i > 0:
            selectedValue.append(i)
        else:
            selectedValue.append(0)
    return selectedValue


def sum(selectedValue):
    total = 0
    for i in selectedValue:
        total += i

    return total


def percent(selectedValue):
    sumValue = sum(selectedValue)
    for i in range(len(selectedValue)):
        selectedValue[i] = selectedValue[i] / sumValue
    for i in range(len(selectedValue) - 2, -1, -1):
        temp = 0
        for j in range(i + 1):
            temp += selectedValue[j]
        selectedValue[i] = temp
    selectedValue[len(selectedValue) - 1] = 1


def select(fValue, newPopSize, pop):
    selectedValue = abandon(fValue)
    percent(selectedValue)
    selectPop = []
    # 选newPopSize个，就生成newPopSize个随机数
    for i in range(newPopSize):
        pSelect = random.random()
        for j in range(len(selectedValue)):
            if selectedValue[j] > pSelect:
                temp = copy.deepcopy(pop[j])
                selectPop.append(temp)
                break

    return selectPop
