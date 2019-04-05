import math


def fun(x):
    # 这个是f(x)表达式
    # value = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
    value = x*math.sin(10*math.pi*x)+2
    return value
