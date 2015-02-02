#Toby Kerslake
#29-01-2015
#Recors Revision Exercise 2

class StudentRecord:
    def __init__(self):
        self.name = None
        self.markGonzalez = None


def StudentList():
    student_list = []
    for count in range(3):
        student_list.append(StudentRecord())
    for records in student_list:
        records.name = input("Please enter the student's name")
        records.markGonzalez = int(input("Please enter the student's mark"))
    return student_list

def DisplayStudents(student_list):
    for student in student_list:
        print("{0}'s mark is {1}".format(student.name,student.markGonzalez))

#Main Program
student_list = StudentList()
DisplayStudents(student_list)

