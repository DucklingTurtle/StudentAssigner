print("Importing packages...")
import classes, teachers_sheet, students_sheet, sys, gspread, random, time, math
from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials
from collections import Counter
import xlwt, xlrd
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet("Students Assigned")

# look at itertools for algorithm optimization

# teachers sheet and student sheet
t_sheet = teachers_sheet.sheet
s_sheet = students_sheet.sheet

# sheets init
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials_studentassigner2.json", scope)
client = gspread.authorize(creds)
gc = gspread.authorize(creds)

# init
help_list = "To use app, first you must import data"
commands_list = "Student Input, Teacher Input, Assigner"
commands_student = "Create Students, See Students, Remove Student"
commands_student_stats = "Student Stats, Back"
commands_teacher = "Create Teachers, See Teachers, Remove Teacher"
commands_assigner = "Sort"
commands_assigner_sort = "Teachers"
mode = "init"
focus_list = (
    "AP", "CP", "IR", "MT", "TH"
)
students_list = [
    # classes.Student("Osvaldo Last", "AP", "IR", "Adviser 1"),
    # classes.Student("Amanda Panda", "CP", "TH", "Adviser 2")
]
teachers_list = [
    # classes.Teacher("Test_first1 Test_last2", "CP", [1, 2]),
    # classes.Teacher("Panda Amanda", "IR", [1, 3]),
    # classes.Teacher("First3 Last3", "AP", [1, 2])
]
days_list = {
}


def error_correction():
    # sh1 = gc.open("Students Sorted")
    # loc = ("StudentAssigner.xls")
    # wb1 = xlrd.open_workbook(loc)
    # sheet = wb1.sheet_by_index(0)
    # # for loops to go through array
    # for row in range(sheet.nrows):
    #     name = sheet.cell_value(row, 0)
    #     adviser = sheet.cell_value(row, 1)
    #     focus1_t_1 = sheet.cell_value(row, 2)
    #     focus1_t_2 = sheet.cell_value(row, 3)
    #     focus2_t_1 = sheet.cell_value(row, 4)
    #     focus2_t_2 = sheet.cell_value(row, 5)
    #     focus1_hour = sheet.cell_value(row, 6)
    #     focus2_hour = sheet.cell_value(row, 7)
    for student in students_list:
        s_focus1 = student.focus1
        s_focus2 = student.focus2
        t_focus1_f = student.focus1_t[0].focus1
        try:
            t_focus1_s = student.focus1_t[1].focus1
        except:
            print("No second teacher for student. Correcting...")
            for teacher in teachers_list:
                if student.focus1 == teacher.focus1 and teacher.hours_days[student.test_hour_parsed[0]]:
                    if student.test_hour_parsed[1] in teacher.hours_days[student.test_hour_parsed[0]]:
                        student.focus1_t.append(teacher)
                    else:
                        pass
        t_focus2_f = student.focus2_t[0].focus1
        try:
            t_focus2_s = student.focus2_t[1].focus1
        except:
            print("No second teacher for student. Correcting...")
            for teacher in teachers_list:
                if student.focus2 == teacher.focus2 and teacher.hours_days[student.test_hour_parsed[0]]:
                    if student.test_hour_parsed[1] in teacher.hours_days[student.test_hour_parsed[0]]:
                        student.focus2_t.append(teacher)
                    else:
                        pass
# def verify():
#     for student in students_list:
#         # for teacher in teachers_list:
#             t_list = list(student.focus1_t)
#             t_name = t_list[0]
#             t_list2 = list(student.focus2_t)
#             t_name2 = t_list2[0]
#             t_hold = list(student.focus1_t)
#             # check if focus1 matches focus1 list
#             if student.focus1 == student.focus1_obj[0].focus:
#                 pass
#             else:
#                 print("Error: Focus 1 does not match Focus 1 Obj List")
#             # check if focus1_obj = focus1_list
#             if student.focus1_obj[0].name == t_name:
#                 pass
#             else:
#                 print("Error: Focus 1 Obj != Focus 1 list")
#             # check if focus2 matches focus2 list
#             if student.focus2 == student.focus2_obj[0].focus:
#                 pass
#             else:
#                 print("Error: Focus 2 != Focus 2 List")
#             # check if focus2_obj = focus2_list
#             if student.focus2_obj[0].name == t_name2:
#                 pass
#             else:
#                 print("Error: Focus 2 Obj not in Focus 2 List")
#             # check if all focus 1 teachers have the same time
#             try:
#                 if student.focus1_t[t_hold[0]] == student.focus1_t[t_hold[1]]:
#                     pass
#                 else:
#                     print("Error: Focus 1 teachers not equal")
#             except:
#                 print(student.name + " Missing Focus 1 Second Teacher")
#                 sort_again = True
#             # check if all focus 2 teachers have the same time
#     try:
#         if sort_again is True:
#             sort()
#             # sort_again = False
#             # verify()
#             print("sort again")
#     except:
#         pass


# def match_first(focus, teacher, student):
#     # print("In match_first")
#     t_time = random.choice(teacher.hours)
#     while True:
#         if focus == 1:
#             # print("In focus 1")
#             if len(student.focus2_t) >= 1:
#                 s_teacher_list = list(student.focus2_t)
#                 name_teacher = s_teacher_list[0]
#                 if t_time != student.focus2_t[name_teacher]:
#                     break
#                 else:
#                     if len(teacher.hours) > 1:
#                         t_time = random.choice(teacher.hours)
#                     else:
#                         return
#             else:
#                 break
#         elif focus == 2:
#             if len(student.focus1_t) >= 1:
#                 # print("In focus 2")
#                 s_teacher_list = list(student.focus1_t)
#                 name_teacher = s_teacher_list[0]
#                 if t_time != student.focus1_t[name_teacher]:
#                     break
#                 else:
#                     if len(teacher.hours) > 1:
#                         t_time = random.choice(teacher.hours)
#                     else:
#                         return
#             else:
#                 break
#         else:
#             print("Error: no focus")
#             return
#     teacher.first_pass = True
#     # print("time: " + str(t_time))
#     # print("Student name: " + student.name)
#     # print("teacher name: " + teacher.name)
#     if focus == 1 and t_time not in teacher.hours_taken:
#         # add teacher to student's focus1 teachers list, time is key, teacher obj is value
#         student.focus1_t[str(teacher.name)] = t_time
#         student.focus1_obj.append(teacher)
#         # add student to teacher's student list, time is key, student obj is value
#         teacher.students[str(student.name)] = t_time
#         teacher.hours_taken.append(t_time)
#         # print("t_time: " + str(t_time))
#     if focus == 2 and t_time not in teacher.hours_taken:
#         student.focus2_t[str(teacher.name)] = t_time
#         student.focus2_obj.append(teacher)
#         teacher.students[str(student.name)] = t_time
#         teacher.hours_taken.append(t_time)

# def match_continue(focus, teacher, student):
#     if focus == 1:
#         s_teacher_list = list(student.focus1_t)
#         time_name = s_teacher_list[0]
#         time = student.focus1_t[time_name]
#         if time not in teacher.hours_taken:
#             s_teacher_list = list(student.focus1_t)
#             name_teacher = s_teacher_list[0]
#             # student
#             student.focus1_obj.append(teacher)
#             student.focus1_t[teacher.name] = student.focus1_t[name_teacher]
#             # print("teacher name: " + teacher.name)
#             # print("First teacher: " + name_teacher)
#             # print("student name: " + student.name)
#             # teacher
#             teacher.students[str(student.name)] = student.focus1_t[name_teacher]
#             teacher.hours_taken.append(time)
#             # print("hours to append: " + str(student.focus1_t[name_teacher]))
#             # print("hours taken: " + str(teacher.hours_taken))
#             # print(time)
#     if focus == 2:
#         s_teacher_list = list(student.focus2_t)
#         time_name = s_teacher_list[0]
#         time = student.focus2_t[time_name]
#         if time not in teacher.hours_taken:
#             name_teacher = s_teacher_list[0]
#             # student
#             student.focus2_obj.append(teacher)
#             student.focus2_t[teacher.name] = student.focus2_t[name_teacher]
#             # teacher
#             teacher.students[student.name] = student.focus2_t[name_teacher]
#             teacher.hours_taken.append(time)
#             # print("teacher name: " + teacher.name)
#             # print("First teacher: " + name_teacher)
#             # print("student name: " + student.name)
#             # print(teacher.hours_taken)

# def sort():
#     # run first block, then second
#     for loop in range(3):
#         for student in students_list:
#             for teacher in teachers_list:
#                 if loop == 0:
#                     if teacher.first_pass is not True:
#                         if len(student.focus1_obj) <= 0 or len(student.focus2_obj) <= 0:
#                             if not teacher.students:
#                                 if teacher.focus == student.focus1:
#                                     # print("test")
#                                     if len(student.focus1_t) <= 0:
#                                         # print(student.name)
#                                         match_first(1, teacher, student)
#                                         # print("Focus 1")
#                                 elif teacher.focus == student.focus2:
#                                     # print("test2")
#                                     if len(student.focus2_t) <= 0:
#                                         # print(student.name)
#                                         match_first(2, teacher, student)
#                                         # print("Focus 2")
#                 elif loop == 1 or loop == 2:
#                     # print("In Loop 2")
#                     # print(loop)
#                     # print(student.name)
#                     # print(teacher.name)
#                     # print(teacher.focus)
#                     # print(student.focus1)
#                     # print(student.focus2)
#                     # print(len(student.focus1_t))
#                     # print(student.focus1_t)
#                     # print(len(student.focus2_t))
#                     # print(student.focus2_t)
#                     # print("hours taken: " + str(teacher.hours_taken))
#                     # print(teacher.hours)
#                     if teacher.focus == student.focus1 and len(student.focus1_t) == 1:
#                         # print("In Focus 1 Loop 2")
#                         if teacher.name != student.focus1_obj[0].name:
#                             # print("In name comparison, Focus 1 Loop 2")
#                             # # turns student's focus1 t dictionary in a list, index = lists first obj
#                             # s_teacher_list = list(student.focus1_t)
#                             # index = s_teacher_list[0]
#                             # print(index)
#                             if student.focus1_obj[0].focus == teacher.focus:
#                                 # print("In focus = teacher focus, Focus 1 Loop 2")
#                                 s_teacher_list = list(student.focus1_t)
#                                 name_teacher = s_teacher_list[0]
#                                 if student.focus1_t[name_teacher] in teacher.hours:
#                                     # print("In any function, Focus 1 Loop 2")
#                                     match_continue(1, teacher, student)
#                     elif teacher.focus == student.focus2 and len(student.focus2_t) == 1:
#                         # print("In Focus 2 Loop 2")
#                         if teacher.name != student.focus2_obj[0].name:
#                             # print("In name comparison Focus 2 Loop 2")
#                             # # turns student's focus1 t dictionary in a list, index = lists first obj
#                             # s_teacher_list = list(student.focus1_t)
#                             # index = s_teacher_list[0]
#                             # print(index)
#                             if student.focus2_obj[0].focus == teacher.focus:
#                                 # print("In focus = teacher focus, Focus 1 Loop 2")
#                                 s_teacher_list = list(student.focus2_t)
#                                 name_teacher = s_teacher_list[0]
#                                 if student.focus2_t[name_teacher] in teacher.hours:
#                                     # print("In any function, Focus 1 Loop 2")
#                                     match_continue(2, teacher, student)
#

def match():
    # combine all focus' into one
    # -----------------------------------------
    s_focus_list = []
    for student in students_list:
        s_focus_list.append(student.focus1)
        s_focus_list.append(student.focus2)
    t_focus_list = []
    for teacher in teachers_list:
        t_focus_list.append(teacher.focus1)
        t_focus_list.append(teacher.focus2)
    # count number of instances for each focus
    # ------------------------------------------
    # create counter objects
    s_counter_focus = Counter(s_focus_list)
    t_counter_focus = Counter(t_focus_list)
    s_focus_mean = {
        "AP": None,
        "CP": None,
        "IR": None,
        "MT": None,
        "TH": None,
    }
    t_focus_mean = {
            "AP": None,
            "CP": None,
            "IR": None,
            "MT": None,
            "TH": None,
    }
    # students organize
    s_focus_mean["AP"] = s_counter_focus["AP"]
    s_focus_mean["CP"] = s_counter_focus["CP"]
    s_focus_mean["IR"] = s_counter_focus["IR"]
    s_focus_mean["MT"] = s_counter_focus["MT"]
    s_focus_mean["TH"] = s_counter_focus["TH"]
    # sorted gets items then key is basically map and lambda does a command, here it grabs the second item
    s_focus_org = sorted(s_focus_mean.items(), key=lambda item: item[1])
    # teachers organize
    t_focus_mean["AP"] = t_counter_focus["AP"]
    t_focus_mean["CP"] = t_counter_focus["CP"]
    t_focus_mean["IR"] = t_counter_focus["IR"]
    t_focus_mean["MT"] = t_counter_focus["MT"]
    t_focus_mean["TH"] = t_counter_focus["TH"]
    t_focus_org = sorted(t_focus_mean.items(), key=lambda item: item[1])
    # divide into days
    # ------------------------------------------
    # 10 days divided by number of students, and round up
    students_per_day = 10 / len(students_list)
    math.ceil(students_per_day)
    students_per_day = int(students_per_day)
    # match students with teachers
    # --------------------------------------------
    # make least common focus' list from teachers
    t_common_focus = list(t_focus_org[4])
    t_avg_focus = list(t_focus_org[3] + t_focus_org[2])
    t_least_focus = list(t_focus_org[1] + t_focus_org[0])
    # make least common focus' list from students
    s_common_focus = list(s_focus_org[4])
    s_avg_focus = list(s_focus_org[3] + s_focus_org[2])
    s_least_focus = list(s_focus_org[1] + s_focus_org[0])
    # Add to Pool with focus label
    # ----------------------------------------------
    s_pool = []
    s_pool1 = []
    s_pool2 = []
    s_pool3 = []
    t_pool = []
    t_pool1 = []
    t_pool2 = []
    t_pool3 = []
    # adding students and teachers to pool
    # student
    for student in students_list:
        if student.focus1 in s_least_focus or student.focus2 in s_least_focus and student.focus1 not in s_common_focus or student.focus2 not in s_common_focus:
            s_pool1.append(student)
            print(student.name)
        elif student.focus1 in s_avg_focus or student.focus2 in s_avg_focus and student.focus1 not in s_common_focus or student.focus2 not in s_common_focus:
            s_pool2.append(student)
            print(student.name)
        elif student.focus1 in s_common_focus or student.focus2 in s_common_focus:
            print(student.name)
            s_pool3.append(student)
    for student in s_pool1:
        s_pool.append(student)
    for student in s_pool2:
        s_pool.append(student)
    for student in s_pool3:
        s_pool.append(student)
    # teacher
    for teacher in teachers_list:
        if teacher.focus1 in t_least_focus or teacher.focus2 in t_least_focus:
            t_pool1.append(teacher)
        elif teacher.focus1 in t_avg_focus or teacher.focus2 in t_avg_focus and teacher.focus1 != t_common_focus or teacher.focus2 != t_common_focus:
            t_pool2.append(teacher)
        elif teacher.focus1 in t_common_focus or teacher.focus2 in t_common_focus:
            t_pool3.append(teacher)
    for teacher in t_pool1:
        t_pool.append(teacher)
    for teacher in t_pool2:
        t_pool.append(teacher)
    for teacher in t_pool3:
        t_pool.append(teacher)

        s_pool_weeks = students_list
        t_pool_weeks = teachers_list
    # Sort by focus and time teacher
    # -----------------------------------------------
    t_l_focus_dic = {
        "AP": [],
        "CP": [],
        "IR": [],
        "MT": [],
        "TH": []
    }
    t_a_focus_dic = {
        "AP": [],
        "CP": [],
        "IR": [],
        "MT": [],
        "TH": []
    }
    t_m_focus_dic = {
        "AP": [],
        "CP": [],
        "IR": [],
        "MT": [],
        "TH": []
    }
    # least focus
    for focus in focus_list:
        for teacher in t_pool1:
            if teacher.focus1 == focus or teacher.focus2 == focus:
                t_l_focus_dic[focus].append(teacher)
                # print(list(x.name for x in t_l_focus_dic[focus]))
    # avg focus
    for focus in focus_list:
        for teacher in t_pool2:
            if teacher.focus1 == focus or teacher.focus2 == focus:
                t_a_focus_dic[focus].append(teacher)
    # most focus
    for focus in focus_list:
        for teacher in t_pool3:
            if teacher.focus1 == focus or teacher.focus2 == focus:
                t_m_focus_dic[focus].append(teacher)
    # # Matching
    # # -----------------------------------------------
    # # for 10 days
    print("Students per day: " + str(students_per_day))
    counter = 0
    focus1_counter = 0
    focus2_counter = 0
    s_pools = [s_pool1, s_pool2, s_pool3]
    day = 1
    for pool in s_pools:
        print("Pool: " + str(pool))
        for student in pool:
            print("Student: " + str(student.name))
            if counter == students_per_day:
                day += 1
                counter = 0
                print("Changing Day To: " + str(day))
            counter += 1
            focus_pool = []
            focus_pool.append(student.focus1)
            focus_pool.append(student.focus2)
            focus1_counter = 0
            focus2_counter = 0
            teachers_used_list = []
            print("counter: " + str(counter))
            for focus in focus_pool:
                print("Focus: " + str(focus))
                for teacher in t_l_focus_dic[focus]:
                    if teacher.hours_days[day]:
                        # print("Teacher hours_days[" + str(day) + "]:" + str(teacher.hours_days[day]))
                        if student.focus1 == teacher.focus1 and focus1_counter < 2 and teacher.hours_days[day]\
                                and teacher.name not in teachers_used_list:
                            if student.test_hour:
                                if student.test_hour_parsed[1] in teacher.hours_days[day]:
                                    pass
                            else:
                                pass
                            teachers_used_list.append(teacher.name)
                            student.focus_t.append(teacher)
                            if student.test_hour is None:
                                random.seed(30)
                                times = random.choice(teacher.hours_days[day])
                                student.test_hour_parsed[0] = day
                                student.test_hour_parsed[1] = times
                            else:
                                times = student.test_hour_parsed[1]
                            student.focus1_t.append(teacher)
                            student.test_hour = "Test Day: " + str(day) + "\nTest Hour: " + str(times)
                            focus1_counter += 1
                            # t_l_focus_dic[focus].remove(teacher)
                            print("Focus1: " + str(focus))
                            print("Teacher name: " + str(teacher.name))
                            print("Student Test Hour and Day: " + str(student.test_hour))
                        if student.focus2 == teacher.focus2 and focus2_counter < 2 and teacher.hours_days[day] \
                                and teacher.name not in teachers_used_list:
                            if student.test_hour:
                                if student.test_hour_parsed[1] in teacher.hours_days[day]:
                                    pass
                            else:
                                pass
                            teachers_used_list.append(teacher.name)
                            student.focus_t.append(teacher)
                            if student.test_hour is None:
                                # random.seed(random.randint(0, 300))
                                times = random.choice(teacher.hours_days[day])
                                student.test_hour_parsed[0] = day
                                student.test_hour_parsed[1] = times
                            else:
                                times = student.test_hour_parsed[1]
                            student.focus2_t.append(teacher)
                            student.test_hour = "Test Day: " + str(day) + "\nTest Hour: " + str(times)
                            focus2_counter += 1
                            # t_l_focus_dic[focus].remove(teacher)
                            print("Focus2: " + str(focus))
                            print("Teacher name: " + str(teacher.name))
                            print("Student Test Hour and Day: " + str(student.test_hour))

                for teacher in t_a_focus_dic[focus]:
                    if teacher.hours_days[day]:
                        # print("Teacher hours_days[" + str(day) + "]:" + str(teacher.hours_days[day]))
                        if student.focus1 == teacher.focus1 and focus1_counter < 2 and teacher.hours_days[day]\
                                and teacher.name not in teachers_used_list:
                            if student.test_hour:
                                if student.test_hour_parsed[1] in teacher.hours_days[day]:
                                    pass
                            else:
                                pass
                            teachers_used_list.append(teacher.name)
                            student.focus_t.append(teacher)
                            if student.test_hour is None:
                                # random.seed(random.randint(0, 300))
                                times = random.choice(teacher.hours_days[day])
                                student.test_hour_parsed[0] = day
                                student.test_hour_parsed[1] = times
                            else:
                                times = student.test_hour_parsed[1]
                            student.focus1_t.append(teacher)
                            student.test_hour = "Test Day: " + str(day) + "\nTest Hour: " + str(times)
                            focus1_counter += 1
                            # t_a_focus_dic[focus].remove(teacher)
                            print("Focus1: " + str(focus))
                            print("Teacher name: " + str(teacher.name))
                            print("Student Test Hour and Day: " + str(student.test_hour))
                        if student.focus2 == teacher.focus2 and focus2_counter < 2 and teacher.hours_days[day] \
                                and teacher.name not in teachers_used_list:
                            if student.test_hour:
                                if student.test_hour_parsed[1] in teacher.hours_days[day]:
                                    pass
                            else:
                                pass
                            teachers_used_list.append(teacher.name)
                            student.focus_t.append(teacher)
                            if student.test_hour is None:
                                # random.seed(random.randint(0, 300))
                                times = random.choice(teacher.hours_days[day])
                                student.test_hour_parsed[0] = day
                                student.test_hour_parsed[1] = times
                            else:
                                times = student.test_hour_parsed[1]
                            student.focus2_t.append(teacher)
                            student.test_hour = "Test Day: " + str(day) + "\nTest Hour: " + str(times)
                            focus2_counter += 1
                            # t_a_focus_dic[focus].remove(teacher)
                            print("Focus2: " + str(focus))
                            print("Teacher name: " + str(teacher.name))
                            print("Student Test Hour and Day: " + str(student.test_hour))


    # done = False
    # counter = 0
    # student_found = None
    # # 10 days repeats
    # for x in range(1, 11):
    #     # keep adding if number of students per day is below set number per week
    #     counter += 1
    #     if counter >= students_per_day:
    #         break
    #     student_found = None
    #     for student in s_pool:
    #         # if student_found:
    #         #     print("test break")
    #         #     break
    #             # move break to teacher for loop so it stops it once the student is all filled up
    #         for teacher in t_pool:
    #             # check if teacher fits conditions
    #             while True:
    #                 # if [x + y for student in s_pool for teacher in t_pool
    #                 #     if ])
    #                 if len(student.focus1_t) == 2 and len(student.focus2_t) == 2:
    #                     break
    #                 if (student.focus1 == teacher.focus1 or student.focus1 == teacher.focus2 or
    #                     student.focus2 == teacher.focus1 or student.focus2 == teacher.focus2):
    #                     if student.test_hour in teacher.days or student.test_hour is None:
    #
    #                     if teacher.focus1 == student.focus1:
    #
    #             break
    #                 # if len(student.focus1_t) < 2:
    #                 #     if student.focus1 == teacher.focus1 or teacher.focus2:
    #                 #
    #                 #     if student.focus1 or student.focus2 == teacher.focus1 or teacher.focus2






# def match():
#     # number of students per day
#     stu_per_day = len(students_list) / 10
#     daily_students = round(stu_per_day, 0)
#     # students per loop
#     loop_student = 0
#     # 10 days loop
#     for loop in range(11):
#         while loop_student < 3:
#         for student in students_list:
#             # teacher loop
#             for teacher in teachers_list:


def create_students():
    print("Creating students...")
    # get data for students
    s_f_name_col = s_sheet.col_values(3)
    s_l_name_col = s_sheet.col_values(2)
    s_focus1_col = s_sheet.col_values(4)
    s_focus2_col = s_sheet.col_values(5)
    s_adviser_col = s_sheet.col_values(6)
    # starts at index 2 to prevent errors from 0 and to not get the header,
    # does not have add at end because it needs to start at 1, and end at 9,
    # one less than the len of the column, gets range of teachers
    for index in range(1, len(s_sheet.col_values(2))):
        s_name = s_f_name_col[index] + " " + s_l_name_col[index]
        # print("Name: " + s_name)
        s_focus1 = s_focus1_col[index]
        # print("Focus 1: " + s_focus1)
        s_focus2 = s_focus2_col[index]
        # print("Focus 2: " + s_focus2)
        s_adviser = s_adviser_col[index]
        # print("Adviser: " + s_adviser)
        students_list.append(classes.Student(s_name, s_focus1, s_focus2, s_adviser))

def create_teachers():
    print("Creating teachers...")
    # get data for teachers
    t_name_col = t_sheet.col_values(2)
    t_focus1_col = t_sheet.col_values(3)
    t_focus2_col = t_sheet.col_values(4)
    t_days_avail_col = t_sheet.col_values(5)
    t_day_1_col = t_sheet.col_values(6)
    t_day_2_col = t_sheet.col_values(7)
    t_day_3_col = t_sheet.col_values(8)
    t_day_4_col = t_sheet.col_values(9)
    t_day_5_col = t_sheet.col_values(10)
    t_day_6_col = t_sheet.col_values(11)
    t_day_7_col = t_sheet.col_values(12)
    t_day_8_col = t_sheet.col_values(13)
    t_day_9_col = t_sheet.col_values(14)
    t_day_10_col = t_sheet.col_values(15)
    t_day_col = {
        1: t_day_1_col,
        2: t_day_2_col,
        3: t_day_3_col,
        4: t_day_4_col,
        5: t_day_5_col,
        6: t_day_6_col,
        7: t_day_7_col,
        8: t_day_8_col,
        9: t_day_9_col,
        10: t_day_10_col,
    }
    # range start 1 to avoid header
    for index in range(1, (len(t_name_col)) - 1):
        name = t_name_col[index]
        focus1 = t_focus1_col[index]
        focus2 = t_focus2_col[index]
    # sort data for days available
        days_avail = t_days_avail_col[index]
        # print(days_avail)
        days = days_avail.split(", ")
        days = list(map(int, days))
    # get hours for days
        hours_days = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
            10: None,
        }
        for x in range(1, 11):
            try:
                hours_hold = t_day_col[x][index]
                hours_parsed = []
                if "9AM-11AM" in hours_hold:
                    hours_parsed.append(1)
                if "11AM-1PM" in hours_hold:
                    hours_parsed.append(2)
                if "1PM-3PM" in hours_hold:
                    hours_parsed.append(3)
                hours_days[x] = hours_parsed
            except:
                print("Error while creating hours, teachers.")
        # print(hours_days)
    # create teacher
        teachers_list.append(classes.Teacher(name, focus1, focus2, days, hours_days))

# def export_to_sheets():
#     print("Creating Sheets...")
#     # init sheet
#     # student sheet
#     # sh1 = gc.create("Students Sorted")
#     try:
#         sh1 = gc.open("Students Sorted")
#     except:
#         sh1 = gc.create("Students Sorted")
#     ws1 = sh1.get_worksheet(0)
#     ws1.update_cell(1, 1, "Name")
#     ws1.update_cell(1, 2, "Adviser")
#     ws1.update_cell(1, 3, "Focus 1 Teachers")
#     ws1.update_cell(1, 5, "Focus 2 Teachers")
#     ws1.update_cell(1, 7, "Focus 1 Hour")
#     ws1.update_cell(1, 8, "Focus 2 Hour")
#     # sh1.share("studentassigner@gmail.com", perm_type="user", role="writer")
#     # teacher sheet
#     try:
#         sh2 = gc.open("Teachers Sorted")
#     except:
#         sh2 = gc.create("Teachers Sorted")
#     ws2 = sh2.get_worksheet(0)
#     ws2.update_cell(1, 1, "Name")
#     ws2.update_cell(1, 2, "Students and Time")
#     ws2.update_cell(1, 5, "Focus")
#     # sh2.share("studentassigner@gmail.com", perm_type="user", role="writer")
#     print("Appending student sheet...")
#     # write to sheets
#     # student
#     for index in range(len(students_list)):
#         cell = index + 2
#         student = students_list[index]
#         # name
#         ws1.update_cell(cell, 1, str(student.name))
#         # adviser
#         ws1.update_cell(cell, 2, str(student.adviser))
#         # prints teachers out, needed for loop so it doesnt give an index error
#         loop = 0
#         for loop2 in student.focus1_t:
#             loop += 1
#             if loop == 1:
#                 # focus 1 teacher 1
#                 print(student.name)
#                 print(student.focus1_t[0].name)
#                 ws1.update_cell(cell, 3, str(student.focus1_t[0].name))
#                 # print("works1")
#             if loop == 2:
#                 try:
#                     # focus 1 teacher 2
#                     ws1.update_cell(cell, 4, str(student.focus1_t[1].name))
#                     # print("works2")
#                 except:
#                     print("Error! Student missing second focus 1 teacher. Student Name: " + student.name)
#         loop = 0
#         for loop2 in student.focus2_t:
#             loop += 1
#             if loop == 1:
#                 # focus 2 teacher 1
#                 ws1.update_cell(cell, 5, str(student.focus2_t[0].name))
#                 # print("works3")
#             if loop == 2:
#                 try:
#                     # focus 2 teacher 2
#                     ws1.update_cell(cell, 6, str(student.focus2_t[1].name))
#                     # print("works4")
#                 except:
#                     print("Error! Student missing second focus 2 teacher. Student Name: " + student.name)
#         # hours
#         # get first teacher's time
#         s_teacher_list = list(student.focus_t)
#         times = student.test_hour_parsed[1]
#         day = student.test_hour_parsed[0]
#         focus1_time = times
#         if focus1_time == 1:
#             focus1_time = "9AM-11AM"
#         elif focus1_time == 2:
#             focus1_time = "11AM-1PM"
#         elif focus1_time == 3:
#             focus1_time = "1PM-3PM"
#         # get first teacher's time
#         # s_teacher_list = list(student.focus2_t)
#         # hold_time = s_teacher_list[0]
#         # focus2_time = student.focus2_t[hold_time]
#         # if focus2_time == 1:
#         #     focus2_time = "9AM-11AM"
#         # elif focus2_time == 2:
#         #     focus2_time = "11AM-1PM"
#         # elif focus2_time == 3:
#         #     focus2_time = "1PM-3PM"
#         ws1.update_cell(cell, 7, str(focus1_time))
#         ws1.update_cell(cell, 8, str(focus1_time))
#     print("Wait 100 seconds so GDrive does not lock out")
#     time.sleep(100)
#     print("Appending teacher sheet...")
#     # teacher
#     # for index in range(len(teachers_list)):
#     #     cell = index + 2
#     #     teacher = teachers_list[index]
#     #     # name
#     #     ws2.update_cell(cell, 1, teacher.name)
#     #     # hours
#     #     hours = []
#     #     hours_pre = teacher.hours_days
#     #     if 1 in hours_pre:
#     #         hours.append("9AM-11AM")
#     #     if 2 in hours_pre:
#     #         hours.append("11AM-1PM")
#     #     if 3 in hours_pre:
#     #         hours.append("1PM-3PM")
#     #     ws2.update_cell(cell, 2, str(hours)[1:-1])
#     #     # focus
#     #     ws2.update_cell(cell, 5, teacher.focus1)

def export_to_sheets():
    print("Creating Sheets...")
    # init sheet
    # student sheet
    # sh1 = gc.create("Students Sorted")
    # try:
    #     sh1 = gc.open("Students Sorted")
    # except:
    #     sh1 = gc.create("Students Sorted")
    # ws1 = sh1.get_worksheet(0)
    sheet1.write(0, 0, "Name")
    sheet1.write(0, 1, "Adviser")
    sheet1.write(0, 2, "Focus 1 Teachers")
    sheet1.write(0, 4, "Focus 2 Teachers")
    sheet1.write(0, 6, "Focus 1 Hour")
    sheet1.write(0, 7, "Focus 2 Hour")
    # sh1.share("studentassigner@gmail.com", perm_type="user", role="writer")
    # teacher sheet
    # try:
    #     sh2 = gc.open("Teachers Sorted")
    # except:
    #     sh2 = gc.create("Teachers Sorted")
    # ws2 = sh2.get_worksheet(0)
    # ws2.update_cell(1, 1, "Name")
    # ws2.update_cell(1, 2, "Students and Time")
    # ws2.update_cell(1, 5, "Focus")
    # sh2.share("studentassigner@gmail.com", perm_type="user", role="writer")
    print("Appending student sheet...")
    # write to sheets
    # student
    for index in range(len(students_list)):
        cell = index + 1
        student = students_list[index]
        # name
        sheet1.write(cell, 0, str(student.name))
        # adviser
        sheet1.write(cell, 1, str(student.adviser))
        # prints teachers out, needed for loop so it doesnt give an index error
        loop = 0
        for loop2 in student.focus1_t:
            loop += 1
            if loop == 1:
                # focus 1 teacher 1
                print(student.name)
                print(student.focus1_t[0].name)
                sheet1.write(cell, 2, str(student.focus1_t[0].name))
                # print("works1")
            if loop == 2:
                try:
                    # focus 1 teacher 2
                    sheet1.write(cell, 3, str(student.focus1_t[1].name))
                    # print("works2")
                except:
                    print("Error! Student missing second focus 1 teacher. Student Name: " + student.name)
        loop = 0
        for loop2 in student.focus2_t:
            loop += 1
            if loop == 1:
                # focus 2 teacher 1
                sheet1.write(cell, 4, str(student.focus2_t[0].name))
                # print("works3")
            if loop == 2:
                try:
                    # focus 2 teacher 2
                    sheet1.write(cell, 5, str(student.focus2_t[1].name))
                    # print("works4")
                except:
                    print("Error! Student missing second focus 2 teacher. Student Name: " + student.name)
        # hours
        # get first teacher's time
        s_teacher_list = list(student.focus_t)
        times = student.test_hour_parsed[1]
        day = student.test_hour_parsed[0]
        focus1_time = times
        if focus1_time == 1:
            focus1_time = "9AM-11AM"
        elif focus1_time == 2:
            focus1_time = "11AM-1PM"
        elif focus1_time == 3:
            focus1_time = "1PM-3PM"
        # get first teacher's time
        # s_teacher_list = list(student.focus2_t)
        # hold_time = s_teacher_list[0]
        # focus2_time = student.focus2_t[hold_time]
        # if focus2_time == 1:
        #     focus2_time = "9AM-11AM"
        # elif focus2_time == 2:
        #     focus2_time = "11AM-1PM"
        # elif focus2_time == 3:
        #     focus2_time = "1PM-3PM"
        sheet1.write(cell, 6, str(focus1_time))
        sheet1.write(cell, 7, str(focus1_time))

    wb.save("StudentAssigner.xls")
    print("Wait 100 seconds so GDrive does not lock out")
    time.sleep(100)
    print("Appending teacher sheet...")
    # teacher
    # for index in range(len(teachers_list)):
    #     cell = index + 2
    #     teacher = teachers_list[index]
    #     # name
    #     ws2.update_cell(cell, 1, teacher.name)
    #     # hours
    #     hours = []
    #     hours_pre = teacher.hours_days
    #     if 1 in hours_pre:
    #         hours.append("9AM-11AM")
    #     if 2 in hours_pre:
    #         hours.append("11AM-1PM")
    #     if 3 in hours_pre:
    #         hours.append("1PM-3PM")
    #     ws2.update_cell(cell, 2, str(hours)[1:-1])
    #     # focus
    #     ws2.update_cell(cell, 5, teacher.focus1)


print("Welcome to Student Assigner!\nTo start, enter \"import data\"")
while True:
    # print("Command: ")
    # user_input = input("").strip().lower()
    # if user_input == "import data":
    create_students()
    create_teachers()
    # user input
    print("\nSort and print to excel sheet?\nY/N")
    user_input = input("").strip().lower()
    if user_input == "y":
        match()
        # verify()
        export_to_sheets()
        sys.exit()
    elif user_input == "verify":
        error_correction()
    else:
        sys.exit()
# else:
#     print("Invalid Command")