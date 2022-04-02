import random

import Visualizer
import timetable

tL = timetable.Timetable()


class GeneticAlgorithm:
    # Parameters
    POPULATION_size = 100  # this will return : 15 individual classes(1 timetable) * Population_Size
    CROSSOVER_POINT = 1  # Just do single-point crossover for now (can change this, but it gets complicated)
    MAX_GENERATIONS = 10

    def __init__(self):

        # initialize parameters
        self.Generation = 0
        self.Crossover = self.CROSSOVER_POINT
        self.max_generations = self.MAX_GENERATIONS

        self.best_SOL = None
        self.found_Solution = False
        self.new_generation = False

        # Containers
        self.mating_Pool = []
        self.population = []
        self.new_population = []

    # Create populations of random timetables
    def initiate_Populations(self):

        # create timetable in the size declared above
        population = [tL.create_timetables() for _ in range(self.POPULATION_size)]
        self.population.append(population)

        # take whole populations of the first generation to select an individual to be evaluated
        self.evaluate_Individuals_From_Population(population)

    # check all timetables from the generated populations if there are any fit schedules
    def evaluate_Individuals_From_Population(self, population):

        # random selection of an individual (timetable)
        random_tables = random.choice(population)

        # if a solution is  found
        if tL.fitness_(tL.clash_Calculation(random_tables)) != "Pass":
            self.found_Solution = True
            self.best_SOL = random_tables
            self.Best_Solution()

        # else loop until found solution
        while not self.found_Solution and self.Generation < self.max_generations:
            self.Generation += 1

            print('Generation:', self.Generation, 'Fitness Score:', tL.fitness_Score)
            self.selection_by_Roulette(population)

    # FIX THESE!!!! ADD UP ALL THE TOTAL SCORE IN THE POPULATION AND SO ON.....
    def selection_by_Roulette(self, population):

        random_selection_1 = random.choice(population)
        random_selection_2 = random.choice(population)

        parent_1 = []
        parent_2 = []

        for i in random_selection_1:
            parent_1.append(i)

        for j in random_selection_2:
            parent_2.append(j)

        self.mating_Pool.append(parent_1)
        self.mating_Pool.append(parent_2)

        self.crossover_Chromo(random.choice(parent_1), random.choice(parent_2), self.CROSSOVER_POINT)

    def crossover_Chromo(self, Parent_1, Parent_2, crossover_point):

        # chromosome in list
        print("parent_M:", Parent_1)
        print("parent_F:", Parent_2)

        Selection_1 = Parent_1[:]
        Selection_2 = Parent_2[:]

        for i in range(crossover_point, len(Selection_1)):
            Selection_1[i], Selection_2[i] = Selection_2[i], Selection_1[i]

            print("Offspring 1:", Selection_1)
            print("Offspring 2:", Selection_2)

            while range(len(self.mating_Pool) < self.POPULATION_size):

                self.new_population.append(Selection_1)
                self.new_population.append(Selection_2)
                self.evaluate_Individuals_From_Population(self.population)

            else:
                self.evaluate_Individuals_From_Population(self.mating_Pool)

    # DON'T FORGET THIS!!!! TRY THIS
    def Mutation(self):
        pass

    # if solution has been found
    def Best_Solution(self):
        print('Generation: ', self.Generation, '\n',
              'Fitness Score:', tL.fitness_Score, '\n',
              'Chromosome:', self.best_SOL)

        vsl = Visualizer.Visualizer()
        vsl.append_to_timetable(self.best_SOL)


def main():
    ga = GeneticAlgorithm()
    ga.initiate_Populations()


main()
