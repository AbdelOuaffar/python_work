from operator import attrgetter
import sys
from datetime import date

class Student:
    def __init__(self, firstname, lastname,dob):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = self.__parse_date__(dob)

    def print(self):
        print(f"{self.firstname} {self.lastname} {self.birthdate}")

    def __parse_date__(self, dob):
        tokens = dob.split("-")
        return date(int(tokens[0]), int(tokens[1]), int(tokens[2]))


def read_students_file(filename):
    file = open(filename, "r")
    file.readline()  # skipping the first line by reading it
    students = []

    for line in file:  # iterate over all the line
        student = create_student_from_line(line)
        students.append(student)  # now we have all items in the file in a list_of_words
    file.close()
    return students

def create_student_from_line(line):
    tokens = line.split(",")
    student = Student(tokens[0], tokens[1], tokens[2])
    return student

def sorting_by_key(Name, final):
    final.sort(key=it(Name))  # print the whole list of dic(of students) sorted by the key gaven
    return final
def search(students, search):
        group = []
        for student in students:
            if search in student.lastname:
                group.append(student.lastname)
            if search in student.firstname:
                group.append(student.firstname)
        return group
def main():
    try:

        file_name = 'student_data.txt'
        sorting_key = input('enter birthdate or lastname or firstname :')
        students = read_students_file(file_name)
        students.sort(key=attrgetter(sorting_key))
        for student in students:
            student.print()
        name_char = input("enter your search: ")
        while name_char != "q":
            group_result = search(students, name_char)
            print(group_result)
            name_char = input('enter your  search ( q to quit):')
        return
    except KeyError:
        print(f"{sorting_key} is not a valid Entry the key has to be written in one of those ways(FirstName,LastName or DateOfBirth)", file=sys.stderr)
        return
    except FileNotFoundError:
        print(f"{file_name} doesn't exist please try a different file", file=sys.stderr)
        return

if __name__ == '__main__':
    main()
#enter your search: >? a
#['Juha', 'Kirra', 'Magas', 'Nira', 'Lima', 'Saleh', 'Saleh', 'Manal']
#enter your  search ( q to quit):>? m
#['Lima']
#enter your  search ( q to quit):>? ma
#['Lima']
#enter your  search ( q to quit):>? l
#['Saleh', 'Ali', 'Saleh', 'Manal']
#enter your  search ( q to quit):>? ale
#['Saleh', 'Saleh']
#enter your  search ( q to quit):>? q

