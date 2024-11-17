import random
from game.knight import Knight

class Population:
  def __init__(self, population_size):
      self.population_size = population_size
      self.generation = 1
      self.knights = [Knight() for _ in range(self.population_size)]

  def check_population(self):
      for knight in self.knights:
          knight.check_moves()

  def evaluate(self):
      for knight in self.knights:
          knight.evaluate_fitness()
      max_fitness_knight = max(self.knights, key=lambda knight: knight.fitness)
      return max_fitness_knight.fitness, max_fitness_knight

  def tournament_selection(self, tournament_size=3):
      tournament = random.sample(self.knights, tournament_size)
      tournament.sort(key=lambda knight: knight.fitness, reverse=True)
      return tournament[:2]

  def create_new_generation(self):
      new_population = []
      while len(new_population) < self.population_size:
          parent1, parent2 = self.tournament_selection() 
          offspring1_chromosome, offspring2_chromosome = parent1.chromosome.crossover(parent2.chromosome)
          offspring1_chromosome.mutation()
          offspring2_chromosome.mutation()
          offspring1 = Knight(offspring1_chromosome)
          offspring2 = Knight(offspring2_chromosome)
          new_population.extend([offspring1, offspring2])
      self.knights = new_population[:self.population_size]
      self.generation += 1