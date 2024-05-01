# nqueen.py
import random
import math

class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = []

    def backtracking(self, row):
        if row == self.N:
            return True
        for col in range(self.N):
            if self.is_valid(row, col):
                self.board.append(col)
                if self.backtracking(row + 1):
                    return True
                self.board.pop()
        return False

    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
            self.board[i] - i == col - row or \
            self.board[i] + i == col + row:
                return False
        return True

    def genetic_algorithm(self):
        population_size = 100
        mutation_rate = 0.1
        max_generations = 1000

        def generate_individual():
            return [random.randint(0, self.N - 1) for _ in range(self.N)]

        def crossover(parent1, parent2):
            crossover_point = random.randint(1, self.N - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2

        def mutate(individual):
            if random.random() < mutation_rate:
                individual[random.randint(0, self.N - 1)] = random.randint(0, self.N - 1)
            return individual

        population = [generate_individual() for _ in range(population_size)]
        for generation in range(max_generations):
            population = sorted(population, key=lambda x: sum(self.calculate_attacks(x)))
            if sum(self.calculate_attacks(population[0])) == 0:
                self.board = population[0]
                return True
            next_generation = population[:10]
            while len(next_generation) < population_size:
                parent1, parent2 = random.sample(population[:50], 2)
                child1, child2 = crossover(parent1, parent2)
                next_generation.append(mutate(child1))
                next_generation.append(mutate(child2))
            population = next_generation[:]
        return False

    def simulated_annealing(self):
        def probability(delta_e, T):
            return 1 if delta_e < 0 else math.exp(-delta_e / T)

        def generate_neighbor(state):
            neighbor = state[:]
            row = random.randint(0, self.N - 1)
            col = random.randint(0, self.N - 1)
            neighbor[row] = col
            return neighbor

        current_state = self.board[:] if self.board else [random.randint(0, self.N - 1) for _ in range(self.N)]
        T = 1.0
        T_min = 0.0001
        alpha = 0.9
        while T > T_min:
            new_state = generate_neighbor(current_state)
            current_attacks = self.calculate_attacks(current_state)
            new_attacks = self.calculate_attacks(new_state)
            delta_e = sum(new_attacks) - sum(current_attacks)
            if probability(delta_e, T) > random.random():
                current_state = new_state[:]
            T *= alpha
        if sum(self.calculate_attacks(current_state)) == 0:
            self.board = current_state[:]
            return True
        return False

    def hill_climbing(self):
        def calculate_attacks(state):
            attacks = [0] * self.N
            for i in range(self.N):
                for j in range(i + 1, self.N):
                    if state[i] == state[j] or \
                            state[i] - i == state[j] - j or \
                            state[i] + i == state[j] + j:
                        attacks[i] += 1
                        attacks[j] += 1
            return attacks

        def generate_neighbors(state):
            neighbors = []
            for i in range(self.N):
                for j in range(self.N):
                    if state[i] != j:
                        neighbor = state[:]
                        neighbor[i] = j
                        neighbors.append(neighbor)
            return neighbors

        current_state = self.board[:] if self.board else [random.randint(0, self.N - 1) for _ in range(self.N)]
        current_attacks = calculate_attacks(current_state)
        while True:
            neighbors = generate_neighbors(current_state)
            best_neighbor = None
            best_attacks = float('inf')
            for neighbor in neighbors:
                neighbor_attacks = calculate_attacks(neighbor)
                if sum(neighbor_attacks) < best_attacks:
                    best_neighbor = neighbor[:]
                    best_attacks = sum(neighbor_attacks)
            if best_attacks < sum(current_attacks):
                current_state = best_neighbor[:]
                current_attacks = calculate_attacks(current_state)
            else:
                break
        if sum(current_attacks) == 0:
            self.board = current_state[:]
            return True
        return False


    def calculate_attacks(self, state):
        attacks = [0] * self.N
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or \
                        state[i] - i == state[j] - j or \
                        state[i] + i == state[j] + j:
                    attacks[i] += 1
                    attacks[j] += 1
        return attacks
