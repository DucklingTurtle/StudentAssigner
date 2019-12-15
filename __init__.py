import classes

commands_list = "Student Input, Teacher Input, Assigner"
commands_student = "Create Student, See Students, Remove Student"
commands_student_stats = "Student Stats, Back"
commands_teacher = "Create Teacher, See Teachers, Remove Teacher"
commands_assigner = "Sort"
commands_assigner_sort = "Sort Time"
mode = "init"
students_list = [
    classes.Student("Test_first Test_last", "Test Focus 1", "Test Focus 2"),
    classes.Student("Amanda Panda", "Sound Engineering", "Programming")
]
teachers_list = [
    classes.Teacher("Test_first1 Test_last2", "Test Focus 1", 650, 1230),
    classes.Teacher("Panda Amanda", "Test Focus 2", 830, 1430)
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
            if user_input == "create student":
                student_name = input("Student's name?: \n")
                student_focus1 = input("Student's first area of focus?: \n")
                student_focus2 = input("Student's second area of focus?: \n")
                students_list.update({"Name": student_name, student_name : classes.Student(student_name, student_focus1, student_focus2)})
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
                                    print(*temp_student_object.focus1_teachers, sep=", ")
                                    print("Focus Area 2: " + temp_student_object.focus2 + "\nFocus 2 Teachers: ", end="")
                                    print(*temp_student_object.focus2_teachers, sep=", ")
                                    print("Adviser: " + temp_student_object.adviser)
                    elif user_input == "back":
                        break
                    else:
                        print("Invalid Command")
            elif user_input == "back":
                break
            else:
                print("Invalid Command")
    elif mode == "teacher":
        while mode == "teacher":
            print("Commands: " + commands_teacher + "\nEnter Command: ")
            user_input = input("").strip().lower()
            # if user_input == ""
    elif mode == "assigner":
        while mode == "assigner":
            print("Commands: " + commands_assigner + "\nEnter Command: ")
            user_input = input("").strip().lower()
            if user_input == "sort":
                print("Sort what?: ")
                print("Commands: " + commands_assigner_sort + "\nEnter Command: ")
                user_input = input("").strip().lower()
                # sorts time by chunks
                if user_input == "sort time":
                    for index in range(len(teachers_list)):
                        teacher = teachers_list[index]
                        if teacher.start_time <= 900 and teacher.end_time >= 1100:
                            teacher.time_range.append(1)
                            print("Time range add 1")
                        if teacher.start_time <= 1100 and teacher.end_time >= 1300:
                            teacher.time_range.append(2)
                            print("Time range add 2")
                        if teacher.start_time <= 1300 and teacher.end_time >= 1500:
                            teacher.time_range.append(3)
                            print("Time range add 3")
                if user_input == ""


    else:
        print("Invalid Command")

