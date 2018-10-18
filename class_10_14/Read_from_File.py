with open('C:/Users/PC/python_work/employees.txt', 'r') as f:

       headline=f.readline()
       line1=f.readline()
       head=headline.split()
       line=line1.split()
       print(head[0],int(line[0]))
       print("FullName:",line[2]+","+line[1])
       print(head[3],float(line[3]))
       f.close()


