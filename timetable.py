import numpy as np
from numpy.ma.bench import xs

import Classes
from initialize import *


# Encapsulates all objects
class Timetable(object):

    def __init__(self):
        self.fit = None
        self.modules = []
        self.Slots = []
        self._Class = None
        self.clashes = 1

        self.fitness_Score = None
        self.number_of_classes = len(mD.get_module_Code)

    def create_Sessions(self):

        cL = Classes.Class_Session()
        self._Class = (cL.create_Class())

        return self._Class

    # For every timetable, do evaluation
    def create_timetables(self):

        # Random classes
        self.Slots = [self.create_Sessions() for _ in range(self.number_of_classes)]

        return self.Slots

    def clash_Calculation(self, classes):

        clashes = 0

        #     module_mapper = map(lambda x: tuple(x[0]), classes)
        #     unique_modules = set(module_mapper)
        #
        #     duplicate_counter = len(unique_modules) - len(xs)
        #
        #     print(classes)
        #     print(duplicate_counter)
        #
        # def filter_condition(self, x, y):
        #     return x != y and y[1:] == y[1:]
        #
        # def filterer(self, classes, acc=None):
        #     if acc is None:
        #         acc = []
        #
        #     if classes:
        #         c, cs = classes[0], classes[1:]
        #         if c not in acc:
        #             filtered_classes = list(filter(lambda x: self.filter_condition(c, x), cs))
        #             if filtered_classes:
        #                 acc.extend(filtered_classes + [c])
        #         return self.filterer(cs, acc)
        #     else:
        #         return acc

        self.clashes += clashes
        self.fitness_(self.clashes)

        return self.clashes

    def fitness_(self, clashes):

        self.fitness_Score = 1 / clashes

        # fittest = 1 / (total number of clashes)       1/2. if 0.5 == unfit

        if self.fitness_Score == 1.0:
            self.fit = "Pass"

        elif self.fitness_Score < 1:
            self.fit = "Fail"

        self.get_fitness_bool()
        return self.fit

    def get_fitness_bool(self):
        return self.fit

    def get_fitness_Score(self):
        return self.clashes

    def return_timetable(self, classes, score):
        return classes, score


def main():
    tbl = Timetable()
    print(tbl.create_timetables())
    print(tbl.clash_Calculation(tbl.create_timetables()))


if __name__ == '__main__':
    main()
