def     Aword_count(list):

            i=0
            for word in list:
                if word== S_word:
                    i+= 1
            return i
List_of_words=['jane',"joe","mark","jane"]
S_word= input("enter a word in the list for count:")
Result= Aword_count(List_of_words)
print( Result)
            