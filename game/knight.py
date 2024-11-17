import random
from genetic.chromosome import Chromosome  # Assurez-vous que Chromosome.py est dans le même répertoire

class Knight:
    def __init__(self, chromosome=None):
      self.position = (0, 0)
      self.chromosome = chromosome if chromosome is not None else Chromosome()
      self.path = [self.position] if chromosome is None else [(0, 0)] 
      self.fitness = 0
      

      self.moves = {
          1: (1, -2),  # up-right
          2: (2, -1),  # right-up
          3: (2, 1),   # right-down
          4: (1, 2),   # down-right
          5: (-1, 2),  # down-left
          6: (-2, 1),  # left-down
          7: (-2, -1), # left-up
          8: (-1, -2)  # up-left
      }

    def move_forward(self, direction):
      x, y = self.position
      if direction in self.moves:
          dx, dy = self.moves[direction]
          new_position = (x + dx, y + dy)
          return new_position
      else:
          raise ValueError("Invalid direction. Must be an integer between 1 and 8.")

    def move_backward(self):
      if len(self.path) > 1:
          self.path.pop()
          self.position = self.path[-1]
      else:
          raise ValueError("Cannot move backward from the initial position.")

    def is_valid_move(self, position):
        x, y = position
        return (0 <= x < 8 and 0 <= y < 8) and position not in self.path

    def check_moves(self):
      cycle_direction = random.choice(['forward', 'backward'])
      for i in range(len(self.chromosome.genes)):
          move = self.chromosome.genes[i]
          next_position = self.move_forward(move)
          if not self.is_valid_move(next_position):
              found_valid_move = False
              if cycle_direction == 'forward':
                  for new_move in range(move + 1, move + 9):
                      adjusted_move = (new_move - 1) % 8 + 1
                      next_position = self.move_forward(adjusted_move)
                      if self.is_valid_move(next_position):
                          self.chromosome.genes[i] = adjusted_move  
                          self.position = next_position
                          self.path.append(self.position)
                          found_valid_move = True
                          break
              else:
                  for new_move in range(move - 1, move - 9, -1):
                      adjusted_move = (new_move - 1) % 8 + 1
                      next_position = self.move_forward(adjusted_move)
                      if self.is_valid_move(next_position):
                          self.chromosome.genes[i] = adjusted_move  # Remplacer dans le chromosome
                          self.position = next_position
                          self.path.append(self.position)
                          found_valid_move = True
                          break
              if not found_valid_move:
                  pass
          else:
              self.position = next_position
              self.path.append(self.position)

    def evaluate_fitness(self):
      self.fitness = len(self.path)
      return self.fitness