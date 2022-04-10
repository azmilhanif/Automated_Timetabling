import itertools
import random
import threading

import PySimpleGUI as sg

import Visualizer
import timetable

tL = timetable.Timetable()

layout = [[sg.Column([[sg.Text("BSc Computer Science timetable generator")],
                      [sg.Button("Generate course timetable")],
                      [sg.Button("View generated timetable")]],
                     element_justification='c')],
          ]

layout = [[sg.Column(layout, element_justification='c', vertical_alignment='center')]]
window = sg.Window(title="Computer Science", layout=layout, element_justification='c', resizable=True)
# window = sg.Window(title="Computer Science", layout=layout, size=(500, 500), element_justification='c')


# ----------------------------- EVENT LOOP -----------------------------------
while True:

    class GeneticAlgorithm:
        # Parameters
        POPULATION_size = 10  # this will return : 15 individual classes(1 timetable) * Population_Size
        ITERATIONS = 10  # Max number of loops to find best_Solution??? IDK this didn't change anything
        CROSSOVER_POINT = 2
        MUTATION_RATE = 0.5

        def __init__(self):

            # initialize parameters
            self.Generation = 0
            self.Crossover = self.CROSSOVER_POINT
            self.Iterations = self.ITERATIONS

            self.best_SOL = None
            self.found_Solution = False

            # Populations
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
            if tL.fitness_(tL.clash_Calculation(random_tables)) == "Pass":
                self.found_Solution = True
                self.best_SOL = random_tables
                self.Best_Solution()

            # else loop until found solution
            while not self.found_Solution:
                self.Generation += 1

                print('Generation# :', self.Generation, 'Fitness Score:', tL.fitness_Score)

                self.selection_by_Roulette(population)

        def selection_by_Roulette(self, population):
            reselect = False
            while not reselect:

                # for x in population:
                random_selection_1 = random.choice(population)
                random_selection_2 = random.choice(population)

                if random_selection_2 == random_selection_1:
                    reselect = True

                else:

                    parent_1 = []
                    parent_2 = []

                    for i in random_selection_1:
                        # for y in i:
                        parent_1.append(i)
                    for j in random_selection_2:
                        # for z in j:
                        parent_2.append(j)

                    self.crossover_Chromo(parent_1, parent_2, self.CROSSOVER_POINT)

        def crossover_Chromo(self, random_Selection_1, random_Selection_2, crossover_point):

            c1 = []
            c2 = []

            # chromosome in list
            print("parent_M:", random_Selection_1)
            print("parent_F:", random_Selection_2)

            merged = list(itertools.chain.from_iterable(random_Selection_1))
            parent1 = list(itertools.chain.from_iterable(merged))

            # print(parent1)

            # parent_1_Chromo = ''.join(map(str, final))
            # print(parent_1_Chromo)

            # chromosome list to string
            # parent_1_ = list(itertools.chain.from_iterable(test_list))
            # parent_1_Chromo = ''.join(map(str, parent_1_))
            #
            # print(parent_1_Chromo)

            # chromosome list to string
            # parent_1_ = list(itertools.chain.from_iterable(random_Selection_1))
            # parent_1_Chromo = ''.join(map(str, parent_1_))
            #
            # parent_2_ = list(itertools.chain.from_iterable(random_Selection_2))
            # parent_2_Chromo = ''.join(map(str, parent_2_))
            #
            # c1 = list(parent_1_Chromo)
            # c2 = list(parent_2_Chromo)
            #
            # print(c1)

            # c1 = list(random_Selection_1)
            # c2 = list(random_Selection_2)

            # interchanging the genes
            # for i in range(crossover_point, len(random_Selection_1)):
            #     c1[i], c2[i] = c2[i], c1[i]

            # for i in range(len(random_Selection_1)):
            #     c1[0], c2[0] = c2[0], c1[0]

            # c1 = ''.join(c1)
            # c2 = ''.join(c2)

            # encode crossed lists back to list to add into population
            # wrapped_c1 = textwrap.wrap(c1, 5)
            # wrapped_c2 = textwrap.wrap(c2, 5)
            #
            # length_to_split = [5, 5, 5,
            #                    5, 5, 5,
            #                    5, 5, 5,
            #                    5, 5, 5,
            #                    5, 5, 5]
            #
            # # Using islice
            #
            # offspring1 = [wrapped_c1[x - y: x] for x, y in zip(
            #     itertools.accumulate(length_to_split), length_to_split)]
            #
            # offspring2 = [wrapped_c2[x - y: x] for x, y in zip(
            #     itertools.accumulate(length_to_split), length_to_split)]
            #
            # print("Offspring 1: ", offspring1)
            # print("offspring 2: ", offspring2, "\n")
            #
            # self.population.append(offspring1)
            # self.population.append(offspring2)
            #
            # self.evaluate_Individuals_From_Population(self.population)
            # self.mutation(self.population)

            # self.new_population.extend([offspring1, offspring2])
            # self.evaluate_Individuals_From_Population(self.new_population)
            # self.mutation(self.new_population)

            return 0

        def mutation(self, children):

            if random.randint(0, 10) == self.MUTATION_RATE:
                self.new_population.append(children)

            self.evaluate_Individuals_From_Population(self.new_population)

        def Best_Solution(self):
            print('Generation# : ', self.Generation, '\n',
                  'Fitness Score:', tL.fitness_Score, '\n',
                  'Chromosome:', self.best_SOL)

            vsl = Visualizer.Visualizer()
            vsl.append_to_timetable(self.best_SOL)


    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    elif event == "Generate course timetable":
        while True:
            ga = GeneticAlgorithm()
            try:

                threading.Thread(target=ga.initiate_Populations(), args=(window,), daemon=True).start()

            except IndexError:
                print("Re-Checking")
                threading.Thread(target=ga.initiate_Populations(), args=(window,), daemon=True).start()
                continue

    elif event == 'View generated timetable':
        layout = [
            [sg.Image(filename=r"output/BSC Computer Science.png")],
            [sg.Button("Exit")]
        ]

        window = sg.Window("Image Viewer", layout)

window.close()
