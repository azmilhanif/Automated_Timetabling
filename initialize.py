import pandas as pd

from Data import data as Input_Main
from Data.Group import Group
from Data.Module import Module
from Data.Professor import Lecturer
from Data.Room import room_test
from Data.Time import Time

mD = Module(Input_Main.ModuleFile.module_Code,
            Input_Main.ModuleFile.Lecturer_ID,
            Input_Main.ModuleFile.module_Name,
            Input_Main.ModuleFile.groupID,
            Input_Main.ModuleFile.Course_ID)

rM = room_test(Input_Main.roomfile.room_ID,
               Input_Main.roomfile.room_Name,
               Input_Main.roomfile.seating_Capacity)

lT = Lecturer(Input_Main.staffFile.staffID,
              Input_Main.staffFile.Name)

gP = Group(Input_Main.groupFile.groupID,
           Input_Main.groupFile.Level,
           Input_Main.groupFile.Semester,
           Input_Main.groupFile.no_Of_Students,
           Input_Main.groupFile.Course_ID)

tM = Time(Input_Main.TimeFile.TimeID,
          Input_Main.TimeFile.TimeSlot,
          Input_Main.TimeFile.Details)


