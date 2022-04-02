class Group(object):

    def __init__(self, group_id, Level, Semester, no_Of_Students, course_ID):
        self.id = group_id
        self.Level = Level
        self.semester = Semester
        self._no_Of_Students = no_Of_Students
        self.course_ID = course_ID

    @property
    def get_group_id(self):
        return self.id

    @property
    def get_groupSize(self):
        return self._no_Of_Students

    @property
    def get_Course_ID(self):
        return self.course_ID


    @property
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.id, self.Level, self.semester,
                                           self._no_Of_Students, self.course_ID)
