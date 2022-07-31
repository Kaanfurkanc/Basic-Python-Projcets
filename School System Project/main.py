import school as sc

student = sc.school.student("Kaan Furkan ","Çakıroğlu",42,"Rayenclaw",32)
teacher = sc.school.teacher("Bahadır","Yıldız",123456)
school = sc.school("Ecole42")

while True :
    print(f"""
    Dear {school.schoolName} , welcome  school system  !
    """)
    process = input("Enter 1 for student system\nEnter 2 for teacher system\nEnter '*' to exit : ")
    if process == '1':
        print("\n\nStudent information system ")
        process2 = input("Enter 1 for get lesson points \nEnter 2 for student informations :  ")
        if process2 == '1':
            if student.discipline_score == None:
                pass
            else:
                student.show_lesson_points()
        elif process2 == '2':
            student.getStudentInformations()
        else:
            print("Wrong input !")
    elif process == '2':
        print("\n\nTeacher information system : ")
        process3 = int(input("""
    Processes you can do : 
    Enter 1 for discipline 
    Enter 2  for lesson point
    Enter 3 for Teacher informations :
        """))
        if process3 == 1:
            password = int(input("Please enter your password !"))
            if password == teacher.password:
                student.discipline_status()
            else:
                print("Wrong Password !")
        elif process3 == 2:
            password = int(input("Please enter yout password !"))

            if password == teacher.password:
                if student.discipline_score == None:
                    pass
                else:
                    student.changePoint()
            else:
                print("Wrong Password !")
        elif process3 == 3:
            teacher.info_teacher()
    elif process == '*':
        break
    else :
        print("Wrong process input !")
        
