from FindMax.funtion import fun


def decodeToValue(pop, chrom_length, maxValue, minValue):
    decValue = []
    for i in range(len(pop)):
        temp = 0
        for j in range(chrom_length):
            temp += pop[i][j] * (2 ** j)
            # 按二进制解码成十进制，从左往右读
        decValue.append(temp)
    value = []
    for i in range(len(decValue)):
        temp = minValue + (decValue[i] * (maxValue - minValue)) / (2 ** chrom_length - 1)
        value.append(temp)
    return value


# 返回一个列表，每个位置对应的是相应个体的十进制值

def decodeChrom(pop, chrom_length, maxValue, minValue):
    # 返回一个列表，每个位置是相应的f（x）
    fValue = []
    value = decodeToValue(pop, chrom_length, maxValue, minValue)
    for i in value:
        fValue.append(fun(i))
    return fValue


def printMax(fValue, value):
    max = fValue[0]
    maxX = value[0]
    for i in range(1, len(fValue)):
        if fValue[i] > max:
            max = fValue[i]
            maxX = value[i]
    return max, maxX
