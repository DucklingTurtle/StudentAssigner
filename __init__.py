import classes

commands_list = "Student Input, Teacher Input, "
commands_student = "Create Student, See Students, Remove Student"
commands_student_stats = "See Student Stats, Back"
commands_teacher = "Create Teacher, See Teachers, Remove Teacher"
mode = "init"
students_list = [
    {"Name": "Test_name", "Test_name": classes.Student("Test_Name", "Test_Focus1", "Test_Focus2")},
    {"Name": "Test_name2", "Object": classes.Student("Test_Name2", "Test_Focus1", "Test_Focus2")}
]
teachers_list = []
advisers = []
print("Welcome to Assigner Program!")
print("V 0.1")

def commands(command):
    if command == "student input":
        global mode
        mode = "student"
    elif command == "teacher input":
        mode = "teacher"

# runs all commands
while True:
    if mode == "init":
        while mode == "init":
            print("\nAvailable Commands: " + commands_list + "\nEnter Command: ")
            commands(input("").lower())
    elif mode == "student":
        while mode == "student":
            print("\nAvailable Commands: " + commands_student + "\nEnter Command: ")
            user_input = input("").lower()
            if user_input == "create student":
                student_name = input("Student's name?: \n")
                student_focus1 = input("Student's first area of focus?: \n")
                student_focus2 = input("Student's second area of focus?: \n")
                students_list.update({"Name": student_name, student_name : classes.Student(student_name, student_focus1, student_focus2)})
            elif user_input == "see students":
                print("Students: ")
                for index in range(len(students_list)):
                    print(students_list[index]["Name"])
                # commands under see students
                while True:
                    print("\nAvailable Commands: " + commands_student_stats + "\nEnter Command: ")
                    user_input = input("").lower()
                    if user_input == "see student stats":
                        print("What student?: ")
                        choosen_student = input("")
                        for index in range(len(students_list)):
                            if choosen_student == students_list[index][choosen_student]:
                                print("Succesful")
                                print("Name: " + students_list[index][choosen_student].name)
                                      # + "\nFocus Area 1: " + students_list[index][choosen_student].focus1)
                                      # "\nFocus 1 Teacher: " + students_list[index][choosen_student].focus1_teachers +
                                      # "\nFocus Area 2: " + students_list[index][choosen_student].focus2 +
                                      # "\nFocus Area 2 Teacher: " + students_list[index][choosen_student].focus2_teachers +
                                      # "\nAdviser: " + students_list[index][choosen_student].adviser)
                                # print("Focus Area 1: " + students_list[index][choosen_student].focus1)
                    elif user_input == "back":
                        break
                    else:
                        print("Invalid Command")


    elif mode == "teacher":
        while mode == "teacher":
            print("Available Commands: " + commands_teacher + "\nEnter Command: ")
            commands(input("").lower())
    else:
        print("Invalid Command")

