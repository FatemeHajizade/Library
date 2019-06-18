import numpy as np

def Pseudo_Random(PopulationSize,ChromosomesArray):
    population = np.array([])
    for i in range(0,PopulationSize):
        population = np.append(population, ChromosomesArray[np.random.randint(0,PopulationSize)])
    return population