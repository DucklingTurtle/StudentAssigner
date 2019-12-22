class Student:
    def __init__(self, name, focus1, focus2, adviser):
        self.name = name
        self.adviser = adviser
        self.focus1 = focus1
        self.focus2 = focus2
        self.focus1_teachers = []
        self.focus2_teachers = []
        self.focus1_hour = []
        self.focus2_hour = []
        self.hours = {}
        self.hours_cant = []

class Teacher:
    def __init__(self, name, focus, hours):
        self.name = name
        self.focus = focus
        # add focus2 feature later
        self.focus2 = ""
        self.hours = hours
        self.student1 = ""
        self.student1_obj = ""
        self.student2 = ""
        self.student2_obj = ""
        self.student3 = ""
        self.student3_obj = ""
