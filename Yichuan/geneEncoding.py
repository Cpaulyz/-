import random


def geneEncoding(pop_size, chrom_length):
    pop = []
    for j in range(pop_size):
        temp = []
        for i in range(chrom_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)

    return pop
