import json
import os
import csv
from algorithms.backtracking import backtracking
from algorithms.genetic import genetic_algorithm
from algorithms.ant_colony import ant_colony_optimization
from algorithms.particle_swarm import particle_swarm_optimization
from algorithms.brute_force import brute_force

class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = []

    def backtracking(self, row):
        self.board = []
        return backtracking(self, row)

    def genetic_algorithm(self):
        self.board = []
        population_size, max_generations, mutation_rate, success = genetic_algorithm(self)
        return success, {'population_size': population_size, 'max_generations': max_generations, 'mutation_rate': mutation_rate}

    def ant_colony_optimization(self):
        self.board = []
        num_ants, num_iterations, alpha, beta, evaporation_rate, pheromone_constant, success = ant_colony_optimization(self)
        return success, {'num_ants': num_ants, 'num_iterations': num_iterations, 'alpha': alpha, 'beta': beta, 'evaporation_rate': evaporation_rate, 'pheromone_constant': pheromone_constant}
    
    def brute_force(self):
        self.board = []
        return brute_force(self)
    
    def particle_swarm_optimization(self):
        self.board = []
        num_particles, max_iterations, inertia_weight, cognitive_weight, social_weight, success = particle_swarm_optimization(
            self)
        return success, {
            'num_particles': num_particles,
            'max_iterations': max_iterations,
            'inertia_weight': inertia_weight,
            'cognitive_weight': cognitive_weight,
            'social_weight': social_weight
        }

    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
            self.board[i] - i == col - row or \
            self.board[i] + i == col + row:
                return False
        return True

    def calculate_attacks(self, state):
        attacks = [0] * len(state)  # Ensure attacks list matches state length
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or \
                        state[i] - i == state[j] - j or \
                        state[i] + i == state[j] + j:
                    attacks[i] += 1
                    attacks[j] += 1
        return attacks

    def log_run_info(self, algorithm, execution_time, success, additional_info=None):
        run_info = {
            'algorithm': algorithm,
            'execution_time': execution_time,
            'success': success,
            'board': self.board,
            'N': self.N
        }

        if additional_info:
            run_info.update(additional_info)

        # Log to JSON file
        log_file = 'nqueens_run_metrics.json'
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                try:
                    log_data = json.load(f)
                except json.JSONDecodeError:
                    log_data = []
        else:
            log_data = []
        log_data.append(run_info)
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=4)

        # Log to CSV file
        csv_file = 'nqueens_run_metrics.csv'
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=run_info.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(run_info)
