List=[2,7,9,1,3]
def  sum_ctnt_even_index(w):
          sum = 0
          i = 0
          while i< len(w) :
               sum += w[i]
               i+= 2
          return   sum
Result = sum_ctnt_even_index(List)
print(Result,"is the sum of every other number of the list",List)












