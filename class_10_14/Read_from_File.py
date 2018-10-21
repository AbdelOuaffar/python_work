try:
    with open('C:/Users/PC/python_work/Employees.txt', 'r+') as f:



       headline=f.readline()

       line1=f.readline()

       head=headline.split()
       line=line1.split()
       print(head[0],int(line[0]))
       print( f" FullName: {line[2] }{line[1]}" )
       print( head[3], float(line[3]))
       f.write('\n3                  Mohamad            Ajam              120 000.0 ')
       f=open('C:/Users/PC/python_work/Employees.txt', 'r+')
       print(f.read())
       f=open('C:/Users/PC/python_work/Employees.txt', 'r+')
       lines=f.readlines()
       print(lines[1],lines[3])

       print("f encoding:",f.encoding)
       f.close()

except IOError :
       print("an error Occured")

finally:

   print("exit")






