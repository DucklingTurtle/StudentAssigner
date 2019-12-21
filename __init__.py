print("Importing data...")
import classes, teachers_sheet, students_sheet

# teachers sheet and student sheet
t_sheet = teachers_sheet.sheet
s_sheet = students_sheet.sheet

# init
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
    classes.Student("Osvaldo Last", "AP", "IR", "Adviser 1"),
    classes.Student("Amanda Panda", "CP", "TH", "Adviser 2")
]
teachers_list = [
    classes.Teacher("Test_first1 Test_last2", "CP", [1, 2]),
    classes.Teacher("Panda Amanda", "IR", [1, 3]),
    classes.Teacher("First3 Last3", "AP", [1, 2])
]
advisers = []
print("Welcome to Assigner Program!")
print("V 0.1")

def commands(command):
    if command == "student input":
        global mode
        mode = "student"
    elif command == "teacher input":
        mode = "teacher"
    elif command == "assigner":
        mode = "assigner"

def teacher_assign(block):
    if block == 1:
        # check if teachers have student and if not, add to pool
        teacher_pool = []
        for teacher in range(len(teachers_list)):
            if teachers_list[teacher].student1 == "" and 1 in teachers_list[teacher].hours:
                teacher_pool.append(teachers_list[teacher])
        # check if students have teacher, if not, add to pool
        student_pool = []
        for student in range(len(students_list)):
            if len(students_list[student].focus1_teachers) < 2:
                student_pool.append(students_list[student])
            elif len(students_list[student].focus2_teachers) < 2:
                student_pool.append(students_list[student])
        for student in student_pool:
            print("Student pool: " + student.name)
        # loops through student pool
        if len(student_pool) > 0 and len(teacher_pool) > 0:
            for i in range(2):
                for student in student_pool:
                    for teacher in teacher_pool:
                        if student.focus1 == teacher.focus and teacher.student1 == "":
                            if len(student.focus1_teachers) < 2:
                                student.focus1_teachers.append(teacher.name)
                                teacher.student1 = student.name
                                print(student.name)
                                print(teacher.name)
                                print("Works")
                # for student in student_pool:

                #     # fix by going through first focus, filling them all up, and on the second focus, check if focus 1 is empty or not
                #     elif student.focus2 == teacher.focus and teacher.student1 == "":
                #         if len(student.focus2_teachers) < 2:
                #             student.focus2_teachers.append(teacher.name)
                #             teacher.student1 = student.name
                #             print(student.name)
                #             print(teacher.name)
                #             print("works")
                # for teacher in teacher_pool:
                #     if len(student.focus2_teachers) < 2:
                #         if student.focus2 == teacher.focus and teacher.student1 == "":
                #             student.focus2_teachers.append(teacher.name)
                #             teacher.student1 = student.name
                #             print(student.name)
                #             print(teacher.name)
                #             print("works")
        else:
            print("Error: not enough students/teachers in pool")
    elif block == 2:
        # check if teachers have student and if not, add to pool
        teacher_pool = []
        for teacher in range(len(teachers_list)):
            if teachers_list[teacher].student2 == "" and 2 in teachers_list[teacher].hours:
                teacher_pool.append(teachers_list[teacher])
        # check if students have teacher, if not, add to pool
        student_pool = []
        for student in range(len(students_list)):
            if len(students_list[student].focus1_teachers) < 2:
                student_pool.append(students_list[student])
            elif len(students_list[student].focus2_teachers) < 2:
                student_pool.append(students_list[student])
        for student in student_pool:
            print(student.name)
        # loops through student pool
        if len(student_pool) > 0 and len(teacher_pool) > 0:
            for student in student_pool:
                if len(student.focus1_teachers) < 1:
                    for teacher in teacher_pool:
                        if student.focus1 == teacher.focus and teacher.student1 == "":
                            student.focus1_teachers.append(teacher.name)
                            teacher.student1 = student.name
                            print(student.name)
                            print(teacher.name)
                            print("Works")
                if len(student.focus2_teachers) < 1:
                    for teacher in teacher_pool:
                        if student.focus2 == teacher.focus and teacher.student1 == "":
                            student.focus2_teachers.append(teacher.name)
                            teacher.student1 = student.name
                            print(student.name)
                            print(teacher.name)
                            print("works")
        else:
            print("Error: not enough students/teachers in pool")


# runs all commands
while True:
    if mode == "init":
        while mode == "init":
            print("\nCommands: " + commands_list + "\nEnter Command: ")
            commands(input("").lower().strip())
    elif mode == "student":
        while mode == "student":
            print("\nCommands: " + commands_student + "\nEnter Command: ")
            user_input = input("").lower().strip()
            if user_input == "create students":
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
            elif user_input == "see students":
                print("Students: ")
                for index in range(len(students_list)):
                    print(students_list[index].name)
                # commands under see students
                while True:
                    print("\nCommands: " + commands_student_stats + "\nEnter Command: ")
                    user_input = input("").lower().strip()
                    # student stats command
                    if user_input == "student stats":
                        print("What student?: ")
                        chosen_student = input("").strip()
                        # find how many students and scan through that number
                        for index in range(len(students_list)):
                                # finds out if student is in list and what its index is
                                if chosen_student.lower() == students_list[index].name.lower():
                                    temp_student_object = students_list[index]
                                    print("Name: " + temp_student_object.name + "\nFocus Area 1: " + temp_student_object.focus1
                                          + "\nFocus 1 Teachers: ", end="")
                                    # asterisks may print out list, check into later
                                    print(*temp_student_object.focus1_teachers, sep=", ")
                                    print("Focus Area 2: " + temp_student_object.focus2 + "\nFocus 2 Teachers: ", end="")
                                    print(*temp_student_object.focus2_teachers, sep=", ")
                                    print("Adviser: " + temp_student_object.adviser)
                    elif user_input == "back":
                        break
                    else:
                        print("Invalid Command")
            elif user_input == "back":
                mode = "init"
            else:
                print("Invalid Command")
    elif mode == "teacher":
        while mode == "teacher":
            print("Commands: " + commands_teacher + "\nEnter Command: ")
            user_input = input("").strip().lower()
            if user_input == "create teachers":
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
            elif user_input == "see teachers":
                for teacher in teachers_list:
                    print(teacher.name)
            elif user_input == "back":
                mode = "init"
            else:
                print("Invalid Command")
    elif mode == "assigner":
        while mode == "assigner":
            print("Commands: " + commands_assigner + "\nEnter Command: ")
            user_input = input("").strip().lower()
            if user_input == "sort":
                print("Sort what?: ")
                print("Commands: " + commands_assigner_sort + "\nEnter Command: ")
                user_input = input("").strip().lower()
                if user_input == "teachers":
                    # go through 3 blocks of time
                    teacher_assign(1)
                    # teacher_assign(2)
                    # teacher_assign(3)
                    # # check if teachers have student and if not, add to pool
                    # teacher_pool = []
                    # for teacher in range(len(teachers_list)):
                    #     if teachers_list[teacher].student == "" and 1 in teachers_list[teacher].hours:
                    #         teacher_pool.append(teachers_list[teacher])
                    # # check if students have teacher, if not, add to pool
                    # student_pool = []
                    # for student in range(len(students_list)):
                    #     if len(students_list[student].focus1_teachers) < 2:
                    #         student_pool.append(students_list[student])
                    #     elif len(students_list[student].focus2_teachers) < 2:
                    #         student_pool.append(students_list[student])
                    # for student in student_pool:
                    #     print(student.name)
                    # # loops through student pool
                    # if len(student_pool) > 0 and len(teacher_pool) > 0:
                    #     for student in student_pool:
                    #         if len(student.focus1_teachers) < 1:
                    #             for teacher in teacher_pool:
                    #                 if student.focus1 == teacher.focus:
                    #                     student.focus1_teachers.append(teacher.name)
                    #                     teacher_pool.remove(teacher)
                    #                     print(student.name)
                    #                     print(teacher.name)
                    #                     print("Works")
                    #         if len(student.focus2_teachers) < 1:
                    #             for teacher in teacher_pool:
                    #                 if student.focus2 == teacher.focus:
                    #                     student.focus2_teachers.append(teacher.name)
                    #                     print(student.name)
                    #                     print(teacher.name)
                    #                     print("works")
                    # else:
                    #     print("Error: not enough students/teachers in pool")
            elif user_input == "back":
                mode = "init"
            else:
                print("Invalid Command")
    else:
        print("Invalid Command")

