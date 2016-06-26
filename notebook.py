#program like notebook
class Student:
    def __init__(self, name, age, grades=[]):
        self.name=name
        self.age=age
        self.grades=grades
        
    def print(self):
        print(self.name + " "+ str(self.age) + " " + str(self.grades))


def load_students(filename):
    studentList=[]
    students_file = open(filename, "r")

    for line in students_file.readlines():
        name, age, grades = line.split(" ", 2)
        age = int(age)
        grades = grades.strip()

        if grades == '[]':
            grades = []
        else:
            grades = grades.split(", ")
            grades[0] = grades[0][1:]
            grades[-1] = grades[-1][:-1]

            for gradeIndex in range(len(grades)):
                grades[gradeIndex] = float(grades[gradeIndex])

        student = Student (name, age, grades)
        studentList.append(student)

    students_file.close()
    return studentList


def getStudentIndex(studentList, name):
    result = -1

    for studentIndex in range(len(studentList)):
        if studentList[studentIndex].name == name:
            result = studentIndex
            break

    if result == -1:
        print("Student not found!")

    return result


def main():
    studentList = load_students("students.txt")

    while True:
        userInput = input("Enter 0 to see the students.\n"
                          "Enter 1 to add a student.\n"
                          "Enter 2 to add a grade.\n"
                          "Enter 3 to see the average grade.\n"
                          "Enter 4 to remove a student.\n"
                          "Enter exit to exit.\n"
                          "Choose command from above: ")

        if userInput == "exit":
            students_file = open("students.txt", "w")

            for student in studentList:
                students_file.write("{} {} {}\n".format(student.name,
                                                        student.age,
                                                        student.grades))
            print("Bye!")
            break

        elif userInput == "0":
            for student in studentList:
                student.print()

        elif userInput == "1":
            valid_format = True
       
            name = input("Enter name for adding: ")
            for i in "0123456789":
                if i in name:
                    print("Invalid name!")
                    valid_format = False

            if valid_format:
                try:
                    age = int(input("Enter age: "))
                except ValueError:
                    print("Incorrect format of age.")
                    print("Please enter a number for age!")
                    valid_format = False

            if valid_format:
                student = Student(name, age)
                studentList.append(student)

        elif userInput == "2":
            try:
                
                name = input("Enter student name: ")
                studentIndex = getStudentIndex(studentList, name)

                if studentIndex != -1:
                    grade = float(input("Enter student grade: "))
                    if(grade >=2 and grade <=6):
                        studentList[studentIndex].grades.append(grade)
                    else:
                        print("Incorrect format of grade\nPlease enter a  correct number between 2 and 6")

            except:
                print("Incorrect format of grade.\nPlease enter a number for a grade!")

        elif userInput == "3":
            name = input("Enter student name: ")
            studentIndex = getStudentIndex(studentList, name)

            if studentIndex != -1:
                student = studentList[studentIndex]
                average = sum(student.grades) / len(student.grades)
                print("The average grade of the choosen student is: {}".format(
                    round(average, 2)))

        elif userInput == "4":
            name = input("Enter the student's name: ")
            studentIndex = getStudentIndex(studentList, name)

            if studentIndex != -1:
                studentList.pop(studentIndex)
        else:
            print("This command doesn't exist in the program.\r\nPlease enter a correct command!")

        print('-----------')


if __name__ == '__main__':
    main()
