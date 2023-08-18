import random

# Genetic Algorithm Parameters
TARGET_STRING = "HELLO, GENETIC ALGORITHM!"
POPULATION_SIZE = 100
MUTATION_RATE = 0.1

# Create initial population
def create_initial_population(population_size, target_length):
    population = []
    for _ in range(population_size):
        individual = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ,') for _ in range(target_length))
        population.append(individual)
    return population

# Calculate fitness of each individual
def calculate_fitness(individual, target):
    return sum(1 for i, j in zip(individual, target) if i == j)

# Select parents for crossover based on fitness
def select_parents(population, target):
    parents = []
    for _ in range(2):
        candidates = random.choices(population, weights=[calculate_fitness(ind, target) for ind in population], k=2)
        parents.append(max(candidates, key=lambda ind: calculate_fitness(ind, target)))
    return parents

# Perform crossover
def crossover(parent1, parent2):
    split_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    return child1, child2

# Perform mutation
def mutate(individual):
    mutated_individual = ''
    for char in individual:
        if random.random() < MUTATION_RATE:
            mutated_individual += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ,')
        else:
            mutated_individual += char
    return mutated_individual

# Main Genetic Algorithm
def genetic_algorithm(target_string, population_size, mutation_rate, generations):
    population = create_initial_population(population_size, len(target_string))
    
    for generation in range(generations):
        population.sort(key=lambda ind: calculate_fitness(ind, target_string), reverse=True)
        
        if calculate_fitness(population[0], target_string) == len(target_string):
            print("Target string found in generation", generation)
            break
        
        new_population = [population[0]]  # Elitism
        
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, target_string)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])
        
        population = new_population
    print(population)
# Run the genetic algorithm
genetic_algorithm(TARGET_STRING, POPULATION_SIZE, MUTATION_RATE, generations=1000)
