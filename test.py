from initialize import *


class Course:

    def __init__(self):
        self.module_ID = mD.get_module_Code
        self.course_Code = mD.get_module_Course_ID
        self.lecturer = mD.get_module_lecturer

    def __str__(self):
        return [self.module_ID, self.course_Code, self.lecturer]

    def __hash__(self):
        return hash(self.module_ID)


def main():
    crs = Course()
    print(crs.__hash__())


if __name__ == '__main__':
    main()
