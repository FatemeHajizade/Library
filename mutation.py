import numpy as np

def uniform_mutation(child):
    for i in range(0,child.length):
        mutate = np.random.randint(0,1)
        if(mutate>0.5):
            if(child.genes[i]==1):
                child.genes[i]=0
            else:
                child.genes[i]=1
    return child

def inorder_mutation(chromosome, mp) :
     start = np.random.randint(0,chromosome.length)
     stop = np.random.randint(start,chromosome.length)
     for i in range(start, stop) :
         if np.random.uniform(0,1) < mp :
             if chromosome.genes[i] == 1 :
                 chromosome.genes[i] = 0
             else:
                 chromosome.genes[i] = 1
     return chromosome

def twors_mutation(chromosome) :
    rand_index1 = np.random.randint(0,chromosome.length)
    rand_index2 = np.random.randint(0,chromosome.length) 
    while rand_index1 == rand_index2 :
        rand_index2 = np.random.randint(0,chromosome.length)      
    chromosome.genes[rand_index1], chromosome.genes[rand_index2] = chromosome.genes[rand_index2], chromosome.genes[rand_index1]
    return chromosome

def centre_inverse(chromosome, mp) :
    if np.random.uniform(0,1) < mp :
        section1 = np.random.randint(0,chromosome.length)
        sec1 = chromosome.genes[section1::-1] #inversing!
        sec2 = chromosome.genes[:section1:-1]
        chromosome.genes = np.concatenate(sec1,sec2)
        return chromosome
    else:
        return chromosome

def reverse_sequence_mutation(chromosome) :
    rand_index1 = np.random.randint(0,chromosome.length)
    rand_index2 = np.random.randint(0,chromosome.length)  
    while rand_index1 == rand_index2 :
        rand_index2 = np.random.randint(0,chromosome.length)   
    if rand_index2 < rand_index1 :
        rand_index1, rand_index2 = rand_index2, rand_index1      
    i = 0
    while i <= ((rand_index2 - rand_index1 + 1)/2) :
        chromosome.genes[rand_index1 + i], chromosome.genes[rand_index2 - i] = chromosome.genes[rand_index2 - i], chromosome.genes[rand_index1 + i]
        i += 1       
    return chromosome


def throas_mutation(child):
    select = np.random.randint(0,child.length)
    print(select)
    temp = child.genes[select]
    child.genes[select] = child.genes[(select+2)%child.length]
    child.genes[(select+2)%child.length] = temp
    return child

def thrors_mutation(child):
    select = np.zeros(3)
    for i in range(0,3):
        select[i] = np.random.randint(0,child.length)
    select = sorted(select)
    temp1 = child.genes[select[0]]
    temp2 = child.genes[select[1]]
    child.genes[select[0]] = child.genes[select[2]]
    child.genes[select[1]] = temp1
    child.genes[select[2]] = temp2
    return child
    
def partial_shuffle_mutation(chromosome, mp):
    for i in range (1, chromosome.length) :
        p = np.random.uniform(0,1)
        if p < mp :
            j = np.random.randint(i, chromosome.length)
            chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
    return chromosome

def distance_based_mutation(chromosome, gene, distance) :
    g = np.where(chromosome.genes == gene)
    if (g[0]-distance)%chromosome.length < (g[0]+distance)%chromosome.length :
        chromosome.genes[g[0]] = chromosome.genes[np.random.randint((g[0]-distance)%chromosome.length, (g[0]+distance)%chromosome.length)]
    else:
        chromosome.genes[g[0]] = chromosome.genes[np.random.randint((g[0]+distance)%chromosome.length, (g[0]-distance)%chromosome.length)]
    return chromosome