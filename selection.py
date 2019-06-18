import numpy as np

def truncation_selection(pop, truncation_threshold) :
    winners = np.array([])
    new_pop = pop
    sorted_pop = sorted(new_pop, key=lambda x:x.fitness)

    for i in range(len(pop)) :
        random_index = np.random.randint((1-truncation_threshold)*(len(pop)) ,len(pop))
        
        if len(winners) == 0:
            winners = np.append(winners,sorted_pop[random_index])
        for i in range(len(winners)):
            if np.array_equal(sorted_pop[random_index].genes, winners[i].genes):
                break
            elif i == len(winners)-1:
                winners = np.append(winners,sorted_pop[random_index])
    return winners

def tournament_selection(pop, tournament_size) :
    winners = np.array([])
    for i in range(len(pop)) : 
        winner_fitness = 0
        winner_index = -1        
        for j in range(tournament_size) :
            random_index = np.random.randint(len(pop))
            if pop[random_index].fitness > winner_fitness :
                winner_fitness = pop[random_index].fitness
                winner_index = random_index
        if len(winners) == 0:
            winners = np.append(winners,pop[winner_index])
        for i in range(len(winners)):
            if np.array_equal(pop[winner_index].genes,winners[i].genes):
                break
            elif i == len(winners)-1:
                winners = np.append(winners,pop[winner_index])
    return winners

def roulette_wheel_selection(population, n) :
    sumi = 0
    pop = np.full(n, population[0])
    for i in range(0, n) :
        sumi += population[i].fitness
    print(sumi)
    for j in range(0, n) :
        select = np.random.uniform()*sumi
        sumo = 0
        for i in range(0, n) :
            sumo += population[i].fitness
            if sumo >= select :
                 pop[j] = population[i]
        print(sumo)
    return pop

def roulette_wheel_sa(n, population) :
    maxw = 0
    winners = np.full(n, population[0])
    notselected = True
    for i in range(0, n) :
        if maxw < population[i].fitness :
            maxw = population[i].fitness
    for i in range(0, n) :
        notselected = True
        while notselected :
            chro = population[np.random.randint(0, n)]
            chrochance = chro.fitness/maxw
            prob = np.random.uniform(0,1)
            if chrochance > prob :
                notselected = False
                winners[i] = chro
    return winners

def linear_ranking_selection(population, wrr) :
    if wrr < 0:
        return population  
    newpopulation = np.array([])
    population = sorted(population, key=lambda x:x.fitness)
    n = len(population)
    Probselect = np.zeros(n, dtype=float)
    wrrp = 2-wrr    
    for i in range (1,n) :
       Probselect[i] = Probselect[i-1] + ( (1/len(Probselect))*(wrr + (wrrp-wrr)*(i-1)/(len(Probselect)-1)) )
    for i in range (1,n) :
        randnum = np.random.randint(0,1000*Probselect[n-1])/1000
        L = 0
        while Probselect[L] <= randnum :
            L = L+1
        newpopulation = np.append(newpopulation, population[L])
    return newpopulation

def exponential_ranking_selection(pop, c) :
    winners = np.array([])
    new_pop = pop
    sorted_pop = sorted(new_pop, key=lambda x:x.fitness)
    n = len(pop)
    s = np.zeros(n, dtype=float)
    s[0] = 0
    for i in range(1,n) :
        s[i] = s[i-1] + ( (c-1) / (np.power(c, n) - 1) * (np.power(c, n-i)) )
    
    for i in range(1,n) :
        r = np.random.randint(0,1000*s[n-1])/1000
        L = 0
        while s[L] <= r :
            L += 1
        winners = np.append(winners, sorted_pop[L])
    return winners