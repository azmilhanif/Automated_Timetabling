class Lecturer(object):

    def __init__(self, lecturer_ID, lecturer_Name):
        self._lecturer_ID = lecturer_ID
        self._lecturer_Name = lecturer_Name

    @property
    def get_staff_id(self):
        return self._lecturer_ID

    @property
    def get_staff_name(self):
        return self._lecturer_Name

    @property
    def __str__(self):
        return '{}, {} '.format(self._lecturer_ID, self._lecturer_Name)
