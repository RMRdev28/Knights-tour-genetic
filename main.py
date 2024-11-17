from genetic.population import Population
from visualization.visualize import Visualize
import config


def main():
    population = Population(config.POPULATION_SIZE)
    while True:
        population.check_population()
        maxFit, bestSolution = population.evaluate()
        print(f"Génération {population.generation} - Meilleure aptitude: {maxFit}")
        if maxFit == 64:
            print(f"Solution trouvée en {population.generation} générations")
            break
        population.create_new_generation()

    visualize = Visualize()
    visualize.display_game(bestSolution)

if __name__ == "__main__":
  main()