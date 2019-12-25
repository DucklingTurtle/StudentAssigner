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


def sort():
    # inefficient, scans through students and compares them all to every teacher, even if they can't match, optimize later
    # for loop goes through students and then teachers
    for t_index, teacher in enumerate(teachers_list):
        for s_index, student in enumerate(students_list):
            # teacher checks
            if teacher.student1 == "":
                # checks if focus matches for either group
                if teacher.focus == student.focus1 or teacher.focus == student.focus2:
                    # checks if teacher focus will go in focus 1, 2, or None
                    if teacher.focus == student.focus1:
                        # focus 1, if nothing in teacher list for students
                        if len(student.focus1_teachers) <= 0:
                            # teacher changes
                            # add student obj reference to teacher
                            teacher.student1_obj = student
                            # add student hours to teacher
                            s_name = student.name
                            # first available teacher hour, teacher is master
                            t_hours = teacher.hours[0]
                            if t_hours == 1:
                                t_hours = "9AM-11AM"
                            elif t_hours == 2:
                                t_hours = "11AM-1PM"
                            elif t_hours == 3:
                                t_hours = "1PM-3PM"
                            teacher.student1 = s_name + str(t_hours)
                            # student changes
                            # add teacher obj reference to student focus1 teachers list
                            student.focus1_teachers.append(teacher)
                            # add hours to student
                            student.focus1_hour = teacher.hours[0]
                            print("New teacher added")
                            print("Student name: " + student.name)
                            print("Teacher name: " + teacher.name)
                        else:
                            # otherwise, if first teacher in students list = teachers focus 1 and less than 2 items in list
                            if student.focus1_teachers[0].focus == teacher.focus and len(student.focus1_teachers) <= 1:
                                # if any of the hours for new teacher in first teacher
                                if any(teacher.hours) == student.focus1_teachers[0].hours[0]:
                                    # teacher changes
                                    # add student obj reference
                                    teacher.student1_obj = student
                                    # add student hours to teacher
                                    s_name = student.name
                                    t_hours = student.focus1_teachers[0]
                                    if t_hours == 1:
                                        t_hours = "9AM-11AM"
                                    elif t_hours == 2:
                                        t_hours = "11AM-1PM"
                                    elif t_hours == 3:
                                        t_hours = "1PM-3PM"
                                    teacher.student1 = s_name + str(t_hours)
                                    # student changes
                                    # add teacher obj reference to student
                                    student.focus1_teachers.append(teacher)
                                    # add hours to student
                                    if student.focus1_hour == teacher.hours[0]:
                                        print("Works adding teacher to master")
                                    else:
                                        print("Error adding teacher to focus 1")
                                    time_slot = student.focus1_teachers[0].hours[0]
                                    print("Teacher: " + teacher.name)
                                    print("Student: " + student.name)
                                    print("Time slot: " + str(time_slot))
                                    print(student.focus1_hour)
                                    print("teacher hours: " + str(teacher.hours[0]))
                                    print("master teacher hours" + str(student.focus1_teachers[0].hours[0]))

#  test to see if first creation block works, then finish the second one, make sure master teacher is the one dictating the hours

# def sort():
#     num_list = [1, 2, 3]
#     random.shuffle(num_list)
#     # does not work because teachers are being rewritten, remove teachers once used from pool
#     for loop in num_list:
#         # block 1
#         if loop == 1:
#             print("works")
#             # check if teachers have student and if not, add to pool
#             teacher_pool = []
#             for teacher in range(len(teachers_list)):
#                 if teachers_list[teacher].student1 == "" and 1 in teachers_list[teacher].hours:
#                     teacher_pool.append(teachers_list[teacher])
#             for teacher in teacher_pool:
#                 print("Teacher pool: " + teacher.name)
#             # check if students have teacher, if not, add to pool
#             student_pool = []
#             for student in range(len(students_list)):
#                 if len(students_list[student].focus1_teachers) < 2 or len(students_list[student].focus2_teachers) < 2:
#                     student_pool.append(students_list[student])
#                 # elif len(students_list[student].focus2_teachers) < 2:
#                 #     student_pool.append(students_list[student])
#             for student in student_pool:
#                 print("Student pool: " + student.name)
#             # loops through student pool
#             if len(student_pool) > 0 and len(teacher_pool) > 0:
#                 # runs twice because it needs to do both focus'
#                 # for student in student_pool:
#                 #     for teacher in teacher_pool:
#                 for teacher in teacher_pool:
#                     for student in student_pool:
#                         if student.focus1 == teacher.focus and teacher.student1 == "" and student.hours_cant.count(1) < 2:
#                             # for index in range(len(student.focus2_objects)):
#                             if 1 in student.focus1_objects and 2 not in student.focus1_objects and 3 not in student.focus1_objects or len(student.focus1_objects) == 0:
#                                 if len(student.focus1_teachers) < 2:
#                                     if student.hours_cant.count(1) < 2:
#                                         student.hours_cant.append(1)
#                                         student.focus1_teachers.append(teacher.name)
#                                         teacher.student1 = student.name
#                                         # teacher_pool.remove(teacher)
#                                         student.focus1_objects.append(1)
#                                         if str(student.hours.get(1)) == "None":
#                                             student.hours[1] = str(teacher.name + " 9AM-11AM, ")
#                                         else:
#                                             student.hours[1] = str(student.hours.get(1)) + str(teacher.name + " 9AM-11AM, ")
#                                         print(student.name)
#                                         print(teacher.name)
#                                         print("-Works-")
#                         if student.focus2 == teacher.focus and teacher.student1 == "" and student.hours_cant.count(1) < 2:
#                             # for index in range(len(student.focus2_objects)):
#                             if 1 in student.focus2_objects and not 2 in student.focus2_objects and not 3 in student.focus2_objects or len(student.focus1_objects) == 0:
#                                 if len(student.focus2_teachers) < 2:
#                                     if student.hours_cant.count(1) < 2:
#                                         student.hours_cant.append(1)
#                                         student.focus2_teachers.append(teacher.name)
#                                         teacher.student1 = student.name
#                                         # remove from teacher pool
#                                         # teacher_pool.remove(teacher)
#                                         student.focus2_objects.append(1)
#                                         if str(student.hours.get(1)) == "None":
#                                             student.hours[1] = str(teacher.name + " 9AM-11AM, ")
#                                         else:
#                                             student.hours[1] = str(student.hours.get(1)) + str(teacher.name + " 9AM-11AM, ")
#                                         print(student.name)
#                                         print(teacher.name)
#                                         print("-works-")
#                     if len(student.focus1_teachers) >= 2 and len(student.focus2_teachers) >= 2:
#                         student_pool.remove(student)
#                     teacher_pool.remove(teacher)
#             else:
#                 print("Error: not enough students/teachers in pool")
#         # block 2
#         elif loop == 2:
#             # check if teachers have student and if not, add to pool
#             teacher_pool = []
#             for teacher in range(len(teachers_list)):
#                 if teachers_list[teacher].student2 == "" and 2 in teachers_list[teacher].hours:
#                     teacher_pool.append(teachers_list[teacher])
#             for teacher in teacher_pool:
#                 print("Teacher pool: " + teacher.name)
#             # check if students have teacher, if not, add to pool
#             student_pool = []
#             for student in range(len(students_list)):
#                 if len(students_list[student].focus1_teachers) < 2 or len(students_list[student].focus2_teachers) < 2:
#                     student_pool.append(students_list[student])
#                 # elif len(students_list[student].focus2_teachers) < 2:
#                 #     student_pool.append(students_list[student])
#             for student in student_pool:
#                 print("Student pool: " + student.name)
#             # loops through student pool
#             if len(student_pool) > 0 and len(teacher_pool) > 0:
#                 for student in student_pool:
#                     for teacher in teacher_pool:
#                 # for teacher in teacher_pool:
#                 #     for student in student_pool:
#                         if student.focus1 == teacher.focus and teacher.student2 == "" and student.hours_cant.count(2) < 2:
#                             # for index in range(len(student.focus1_objects)):
#                                 # checks if there is teachers with the same hours in focus1, if so, add more
#                             if 2 in student.focus1_objects and not 1 in student.focus1_objects and not 3 in student.focus1_objects or len(student.focus1_objects) == 0:
#                                 if len(student.focus1_teachers) < 2:
#                                     if student.hours_cant.count(2) < 2:
#                                         student.hours_cant.append(2)
#                                         student.focus1_teachers.append(teacher.name)
#                                         teacher.student2 = student.name
#                                         teacher_pool.remove(teacher)
#                                         student.focus1_objects.append(2)
#                                         print("teacher name: " + teacher.name)
#                                         print(teacher_pool)
#                                         if str(student.hours.get(2)) == "None":
#                                             student.hours[2] = str(teacher.name + " 11AM-1PM, ")
#                                         else:
#                                             student.hours[2] = str(student.hours.get(2)) + str(teacher.name + " 11AM-1PM, ")
#                                         print(student.name)
#                                         print(teacher.name)
#                                         print("-Works- Block 2")
#                         if student.focus2 == teacher.focus and teacher.student2 == "" and student.hours_cant.count(2) < 2:
#                             # for index in range(len(student.focus2_objects)):
#                             if 2 in student.focus2_objects and not 1 in student.focus2_objects and not 3 in student.focus2_objects or len(student.focus1_objects) == 0:
#                                 if len(student.focus2_teachers) < 2:
#                                     if student.hours_cant.count(2) < 2:
#                                         student.hours_cant.append(2)
#                                         student.focus2_teachers.append(teacher.name)
#                                         teacher.student2 = student.name
#                                         teacher_pool.remove(teacher)
#                                         student.focus2_objects.append(2)
#                                         if str(student.hours.get(2)) == "None":
#                                             student.hours[2] = str(teacher.name + " 11AM-1PM, ")
#                                         else:
#                                             student.hours[2] = str(student.hours.get(2)) + str(teacher.name + " 11AM-1PM, ")
#
#                                         print(student.name)
#                                         print(teacher.name)
#                                         print("-works- Block 2")
#                     if len(student.focus1_teachers) >= 2 and len(student.focus2_teachers) >= 2:
#                         student_pool.remove(student)
#             else:
#                 print("Error: not enough students/teachers in pool")
#         elif loop == 3:
#             print("works")
#             # check if teachers have student and if not, add to pool
#             teacher_pool = []
#             for teacher in range(len(teachers_list)):
#                 if teachers_list[teacher].student3 == "" and 3 in teachers_list[teacher].hours:
#                     teacher_pool.append(teachers_list[teacher])
#             for teacher in teacher_pool:
#                 print("Teacher pool: " + teacher.name)
#             # check if students have teacher, if not, add to pool
#             student_pool = []
#             for student in range(len(students_list)):
#                 if len(students_list[student].focus1_teachers) < 2 or len(students_list[student].focus2_teachers) < 2:
#                     student_pool.append(students_list[student])
#                 # elif len(students_list[student].focus2_teachers) < 2:
#                 #     student_pool.append(students_list[student])
#             for student in student_pool:
#                 print("Student pool: " + student.name)
#             # loops through student pool
#             if len(student_pool) > 0 and len(teacher_pool) > 0:
#                 # runs twice because it needs to do both focus'
#                 # for i in range(2):
#                 for student in student_pool:
#                     for teacher in teacher_pool:
#                 # for teacher in teacher_pool:
#                 #     for student in student_pool:
#                         if student.focus1 == teacher.focus and teacher.student3 == "" and student.hours_cant.count(3) < 2:
#                             # for index in range(len(student.focus1_objects)):
#                             if 3 in student.focus1_objects and not 1 in student.focus1_objects and not 2 in student.focus1_objects or len(student.focus1_objects) == 0:
#                                 if len(student.focus1_teachers) < 2:
#                                     if student.hours_cant.count(3) < 2:
#                                         student.hours_cant.append(3)
#                                         student.focus1_teachers.append(teacher.name)
#                                         teacher.student3 = student.name
#                                         teacher_pool.remove(teacher)
#                                         student.focus1_objects.append(3)
#                                         if str(student.hours.get(3)) == "None":
#                                             student.hours[3] = str(teacher.name + " 1PM-3PM, ")
#                                         else:
#                                             student.hours[3] = str(student.hours.get(3)) + str(teacher.name + " 1PM-3PM, ")
#                                         print(student.name)
#                                         print(teacher.name)
#                                         print("-Works-")
#                         elif student.focus2 == teacher.focus and teacher.student3 == "" and student.hours_cant.count(3) < 2:
#                             # for index in range(len(student.focus2_objects)):
#                             if 3 in student.focus2_objects and not 1 in student.focus2_objects and not 2 in student.focus2_objects or len(student.focus1_objects) == 0:
#                                 if len(student.focus2_teachers) < 2:
#                                     if student.hours_cant.count(3) < 2:
#                                         student.hours_cant.append(3)
#                                         student.focus2_teachers.append(teacher.name)
#                                         teacher.student3 = student.name
#                                         teacher_pool.remove(teacher)
#                                         student.focus2_objects.append(3)
#                                         if str(student.hours.get(3)) == "None":
#                                             student.hours[3] = str(teacher.name + " 1PM-3PM, ")
#                                         else:
#                                             student.hours[3] = str(student.hours.get(3)) + str(teacher.name + " 1PM-3PM, ")
#                                         print(student.name)
#                                         print(teacher.name)
#                                         print("-works-")
#                     if len(student.focus1_teachers) >= 2 and len(student.focus2_teachers) >= 2:
#                         student_pool.remove(student)
#             else:
#                 print("Error: not enough students/teachers in pool")

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
    ws1.update_cell(1, 7, "Testing Hours")
    sh1.share("studentassigner@gmail.com", perm_type="user", role="writer")
    # teacher sheet
    sh2 = gc.create("Teachers Sorted")
    ws2 = sh2.get_worksheet(0)
    ws2.update_cell(1, 1, "Name")
    ws2.update_cell(1, 2, "Hours")
    ws2.update_cell(1, 3, "Focus")
    ws2.update_cell(1, 4, "Students and Time")
    sh2.share("studentassigner@gmail.com", perm_type="user", role="writer")
    # write to sheets
    # student
    for index in range(len(students_list)):
        cell = index + 2
        # name
        ws1.update_cell(cell, 1, str(students_list[index].name))
        # adviser
        ws1.update_cell(cell, 2, str(students_list[index].adviser))
        # prints teachers out, needed for loop so it dosent give an index error
        for loop in range(len(students_list[index].focus1_teachers)):
            if loop == 1:
                # focus 1 teacher 1
                ws1.update_cell(cell, 3, str(students_list[index].focus1_teachers[0]))
            if loop == 2:
                # focus 1 teacher 2
                ws1.update_cell(cell, 4, str(students_list[index].focus1_teachers[1]))
        for loop2 in range(len(students_list[index].focus2_teachers)):
            if loop2 == 1:
                # focus 2 teacher 1
                ws1.update_cell(cell, 5, str(students_list[index].focus2_teachers[0]))
            if loop2 == 2:
                # focus 2 teacher 2
                ws1.update_cell(cell, 6, str(students_list[index].focus2_teachers[1]))
        # hours
        ws1.update_cell(cell, 7, str(students_list[index].hours)[1: -1])
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
            # export_to_sheets()
        else:
            sys.exit()
