import random
class school():
    def __init__(self,schoolName):
        self.schoolName = schoolName

    class student():
        def __init__(self,stu_name,stu_surname,stu_no,stu_class,stu_discipline_score,lesson = {"math":0,"physics":0}):
            self.stu_name = stu_name
            self.stu_surname = stu_surname
            self.stu_no = stu_no
            self.stu_class = stu_class
            self.discipline_score = stu_discipline_score
            self.lesson = lesson

        def discipline_status(self):
            status = input("Has the student been disciplined (Yes or No) ? ")
            if (status == "Yes"):
                self.discipline_score -= 20
                if (self.discipline_score <= 0):
                    print("Student expelled from school !!")
                    self.stu_name = None
                    self.stu_surname = None
                    self.stu_no = None
                    self.stu_class = None
                    self.discipline_score = None
                else :
                    print(f"New disciplined score : {self.discipline_score}")
            else :
                pass
        def getStudentInformations(self):
            print(f"""
            Student name : {self.stu_name}
            Student surname : {self.stu_surname}
            Student no : {self.stu_no}
            Student class : {self.stu_class}
            Student discipline score : {self.discipline_score}
            """)
        def changePoint(self):
            lesson_name = input("Please enter  which lesson  you  want to change  point(math or physics) : ")

            if lesson_name == "math":
                self.lesson["math"] = int(input("Please enter the point : "))
                if  0<= self.lesson["math"] <= 100:
                    print("Your point successfully changed ! Your math point = ",self.lesson["math"])
                else :
                    print("The point is not changed ! ")
                    self.lesson["math"] = 0
            elif lesson_name == "physics":
                self.lesson["physics"] = int(input("Please enter the point : "))
                if 0 <= self.lesson["physics"] <= 100:
                    print("Your point successfully changed ! Your physics point = ", self.lesson["physics"])
                else:
                    print("The point is not changed ! ")
                    self.lesson["physics"] = 0
            else:
                print("Wrong lesson input !")
        def show_lesson_points(self):
            print(f"""
            Math = {self.lesson["math"]}
            Physics = {self.lesson["physics"]}
            """)
        def cheatExam(self):
            number = random.randint(1,2)
            if (number == 1):
                print("Cheat !")
                self.discipline_score -= 2
            else:
                print("Wrong Alert ! ")
    class teacher:
        def __init__(self,name,surname,password):
            self.name = name
            self.surname = surname
            self.password = password
        def info_teacher(self):
            print(f"""
            Teacher name : {self.name}
            Teacher surname : {self.surname}
            """)