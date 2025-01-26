students = []
print()
print("======================================")
print("          SCHOOL LOG SYSTEM           ")
print("======================================")

while True:
    print()
    print("------------- MAIN MENU -------------")
    print("1. Log in")
    print("2. Log out")
    print("3. Quit")
    print()

    choice = input("What would you like to do?: ")

    if choice == "1":
        print()
        print("------------- LOGGING IN -------------")
        print()

        while True:
            name = input("Enter your full name [Juan de la Cruz] (PRESS Q TO QUIT): ")
            if name.lower() == "q":
                break
            else:
                print()
                student_id = input("Enter your student ID [24-XXXXX]: 24-")
                            
                if student_id.isdigit() == True and len(student_id) == 5:
                    print()
                    print(f"SUCCESSFULLY LOGGED IN AS {name}")
                    print()
                    students.append(name)
                else:
                    print()
                    print("INVALID STUDENT ID")
                    print()

        print()
        print("------------- LOGGED IN STUDENTS -------------")
        for student in students:
            print(student)

    elif choice == "2":
        print()
        print("------ LOGGING OUT ------")
        print()

        if not students:
            print("No students are currently logged in.")
            continue

        print("List of Logged In Students: ")
        for student in students:
            print(student)
        print()

        while True:
            logout = input("Enter who you want to log out (PRESS Q TO QUIT): ").strip()
            
            if logout.lower() == "q":
                break
            elif logout in students:
                print()
                print(f"{logout} has been successfully logged out.")
                print()
                students.remove(logout)
            else:
                print()
                print("STUDENT NOT FOUND")

        print()    
        print("------------- LOGGED IN STUDENTS -------------")
        if students:
            for student in students:
                print(student)
        else:
            print()
            print("NO STUDENT LOGGED IN")
            break
    
    elif choice == "3":
        print()
        print()    
        print("------------- LOGGED IN STUDENTS -------------")
        if students:
            for student in students:
                print(student)
            print()
            exit()
        else:
            print()
            print("NO STUDENT LOGGED IN")
            print()
            exit()

    else:
        print()
        print("INVALID CHOICE.")