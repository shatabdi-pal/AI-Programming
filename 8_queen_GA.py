#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


POPULATION_SIZE = 1000
#MUTATION_RATE = 0.03
MUTATION_RATE = 0.50



#nq = int(input("Enter Number of Queens: "))  
nq = 8
maxFitness = (nq * (nq - 1)) / 2  


# In[3]:


def generate_chromosome(nq):  
    return [random.randint(1, nq) for x in range(nq)]


# In[4]:


def generate_population():
    return [generate_chromosome(nq) for x in range(POPULATION_SIZE)]


# In[5]:


def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))  


# In[6]:


def selection_probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness


# In[7]:


def selection(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"


# In[8]:


def crossover(x, y):  
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


# In[9]:


def mutate(x):  
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


# In[10]:


def genetic_algorithm(population, fitness):
    new_population = []
    probabilities = [selection_probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = selection(population, probabilities)  
        y = selection(population, probabilities) 
        child = crossover(x, y) 
        if random.random() < MUTATION_RATE:
            child = mutate(child)
        print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population


# In[11]:


def print_chromosome(chrom):
    print("Chromosome = {},  Fitness = {}"
          .format(str(chrom), fitness(chrom)))


# In[12]:


population = generate_population()

generation = 1
avg_fitness = []
generation_num = []

while not maxFitness in [fitness(chrom) for chrom in population]:
    print("=== Generation {} ===".format(generation))
    population = genetic_algorithm(population, fitness)
    print("")
    avg = np.mean([fitness(n) for n in population])
    #avg = max([fitness(n) for n in population])
    avg_fitness.append(avg)
    generation_num.append(generation)
    print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
    generation += 1
chrom_out = []
print("Solved in Generation {}".format(generation - 1))
for chrom in population:
    if fitness(chrom) == maxFitness:
        print("")
        print("One of the solutions: ")
        chrom_out = chrom
        print_chromosome(chrom)


# In[13]:


board = []

for x in range(nq):
    board.append(["*"] * nq)

for i in range(nq):
    board[nq - chrom_out[i]][i] = "Q"


# In[14]:


def print_board(board):
    for row in board:
        print(" ".join(row))


print()
print_board(board)


# In[15]:



x = np.array(generation_num)
y = np.array(avg_fitness)
plt.title("Average Fitness to the population (size: 1000) generation number")
plt.xlabel("Generation number")
plt.ylabel("Average fitness")

plt.plot(x, y)
plt.show()


# In[ ]:





# In[ ]:




