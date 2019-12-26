print("Importing packages...")
import classes, teachers_sheet, students_sheet, sys, gspread, random, time
from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials

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
focus_list = [
    "AP", "CP", "IR", "MT", "TH"
]
students_list = [
    # classes.Student("Osvaldo Last", "AP", "IR", "Adviser 1"),
    # classes.Student("Amanda Panda", "CP", "TH", "Adviser 2")
]
teachers_list = [
    classes.Teacher("Test_first1 Test_last2", "CP", [1, 2]),
    classes.Teacher("Panda Amanda", "IR", [1, 3]),
    classes.Teacher("First3 Last3", "AP", [1, 2])
]

def verify():
    for student in students_list:
        # for teacher in teachers_list:
            t_list = list(student.focus1_t)
            t_name = t_list[0]
            t_list2 = list(student.focus2_t)
            t_name2 = t_list2[0]
            t_hold = list(student.focus1_t)
            # check if focus1 matches focus1 list
            if student.focus1 == student.focus1_obj[0].focus:
                pass
            else:
                print("Error: Focus 1 does not match Focus 1 Obj List")
            # check if focus1_obj = focus1_list
            if student.focus1_obj[0].name == t_name:
                pass
            else:
                print("Error: Focus 1 Obj != Focus 1 list")
            # check if focus2 matches focus2 list
            if student.focus2 == student.focus2_obj[0].focus:
                pass
            else:
                print("Error: Focus 2 != Focus 2 List")
            # check if focus2_obj = focus2_list
            if student.focus2_obj[0].name == t_name2:
                pass
            else:
                print("Error: Focus 2 Obj not in Focus 2 List")
            # check if all focus 1 teachers have the same time
            try:
                if student.focus1_t[t_hold[0]] == student.focus1_t[t_hold[1]]:
                    pass
                else:
                    print("Error: Focus 1 teachers not equal")
            except:
                print(student.name + " missing focus 1 second teacher")
                sort_again = True
            # check if all focus 2 teachers have the same time
    try:
        if sort_again is True:
            sort()
            # sort_again = False
            # verify()
            print("sort again")
    except:
        pass


def match_first(focus, teacher, student):
    # print("In match_first")
    t_time = random.choice(teacher.hours)
    while True:
        if focus == 1:
            # print("In focus 1")
            if len(student.focus2_t) >= 1:
                s_teacher_list = list(student.focus2_t)
                name_teacher = s_teacher_list[0]
                if t_time != student.focus2_t[name_teacher]:
                    break
                else:
                    if len(teacher.hours) > 1:
                        t_time = random.choice(teacher.hours)
                    else:
                        return
            else:
                break
        elif focus == 2:
            if len(student.focus1_t) >= 1:
                # print("In focus 2")
                s_teacher_list = list(student.focus1_t)
                name_teacher = s_teacher_list[0]
                if t_time != student.focus1_t[name_teacher]:
                    break
                else:
                    if len(teacher.hours) > 1:
                        t_time = random.choice(teacher.hours)
                    else:
                        return
            else:
                break
        else:
            print("Error: no focus")
            return
    teacher.first_pass = True
    # print("time: " + str(t_time))
    # print("Student name: " + student.name)
    # print("teacher name: " + teacher.name)
    if focus == 1 and t_time not in teacher.hours_taken:
        # add teacher to student's focus1 teachers list, time is key, teacher obj is value
        student.focus1_t[str(teacher.name)] = t_time
        student.focus1_obj.append(teacher)
        # add student to teacher's student list, time is key, student obj is value
        teacher.students[str(student.name)] = t_time
        teacher.hours_taken.append(t_time)
        # print("t_time: " + str(t_time))
    if focus == 2 and t_time not in teacher.hours_taken:
        student.focus2_t[str(teacher.name)] = t_time
        student.focus2_obj.append(teacher)
        teacher.students[str(student.name)] = t_time
        teacher.hours_taken.append(t_time)

def match_continue(focus, teacher, student):
    # print("in match_continute")
    if focus == 1:
        s_teacher_list = list(student.focus1_t)
        time_name = s_teacher_list[0]
        time = student.focus1_t[time_name]
        if time not in teacher.hours_taken:
            s_teacher_list = list(student.focus1_t)
            name_teacher = s_teacher_list[0]
            # student
            student.focus1_obj.append(teacher)
            student.focus1_t[teacher.name] = student.focus1_t[name_teacher]
            # print("teacher name: " + teacher.name)
            # print("First teacher: " + name_teacher)
            # print("student name: " + student.name)
            # teacher
            teacher.students[str(student.name)] = student.focus1_t[name_teacher]
            teacher.hours_taken.append(time)
            # print("hours to append: " + str(student.focus1_t[name_teacher]))
            # print("hours taken: " + str(teacher.hours_taken))
            # print(time)
    if focus == 2:
        s_teacher_list = list(student.focus2_t)
        time_name = s_teacher_list[0]
        time = student.focus2_t[time_name]
        if time not in teacher.hours_taken:
            name_teacher = s_teacher_list[0]
            # student
            student.focus2_obj.append(teacher)
            student.focus2_t[teacher.name] = student.focus2_t[name_teacher]
            # teacher
            teacher.students[student.name] = student.focus2_t[name_teacher]
            teacher.hours_taken.append(time)
            # print("teacher name: " + teacher.name)
            # print("First teacher: " + name_teacher)
            # print("student name: " + student.name)
            # print(teacher.hours_taken)

def sort():
    # run first block, then second
    for loop in range(3):
        for student in students_list:
            for teacher in teachers_list:
                if loop == 0:
                    if teacher.first_pass is not True:
                        if len(student.focus1_obj) <= 0 or len(student.focus2_obj) <= 0:
                            if not teacher.students:
                                if teacher.focus == student.focus1:
                                    # print("test")
                                    if len(student.focus1_t) <= 0:
                                        # print(student.name)
                                        match_first(1, teacher, student)
                                        # print("Focus 1")
                                elif teacher.focus == student.focus2:
                                    # print("test2")
                                    if len(student.focus2_t) <= 0:
                                        # print(student.name)
                                        match_first(2, teacher, student)
                                        # print("Focus 2")
                elif loop == 1 or loop == 2:
                    # print("In Loop 2")
                    # print(loop)
                    # print(student.name)
                    # print(teacher.name)
                    # print(teacher.focus)
                    # print(student.focus1)
                    # print(student.focus2)
                    # print(len(student.focus1_t))
                    # print(student.focus1_t)
                    # print(len(student.focus2_t))
                    # print(student.focus2_t)
                    # print("hours taken: " + str(teacher.hours_taken))
                    # print(teacher.hours)
                    if teacher.focus == student.focus1 and len(student.focus1_t) == 1:
                        # print("In Focus 1 Loop 2")
                        if teacher.name != student.focus1_obj[0].name:
                            # print("In name comparison, Focus 1 Loop 2")
                            # # turns student's focus1 t dictionary in a list, index = lists first obj
                            # s_teacher_list = list(student.focus1_t)
                            # index = s_teacher_list[0]
                            # print(index)
                            if student.focus1_obj[0].focus == teacher.focus:
                                # print("In focus = teacher focus, Focus 1 Loop 2")
                                s_teacher_list = list(student.focus1_t)
                                name_teacher = s_teacher_list[0]
                                if student.focus1_t[name_teacher] in teacher.hours:
                                    # print("In any function, Focus 1 Loop 2")
                                    match_continue(1, teacher, student)
                    elif teacher.focus == student.focus2 and len(student.focus2_t) == 1:
                        # print("In Focus 2 Loop 2")
                        if teacher.name != student.focus2_obj[0].name:
                            # print("In name comparison Focus 2 Loop 2")
                            # # turns student's focus1 t dictionary in a list, index = lists first obj
                            # s_teacher_list = list(student.focus1_t)
                            # index = s_teacher_list[0]
                            # print(index)
                            if student.focus2_obj[0].focus == teacher.focus:
                                # print("In focus = teacher focus, Focus 1 Loop 2")
                                s_teacher_list = list(student.focus2_t)
                                name_teacher = s_teacher_list[0]
                                if student.focus2_t[name_teacher] in teacher.hours:
                                    # print("In any function, Focus 1 Loop 2")
                                    match_continue(2, teacher, student)

def create_students():
    print("Creating students...")
    # get data for students
    s_f_name_col = s_sheet.col_values(3)
    s_l_name_col = s_sheet.col_values(2)
    s_focus1_col = s_sheet.col_values(4)
    s_focus2_col = s_sheet.col_values(5)
    s_adviser_col = s_sheet.col_values(6)
    # starts at index 2 to prevent errors from 0 and to not get the header, gets range of teachers
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
    t_focus_col = t_sheet.col_values(3)
    t_hours_col = t_sheet.col_values(4)
    # starts at index 2 to prevent errors from 0 and to not get the header, gets range of teachers
    for index in range(2, (len(t_sheet.col_values(2))) + 1):
        index2 = index - 1
        t_name = t_name_col[index2]
        t_focus_pre = t_focus_col[index2]
        t_focus = ""
        for focus in focus_list:
            if focus in t_focus_pre:
                t_focus = focus
                break
        t_hours_pre = t_hours_col[index2]
        t_hours_pre = list(t_hours_pre.split(", "))
        t_hours = []
        for scan in t_hours_pre:
            if scan == "9 AM - 11 AM":
                t_hours.append(1)
            if scan == "11 AM - 1 PM":
                t_hours.append(2)
            if scan == "1 PM - 3 PM":
                t_hours.append(3)
        # print(t_name)
        # print(t_focus)
        # print(t_hours)
        teachers_list.append(classes.Teacher(t_name, t_focus, t_hours))

def export_to_sheets():
    print("Creating Sheets...")
    # init sheet
    # student sheet
    # sh1 = gc.create("Students Sorted")
    try:
        sh1 = gc.open("Students Sorted")
    except:
        sh1 = gc.create("Students Sorted")
    ws1 = sh1.get_worksheet(0)
    ws1.update_cell(1, 1, "Name")
    ws1.update_cell(1, 2, "Adviser")
    ws1.update_cell(1, 3, "Focus 1 Teachers")
    ws1.update_cell(1, 5, "Focus 2 Teachers")
    ws1.update_cell(1, 7, "Focus 1 Hour")
    ws1.update_cell(1, 8, "Focus 2 Hour")
    # sh1.share("studentassigner@gmail.com", perm_type="user", role="writer")
    # teacher sheet
    try:
        sh2 = gc.open("Teachers Sorted")
    except:
        sh2 = gc.create("Teachers Sorted")
    ws2 = sh2.get_worksheet(0)
    ws2.update_cell(1, 1, "Name")
    ws2.update_cell(1, 2, "Students and Time")
    ws2.update_cell(1, 5, "Focus")
    # sh2.share("studentassigner@gmail.com", perm_type="user", role="writer")
    print("Appending student sheet...")
    # write to sheets
    # student
    for index in range(len(students_list)):
        cell = index + 2
        student = students_list[index]
        # name
        ws1.update_cell(cell, 1, str(student.name))
        # adviser
        ws1.update_cell(cell, 2, str(student.adviser))
        # prints teachers out, needed for loop so it doesnt give an index error
        for loop in range(2):
            if loop == 0:
                # focus 1 teacher 1
                ws1.update_cell(cell, 3, str(student.focus1_obj[0].name))
                # print("works1")
            if loop == 1:
                try:
                    # focus 1 teacher 2
                    ws1.update_cell(cell, 4, str(student.focus1_obj[1].name))
                    # print("works2")
                except:
                    print("Error! Student missing second focus 1 teacher. Student Name: " + student.name)
        for loop2 in range(2):
            if loop2 == 0:
                # focus 2 teacher 1
                ws1.update_cell(cell, 5, str(student.focus2_obj[0].name))
                # print("works3")
            if loop2 == 1:
                try:
                    # focus 2 teacher 2
                    ws1.update_cell(cell, 6, str(student.focus2_obj[1].name))
                    # print("works4")
                except:
                    print("Error! Student missing second focus 2 teacher. Student Name: " + student.name)
        # hours
        # get first teacher's time
        s_teacher_list = list(student.focus1_t)
        hold_time = s_teacher_list[0]
        focus1_time = student.focus1_t[hold_time]
        if focus1_time == 1:
            focus1_time = "9AM-11AM"
        elif focus1_time == 2:
            focus1_time = "11AM-1PM"
        elif focus1_time == 3:
            focus1_time = "1PM-3PM"
        # get first teacher's time
        s_teacher_list = list(student.focus2_t)
        hold_time = s_teacher_list[0]
        focus2_time = student.focus2_t[hold_time]
        if focus2_time == 1:
            focus2_time = "9AM-11AM"
        elif focus2_time == 2:
            focus2_time = "11AM-1PM"
        elif focus2_time == 3:
            focus2_time = "1PM-3PM"
        ws1.update_cell(cell, 7, str(focus1_time))
        ws1.update_cell(cell, 8, str(focus2_time))
    print("Wait 100 seconds so GDrive does not lock out")
    time.sleep(100)
    print("Appending teacher sheet...")
    # teacher
    for index in range(len(teachers_list)):
        cell = index + 2
        teacher = teachers_list[index]
        # name
        ws2.update_cell(cell, 1, teacher.name)
        # hours
        hours = []
        hours_pre = teacher.hours_taken
        if 1 in hours_pre:
            hours.append("9AM-11AM")
        if 2 in hours_pre:
            hours.append("11AM-1PM")
        if 3 in hours_pre:
            hours.append("1PM-3PM")
        ws2.update_cell(cell, 2, str(hours)[1:-1])
        # focus
        ws2.update_cell(cell, 5, teacher.focus)

print("Welcome to Student Assigner!\nTo start, enter \"import data\"")
while True:
    print("Command: ")
    user_input = input("").strip().lower()
    if user_input == "import data":
        # create students
        create_students()
        # create teachers
        create_teachers()
        # user input
        print("\nSort and print to excel sheet?\nY/N")
        user_input = input("").strip().lower()
        if user_input == "y":
            sort()
            verify()
            export_to_sheets()
        else:
            sys.exit()
    else:
        print("Invalid Command")