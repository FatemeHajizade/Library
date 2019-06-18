import numpy as np

class Chromosome :
    def __init__(self, genes, fitness, length):
        self.genes = genes
        self.fitness = fitness
        self.length = length