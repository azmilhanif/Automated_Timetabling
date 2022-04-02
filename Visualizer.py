import dataframe_image as dfi
import pandas as pd

from initialize import *


class Visualizer:

    def __init__(self):
        # this creates the structure of the timetable
        self.df = pd.DataFrame(columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                               index=['9:30AM - 12:30PM', '12:00PM - 2:00PM', '2:00PM - 5:00PM'])

        self.cols = {'M': 'Monday', 'T': 'Tuesday', 'W': 'Wednesday',
                     'TH': 'Thursday', 'F': 'Friday'}

        self.rows = self.df.index.tolist()

    # insert selected chromosomes from genetic algorithm to empty timetable

    # Code from StackOverflow (Corralien, 2022)
    def get_loc(self, code):
        m, t = code.split('TM')
        col = self.cols[m]
        row = self.rows[int(t) - 1]
        return row, col

    # get the finalized timetable
    def append_to_timetable(self, solution):
        # Decode each element of the list
        mi = pd.MultiIndex.from_tuples(tuple(self.get_loc(x[2][0]) for x in solution),
                                       names=['row', 'col'])

        out = pd.Series([solution]).explode().to_frame('data').set_index(mi).reset_index() \
            .pivot_table('data', 'row', 'col', aggfunc=list, fill_value='') \
            .reindex(index=self.df.index, columns=self.df.columns, fill_value='')
    # End of retrieved code

        pd.set_option('max_colwidth', 800)
      

        return dfi.export(out, r"output/BSC Computer Science.png")
