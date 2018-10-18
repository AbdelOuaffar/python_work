A=[[[7]]]
Flat =[]
B =[]
for i in A:
    while type(i)== type(A):


        B=i
        A=B
        if type( i[0]) !=type(A):
            Flat.append(i[0])
            break

print(Flat)