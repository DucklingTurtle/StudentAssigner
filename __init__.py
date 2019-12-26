print("Importing packages...")
import classes, teachers_sheet, students_sheet, sys, gspread, random
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
def match_first(focus, teacher, student):
    # t_time = random.choice(teacher.hours)
    t_time = teacher.hours[0]
    teacher.first_pass = True
    # if t_time_orig == 1:
    #     t_time = "9AM-11AM"
    # elif t_time_orig == 2:
    #     t_time = "11AM-1PM"
    # elif t_time_orig == 3:
    #     t_time = "1PM-3PM"
    print("time: " + str(t_time))
    print("Student name: " + student.name)
    print("teacher name: " + teacher.name)
    if focus == 1:
        # add teacher to student's focus1 teachers list, time is key, teacher obj is value
        student.focus1_t[str(teacher.name)] = t_time
        student.focus1_obj.append(teacher)
        # add student to teacher's student list, time is key, student obj is value
        teacher.students[str(student.name)] = t_time
    if focus == 2:
        student.focus2_t[str(teacher.name)] = t_time
        student.focus2_obj.append(teacher)
        teacher.students[str(student.name)] = t_time

def match_continue(focus, teacher, student):
    if focus == 1:
        s_teacher_list = list(student.focus1_t)
        teacher1 = student.focus1_t[s_teacher_list[0]]
        time = s_teacher_list[0]
        s_teacher_list = list(student.focus2_t)
        name_teacher = s_teacher_list[0]
        # student
        student.focus1_obj.append(teacher)
        student.focus1_t[teacher.name] = student.focus2_t[name_teacher]
        print("teacher name: " + teacher.name)
        print("First teacher: " + name_teacher)
        print("student name: " + student.name)
        # teacher
        teacher.students[str(student.name)] = time
    if focus == 2:
        s_teacher_list = list(student.focus2_t)
        teacher1 = student.focus2_t[s_teacher_list[0]]
        time = s_teacher_list[0]
        s_teacher_list = list(student.focus2_t)
        name_teacher = s_teacher_list[0]
        # student
        student.focus2_obj.append(teacher)
        student.focus2_t[teacher.name] = student.focus2_t[name_teacher]
        # teacher
        teacher.students[student.name] = time
        print("teacher name: " + teacher.name)
        print("First teacher: " + name_teacher)
        print("student name: " + student.name)

def sort():
    # run first block, then second
    for loop in range(2):
        for student in students_list:
            for teacher in teachers_list:
                if loop == 0:
                    if teacher.first_pass is not True:
                        if len(student.focus1_obj) <= 0 or len(student.focus2_obj) <= 0:
                            if not teacher.students:
                                if teacher.focus == student.focus1:
                                    print("test")
                                    if len(student.focus1_t) <= 0:
                                        match_first(1, teacher, student)
                                        print("Focus 1")
                                elif teacher.focus == student.focus2:
                                    print("test2")
                                    if len(student.focus2_t) <= 0:
                                        match_first(2, teacher, student)
                                        print("Focus 2")
                elif loop == 1:
                    print("loop2")
                    print(student.name)
                    print(teacher.focus)
                    print(student.focus1)
                    print(student.focus2)
                    print(len(student.focus1_t))
                    print(student.focus1_t)
                    print(len(student.focus2_t))
                    print(student.focus2_t)
                    if teacher.focus == student.focus1 and len(student.focus1_t) <= 1:
                        if teacher.name != student.focus1_obj[0].name:
                            print("loop2")
                            print(loop)
                            # # turns student's focus1 t dictionary in a list, index = lists first obj
                            # s_teacher_list = list(student.focus1_t)
                            # index = s_teacher_list[0]
                            # print(index)
                            if student.focus1_obj[0].focus == teacher.focus:
                                s_teacher_list = list(student.focus1_t)
                                name_teacher = s_teacher_list[0]
                                if any(teacher.hours) == student.focus1_t[name_teacher]:
                                    match_continue(1, teacher, student)
                    elif teacher.focus == student.focus2 and len(student.focus2_t) <= 1:
                        if teacher.name != student.focus2_obj[0].name:
                            # # turns student's focus1 t dictionary in a list, index = lists first obj
                            # s_teacher_list = list(student.focus1_t)
                            # index = s_teacher_list[0]
                            # print(index)
                            if student.focus2_obj[0].focus == teacher.focus:
                                s_teacher_list = list(student.focus2_t)
                                name_teacher = s_teacher_list[0]
                                if any(teacher.hours) == student.focus2_t[name_teacher]:
                                    match_continue(2, teacher, student)
                    else:
                        print("Error: student has more or less than 1 teacher")

def create_students():
    print("Creating students...")
    # get data for students
    s_f_name_col = s_sheet.col_values(3)
    s_l_name_col = s_sheet.col_values(2)
    s_focus1_col = s_sheet.col_values(4)
    s_focus2_col = s_sheet.col_values(5)
    s_adviser_col = s_sheet.col_values(6)
    # starts at index 2 to prevent errors from 0 and to not get the header, gets range of teachers
    # for index in range(2, (len(s_sheet.col_values(2))) + 1):
    for index in range(1, len(s_sheet.col_values(2))):
        s_name = s_f_name_col[index] + " " + s_l_name_col[index]
        print("Name: " + s_name)
        s_focus1 = s_focus1_col[index]
        print("Focus 1: " + s_focus1)
        s_focus2 = s_focus2_col[index]
        print("Focus 2: " + s_focus2)
        s_adviser = s_adviser_col[index]
        print("Adviser: " + s_adviser)
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
        print(t_name)
        print(t_focus)
        print(t_hours)
        teachers_list.append(classes.Teacher(t_name, t_focus, t_hours))

def export_to_sheets():
    # init sheet
    # student sheet
    # sh1 = gc.create("Students Sorted")
    sh1 = gc.open("Students Sorted")
    ws1 = sh1.get_worksheet(0)
    ws1.update_cell(1, 1, "Name")
    ws1.update_cell(1, 2, "Adviser")
    ws1.update_cell(1, 3, "Focus 1 Teachers")
    ws1.update_cell(1, 5, "Focus 2 Teachers")
    ws1.update_cell(1, 7, "Focus 1 Hour")
    ws1.update_cell(1, 8, "Focus 2 Hour")
    sh1.share("studentassigner@gmail.com", perm_type="user", role="writer")
    # teacher sheet
    # sh2 = gc.create("Teachers Sorted")
    # ws2 = sh2.get_worksheet(0)
    # ws2.update_cell(1, 1, "Name")
    # ws2.update_cell(1, 2, "Hours")
    # ws2.update_cell(1, 3, "Focus")
    # ws2.update_cell(1, 4, "Students and Time")
    # sh2.share("studentassigner@gmail.com", perm_type="user", role="writer")
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
            print(loop)
            if loop == 0:
                # focus 1 teacher 1
                ws1.update_cell(cell, 3, str(student.focus1_obj[0].name))
                print("works1")
            if loop == 1:
                # focus 1 teacher 2
                ws1.update_cell(cell, 4, str(student.focus1_obj[1].name))
                print("works2")
        for loop2 in range(2):
            if loop2 == 0:
                # focus 2 teacher 1
                ws1.update_cell(cell, 5, str(student.focus2_obj[0].name))
                print("works3")
            if loop2 == 1:
                # focus 2 teacher 2
                ws1.update_cell(cell, 6, str(student.focus2_obj[1].name))
                print("works4")
        # hours
        s_teacher_list = list(student.focus1_t)
        hold_time = s_teacher_list[0]
        focus1_time = student.focus1_t[hold_time]
        if focus1_time == 1:
            focus1_time = "9AM-11AM"
        elif focus1_time == 2:
            focus1_time = "11AM-1PM"
        elif focus1_time == 3:
            focus1_time = "1PM-3PM"
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
        # ws1.update_cell(cell, 4, str(students_list[index].focus2_teachers)[1:-1])
# def write_to_sheets():
#     global ws1
#     global ws2
#     # student
#     # name
#     for index in range(len( students_list)):
#         cell = index + 2
#         ws1.update_cell(cell, 1, str(students_list[index]))

print("Welcome to teacher/student sorter!\nIf lost, enter \"help\", otherwise, enter \"import data\" to start")
while True:
    print("Command: ")
    user_input = input("").strip().lower()
    if user_input == "help":
        print(help_list)
    elif user_input == "import data":
        # create students
        create_students()
        # create teachers
        create_teachers()
        # user input
        print("Sort and print to excel sheet?\nY/N")
        user_input = input("").strip().lower()
        if user_input == "y":
            # sort
            sort()
            # excel sheet
            export_to_sheets()
        else:
            sys.exit()
