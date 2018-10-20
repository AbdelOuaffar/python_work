def     Racket_one(list):
    W1=[]
    for item  in list:
        if type(item)==type(list):
            W1= Racket_two(item)
        else:
            Final_List.append(item)
    return W1
def     Racket_two(list):
    W2=[]
    for elem in list :
        if type(elem)== type(list):
            W2 = Racket_one(elem)
        else :
            Final_List.append(elem)
    return W2
Final_List =[]
Test_List =[[[23,"USA"]],[[[[[123,"Northern"]]]]],"GRT"]
R_list = Racket_one(Test_List)     #function ( Racket one) recieve the test list,test the element if type is list,after
R_list1 = Racket_two(R_list)       #peeling the first layer of the list element passes it to the second function Racket 2
R_list2 = Racket_one(R_list1)       #to do the same thinng.both functions if they find non list type item they add it to
print(Final_List)
                                   #final list
#out put
#[23, 'USA', 123, 'Northern', 'GRT']




