import numpy as np

def single_point_crossover(parent1, parent2) :
    n = parent1.length
    rand_index = np.random.randint(1,n)   
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    for i in range(0, rand_index) :
        child1.genes[i] = parent1.genes[i]     
        child2.genes[i] = parent2.genes[i]
    for i in range(rand_index, n) :
        child1.genes[i] = parent2.genes[i]
        child2.genes[i] = parent1.genes[i]
    return child1, child2

def multi_point_crossover(parent1, parent2, points) :
    n = parent1.length  
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)  
    pointarray = np.full(points,0)
    for i in range(len(pointarray)):
        rand_index = np.random.randint(1,n)
        if not rand_index in pointarray :
            pointarray[i] = rand_index
        else :
            while rand_index in pointarray :
                 rand_index = np.random.randint(1,n)
            pointarray[i] = rand_index
    pointarray = sorted(pointarray)
    pointarray = np.append(pointarray,n)
    k = 0
    for i in range(len(pointarray)) :
        if i%2 == 0 :
            while k < pointarray[i]:
                child1.genes[k] = parent1.genes[k]
                child2.genes[k] = parent2.genes[k]
                k += 1
            k = pointarray[i]
        else:
            while k < pointarray[i]:
                child1.genes[k] = parent2.genes[k]
                child2.genes[k] = parent1.genes[k]
                k += 1
            k = pointarray[i]
    return child1, child2

def uniform_crossover(parent1, parent2):
    n = parent1.length 
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,2), n) 
    for i in range(0,n):
        rand_index = np.random.uniform()
        if rand_index <= 0.5:
            child1.genes[i] = parent1.genes[i]
            child2.genes[i] = parent2.genes[i]
        else:
            child1.genes[i] = parent2.genes[i]
            child2.genes[i] = parent1.genes[i]   
    return child1,child2

def flat_crossover(parent1, parent2, r) :
    n = parent1.length
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    
    for i in range(n) :
        child1.genes[i] = (r[i]*parent1.genes[i]) + ((1-r[i])*parent2.genes[i])
        child2.genes[i] = (r[i]*parent2.genes[i]) + ((1-r[i])*parent1.genes[i])
        
    return child1,child2

def order_crossover(parent1, parent2) :
    n = parent1.length    
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)   
    rand_index1 = np.random.randint(1,n)
    rand_index2 = np.random.randint(1,n)
    while rand_index2 == rand_index1:
        rand_index2 = np.random.randint(1,n)
    
    if rand_index1 > rand_index2:
        rand_index1,rand_index2 = rand_index2,rand_index1
    
    for i in range(rand_index1-1, rand_index2-1) :
        child1.genes[i] = parent1.genes[i]
        child2.genes[i] = parent2.genes[i]
    print(rand_index1,rand_index2)

    j = 0
    k = 0
    for i in range(0,n):
        if j<n and k<n and not parent2.genes[i] in child1.genes :
            child1.genes[j] = parent2.genes[i]
            j += 1
        if not parent1.genes[i] in child2.genes :
            child2.genes[k] = parent1.genes[i]
            k += 1
    
    j = rand_index2
    k = rand_index2

    for i in range(rand_index2, rand_index2+n) :
        if j<n and k<n and not parent2.genes[i%n] in child1.genes :
            child1.genes[j] = parent2.genes[i%n]
            j += 1
        if not parent1.genes[i%n] in child2.genes :
            child2.genes[k] = parent1.genes[i%n]
            k += 1
    return child1,child2
           
def edge_recombination_crossover(parent1, parent2):
    n = parent1.length
    
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)
    
    adj = np.full((n,4), -1)
    
    for i in range(0,n):
        adj[i][0] = parent1.genes[i-1]
        adj[i][1] = parent1.genes[(i+1)%n]
        index = np.where(parent2.genes == parent1.genes[i])
        if np.where(adj[i] == parent2.genes[index[0]-1]) == []:
            adj[i][2] = parent2.genes[index[0]-1]
        if np.where(adj[i] == parent2.genes[(index[0]+1)%n]) == []:
            adj[i][3] = parent2.genes[(index[0]+1)%n]
            
    child1.genes[0] = parent1.genes[0]
    child2.genes[0] = parent2.genes[0]   

    for i in range(0,n-1):
        mini = 100000000000000
        ans = 0
        for j in range(0,4):
            if adj[i][j] != -1 :
                length = size(adj[adj[i][j]])
                if length < mini :
                    mini = length
                    ans = adj[i][j]
        child1.genes[i+1] = ans
        for i in range(0, n):
            if np.where(adj[i] == ans) != []:
                index = np.where(adj[i]==ans)
                adj[i][index[0]] = -1
                
        
    for i in range(0,n):
        adj[i][0] = parent1.genes[i-1]
        adj[i][1] = parent1.genes[(i+1)%n]
        index = np.where(parent2.genes == parent1.genes[i])
        if np.where(adj[i] == parent2.genes[index[0]-1])==[]:
            adj[i][2] = parent2.genes[index[0]-1]
        if np.where(adj[i] == parent2.genes[(index[0]+1)%n])==[]:
            adj[i][3] = parent2.genes[(index[0]+1)%n]
            
    for i in range(0,n-1):
        mini = 100000000000000
        ans = 0
        for j in range(0,4):
            if adj[i][j] != -1 :
                length = size(adj[adj[i][j]])
                if length < mini :
                    mini = length
                    ans = adj[i][j]
        child2.genes[i+1] = ans
        for i in range(0, n):
            if np.where(adj[i] == ans) != []:
                index = np.where(adj[i] == ans)
                adj[i][index[0]] = -1
    return child1, child2

def partially_mapped_crossover(parent1, parent2, crossover_rate) :
    random = np.random.uniform(0,1)
    if random < crossover_rate :
        return parent1, parent2
    else :
        n = parent1.length
        point1 = np.random.randint(n)
        point2 = np.random.randint(n)

        while point1 == point2 :
            point2 = np.random.randint(n)
        if point2 < point1 :
            point1, point2 = point2, point1

        child1 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)
        child2 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)
        
        for i in range(point1, point2+1) :
            child1.genes[i] = parent1.genes[i]
            child2.genes[i] = parent2.genes[i]
            
        for i in range(point1, point2+1) :
            if not parent2.genes[i] in child1.genes:
                if  child1.genes[np.where(parent2.genes == parent1.genes[i])] == -1 :
                    child1.genes[np.where(parent2.genes == parent1.genes[i])] = parent2.genes[i]
                else:
                    index = np.where(parent2.genes == parent1.genes[i])
                    while child1.genes[index] != -1 :
                        index = np.where(parent2.genes == parent1.genes[index])
                    child1.genes[index] = parent2.genes[i]
                
            if not parent1.genes[i] in child2.genes:
                if  child2.genes[np.where(parent1.genes == parent2.genes[i])] == -1 :
                    child2.genes[np.where(parent1.genes == parent2.genes[i])] = parent1.genes[i]
                else:
                    index = np.where(parent1.genes == parent2.genes[i])
                    while child2.genes[index] != -1 :
                        index = np.where(parent1.genes == parent2.genes[index])
                        
                    child2.genes[index] = parent1.genes[i]
                    
        for i in range(n):
            if child1.genes[i] == -1:
                child1.genes[i] = parent2.genes[i]
            if child2.genes[i] == -1:
                child2.genes[i] = parent1.genes[i]
                
        return child1,child2

def cycle_crossover(parent1, parent2) :
    n = parent1.length        
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,2), n)  
    
    child1.genes[0] = parent1.genes[0]
    child2.genes[0] = parent2.genes[0]  
    
    index = 0
    while True:
        tuplee = np.where(parent1.genes == parent2.genes[index])
        if child1.genes[tuplee[0][0]] == -1 :
            child1.genes[tuplee[0][0]] = parent2.genes[index]
            index = tuplee[0][0]
        else :
            break

    index = 0
    while True:
        tuplee = np.where(parent2.genes == parent1.genes[index])
        if child2.genes[tuplee[0]] == -1 :
            child2.genes[tuplee[0]] = parent1.genes[index]
            index = tuplee[0]
        else :
            break
    
    for i in range(n) :
        if child1.genes[i] == -1 :
            child1.genes[i] = parent2.genes[i]
            
    for i in range(n) :
        if child2.genes[i] == -1 :
            child2.genes[i] = parent1.genes[i]
    
    return child1,child2

def alternating_edges_crossover(parent1, parent2) :
    n = parent1.length
    child1 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    child2 = Chromosome(np.full(n,-1), np.random.randint(1,100), n)
    
    child1.genes[0] = parent1.genes[0]
    child2.genes[0] = parent2.genes[0]
        
    for i in range(1,n) :
        if i%2 == 1:
            if not parent1.genes[(list(parent1.genes).index(child1.genes[i-1]) + 1)%n] in child1.genes :
                child1.genes[i] = parent1.genes[(list(parent1.genes).index(child1.genes[i-1]) + 1)%n]
            else:
                rand = np.random.randint(0,n)
                while parent1.genes[rand] in child1.genes :
                    rand = np.random.randint(0,n)
                child1.genes[i] = parent1.genes[rand]
        
            if not parent2.genes[(list(parent2.genes).index(child2.genes[i-1]) + 1)%n] in child2.genes :
                child2.genes[i] = parent2.genes[(list(parent2.genes).index(child2.genes[i-1]) + 1)%n]
            else:
                rand = np.random.randint(0,n)
                while parent2.genes[rand] in child2.genes :
                    rand = np.random.randint(0,n)
                child2.genes[i] = parent2.genes[rand]
                    
                    
        else:
            if not parent2.genes[(list(parent2.genes).index(child1.genes[i-1]) + 1)%n] in child1.genes :
                child1.genes[i] = parent2.genes[(list(parent2.genes).index(child1.genes[i-1]) + 1)%n]
            else:
                rand = np.random.randint(0,n)
                while parent2.genes[rand] in child1.genes :
                    rand = np.random.randint(0,n)
                child1.genes[i] = parent2.genes[rand]
        
            if not parent1.genes[(list(parent1.genes).index(child2.genes[i-1]) + 1)%n] in child2.genes :
                child2.genes[i] = parent1.genes[(list(parent1.genes).index(child2.genes[i-1]) + 1)%n]
            else:
                rand = np.random.randint(0,n)
                while parent1.genes[rand] in child2.genes :
                    rand = np.random.randint(0,n)
                child2.genes[i] = parent1.genes[rand]                     
                    
    return child1, child2