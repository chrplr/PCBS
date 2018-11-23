import numpy as np

NBOXES = 51
NGENERATIONS = 100


def map(rule, triplet):
    """ rule is a list of 8 binary digits defining the CA-rule mapping triplets onto {0, 1}"""
    index = 4 * triplet[0] + 2 * triplet[1] + triplet[2]
    return rule[index]


def get_triplet(line, pos):
    return (line[pos - 1], line[pos], line[pos + 1])


def main(rule, nboxes, ngenerations):
    pop = np.zeros((ngenerations, nboxes), dtype=int)
    pop[0, nboxes // 2 ] = 1

    for g in range(1, ngenerations):
        for b in range(1, nboxes - 1):
            pop[g, b] = map(rule, get_triplet(pop[g - 1,:], b))

    return pop

if __name__ == '__main__':
    rule = [1, 1, 0, 1, 0, 1, 0, 1]
    main(rule, 100, 100)


