class Student:
    def __init__(self, name, focus1, focus2, adviser):
        self.name = name
        self.adviser = adviser
        self.focus1 = focus1
        self.focus2 = focus2
        self.focus_t = []
        self.focus1_t = []
        self.focus2_t = []
        self.test_hour = None
        self.test_hour_parsed = [1,2]
class Teacher:
    def __init__(self, name, focus1, focus2, days, hours):
        self.name = name
        self.focus1 = focus1
        self.focus2 = focus2
        self.students = {}
        self.days = days
        self.hours_days = hours
        self.hours_taken = []
        self.first_pass = False
        # add focus2 feature later
        # self.focus2 = ""
        # self.student1 = ""
        # self.student1_obj = ""
        # self.student1_time = ""
        # self.student2 = ""
        # self.student2_obj = ""
        # self.student2_time = ""
        # self.student3 = ""
        # self.student3_obj = ""
        # self.student3_time = ""
