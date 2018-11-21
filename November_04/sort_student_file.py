from datetime import datetime
import sys
import parser
import pandas as pd

def index_line_file(file):
    with open(file, 'r') as f:
            header = f.readline()
            student_junior = []

            for line in f:
                student = line.split()
                student.append(datetime.strptime(student[2], '%m/%d/%Y'))
                student_junior += [student]



            f.close()
            return student_junior
def list_index(file):
        with open(file, 'r') as f:
            header = f.readline()

            list_birth = []
            for line in f:
                student = line.split()
                student.append(datetime.strptime(student[2], '%m/%d/%Y'))
                list_birth.append(student[3])
            f.close()
            return list_birth

def sort_file_by_field(list_field,student_junior):
        sorted_list_field = sorted(list_field)
        for birth in sorted_list_field:
            for student in student_junior:
                if birth == student[3]:
                    print(student[0:3])


def index_by_first_name(file):
    with open(file, 'r') as f:
            header = f.readline()

            list_first_names = []
            for line in f:
                student = line.split()
                list_first_names.append(student[0])
            f.close()
            return list_first_names
def index_by_Last_name(file):
    with open(file, 'r') as f:
            header = f.readline()
            list_last_names = []
            for line in f:
                student = line.split()
                list_last_names.append(student[1])
            f.close()
            return list_last_names

def student_list(file):

    with open(file, 'r') as f:
            header = f.readline()

            list_student_list = []
            for line in f:
                student = line.split()
                list_student_list.append(student)
            f.close()
            return list_student_list


def sort_f_name(file):
    list = student_list(file)
    first = sorted(index_by_first_name(file))
    for name in first:
        for student in list:
            if name == student[0]:
                print(student)

def sort_l_name(file):
    list = student_list(file)
    last = sorted(index_by_Last_name(file))
    for name in last:
        for student in list:
            if name == student[1]:
                print(student)


def main():
    try:
        if len(sys.argv) != 3:
            print("need 3 arguments")
            return

        if sys.argv[2] == "DateOfBirth":
            list_birth = list_index(sys.argv[1])
            student_tag = index_line_file(sys.argv[1])
            sort_file_by_field(list_birth, student_tag)
        elif sys.argv[2] == "FirstName":
            print(sort_f_name(sys.argv[1]))

        elif sys.argv[2] == "LastName":
            print(sort_l_name(sys.argv[1]))
        else:
            print("Name error ,name field is case sensitive", file=sys.stderr)

    except NameError:
        print("Incorrect name field,case sensitive")


if __name__ == "__main__":
     main()






