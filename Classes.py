import random

from initialize import *


# Combines all the required information
class Class_Session(object):

    def __init__(self):

        # Try this
        self.group_ID = []
        self.module_ID = []
        self.lecturer_ID = []
        self.room_ID = []
        self.time_ID = []
        # End here

        self._Class = []
        self.number_of_Students = []

        self.group_Size = 0

    def create_Class(self):

        for x in mD.get_module_Code:
            self.module_ID.append(x)

        for j in rM.get_id:
            self.room_ID.append(j)

        for t in tM.get_timeID:
            self.time_ID.append(t)

        for i in gP.get_groupSize:
            self.number_of_Students.append(i)

        for z in mD.get_module_lecturer:
            self.lecturer_ID.append(z)

        # Random Module
        mod = random.choice(range(len(self.module_ID)))
        module = self.module_ID[mod]

        # course
        crs = mD.get_module_Course_ID[mod]

        # Random room
        rom = random.choice(range(len(self.room_ID)))
        room_ID = self.room_ID[rom]

        # random time
        tim = random.choice(range(len(self.time_ID)))
        time_Slot = self.time_ID[tim]

        # lecturer
        lec = self.lecturer_ID[mod]

        self._Class = [[module, crs, lec], [room_ID], [time_Slot]]

        return self._Class


def main():
    cs = Class_Session()
    print(cs.create_Class())


if __name__ == '__main__':
    main()
