def     Average(w):
    sum = 0
    for i in w:
        sum += i
        Avg = sum/len(w)
    return Avg
list= [1,2,3,4,5,6]
Result= Average(list)
print(Result,"is the average of the numbers in the list ",list)

