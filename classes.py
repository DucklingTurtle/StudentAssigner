class Student:
    def __init__(self, name, focus1, focus2):
        self.name = name
        self.adviser = "Run teacher matcher"
        self.focus1 = focus1
        self.focus2 = focus2
        self.focus1_teachers = ["Run teacher matcher to get result!"]
        self.focus2_teachers = ["Run teacher matcher"]

class Teacher:
    def __init__(self, name, focus, hours):
        self.name = name
        self.focus = focus
        self.hours = hours
        self.student = ""
