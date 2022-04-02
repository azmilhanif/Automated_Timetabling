class Module(object):

    def __init__(self, module_code, lecturer_ID, module_name, groupID, course_id):
        self._module_code = module_code
        self.module_name = module_name
        self.lecturer_ID = lecturer_ID
        self.groupID = groupID
        self.course_ID = course_id

    @property
    def get_module_Code(self):
        return self._module_code

    @property
    def get_module_name(self):
        return self.module_name

    @property
    def get_module_Course_ID(self):
        return self.course_ID

    @property
    def get_student_Group_ID(self):
        return self.groupID

    @property
    def get_module_lecturer(self):
        return self.lecturer_ID

    def module_Dictionary(self):
        res = dict(zip(self.get_module_Code, self.get_module_name))
        return res


    def __str__(self):
        return '{}, {}, {}, {}, {} '.format(self._module_code,
                                            self.module_name, self.groupID,
                                            self.lecturer_ID,
                                            self.course_ID)
