import random


def mutation(pop, p_mutation):
    popSize = len(pop)
    chromSize = len(pop[0])
    mutation_pop = []
    for i in range(popSize):
        if random.random() < p_mutation:
            mPoint = random.randint(0, chromSize - 1)
            if (pop[i][mPoint] == 1):
                pop[i][mPoint] = 0
            else:
                pop[i][mPoint] == 1
