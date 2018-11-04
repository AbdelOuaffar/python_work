from datetime import datetime
import sys
import parser

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

        if sys.argv[2] == "DateOfBirth":
            list_birth = list_index(sys.argv[1])
            student_tag = index_line_file(sys.argv[1])
            sort_file_by_field(list_birth, student_tag)
        elif sys.argv[2] == "FirstName":
            print(sort_f_name(sys.argv[1]))

        elif sys.argv[2] == "LastName":
            print(sort_l_name(sys.argv[1]))
        else:
            print("Name error ,name field is case sensitive")

    except NameError:
        print("Incorrect name field,case sensitive")


if  __name__ == "__main__":
    main()



(venv) C:\Users\PC\python_work\November_04>sort_student_file.py student.txt DateOfBirth
['Ibrahim,', 'Arabi,', '8/11/1997']
['zak,', 'Aymen,', '3/09/1999']
['Raj,', 'Gharib,', '12/02/2000']
['Bachir,', 'Omar,', '6/15/2002']
['Rabha,', 'Ismail,', '5/23/2005']

(venv) C:\Users\PC\python_work\November_04>sort_student_file.py student.txt FirstName
['Bachir,', 'Omar,', '6/15/2002']
['Ibrahim,', 'Arabi,', '8/11/1997']
['Rabha,', 'Ismail,', '5/23/2005']
['Raj,', 'Gharib,', '12/02/2000']
['zak,', 'Aymen,', '3/09/1999']
None

(venv) C:\Users\PC\python_work\November_04>sort_student_file.py student.txt LastName
['Ibrahim,', 'Arabi,', '8/11/1997']
['zak,', 'Aymen,', '3/09/1999']
['Raj,', 'Gharib,', '12/02/2000']
['Rabha,', 'Ismail,', '5/23/2005']
['Bachir,', 'Omar,', '6/15/2002']
None

#(venv) C:\Users\PC\python_work\November_04>sort_student_file.py DateOfBirth
#['Ibrahim,', 'Arabi,', '8/11/1997']
#['zak,', 'Aymen,', '3/09/1999']
#['Raj,', 'Gharib,', '12/02/2000']
#['Bachir,', 'Omar,', '6/15/2002']
#['Rabha,', 'Ismail,', '5/23/2005']
#(venv) C:\Users\PC\python_work\November_04>sort_student_file.py LastName
#['Ibrahim,', 'Arabi,', '8/11/1997']
#['zak,', 'Aymen,', '3/09/1999']
#['Raj,', 'Gharib,', '12/02/2000']
#['Rabha,', 'Ismail,', '5/23/2005']
#['Bachir,', 'Omar,', '6/15/2002']
#None



#(venv) C:\Users\PC\python_work\November_04>sort_student_file.py FirstName
#['Bachir,', 'Omar,', '6/15/2002']
#['Ibrahim,', 'Arabi,', '8/11/1997']
#['Rabha,', 'Ismail,', '5/23/2005']
#['Raj,', 'Gharib,', '12/02/2000']
#['zak,', 'Aymen,', '3/09/1999']




