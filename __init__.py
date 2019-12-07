import classes

commands_list = "Student Input, Teacher Input, "
commands_student = "Create Student, See Students, Remove Student"
commands_student_stats = "See Student Stats, "
commands_teacher = "Create Teacher, See Teachers, Remove Teacher"
mode = "init"
students_list = [
    {"Name": "Test_name", "Student 1": classes.Student("Test_Name", "Test_Focus1", "Test_Focus2")}
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

while True:
    if mode == "init":
        while mode == "init":
            print("\nAvailable Commands: " + commands_list + "\nEnter Command: ")
            commands(input("").lower())
    elif mode == "student":
        while mode == "student":
            print("\nAvailable Commands: " + commands_student + "\nEnter Command: ")
            user_input = input("")
            if user_input == "create student":
                student_name = input("Student's name?: \n")
                student_focus1 = input("Student's first area of focus?: \n")
                student_focus2 = input("Student's second area of focus?: \n")
                students_list.update({"Name": student_name, student_name : classes.Student(student_name, student_focus1, student_focus2)})
            elif user_input == "see students":
                for index in range(len(students_list)):
                    print("Students: ")
                    print(students_list[index]["Name"])
                # see
                print("\nAvailable Commands: " + commands_student_stats + "\nEnter Command: ")
                user_input = input("")
                if user_input == "See Student Stats":
                    print("What student?: ")
                    choosen_student = input("")
                    # for index in students_list:
                        # if choose_student == list(students_list.keys())[index]:
                        #     print("True")


    elif mode == "teacher":
        while mode == "teacher":
            print("Available Commands: " + commands_teacher + "\nEnter Command: ")
            commands(input("").lower())
    else:
        print("Invalid Command")

