def     word_count(sentence):
            i= 0
            for letter in sentence:
                if letter ==" ":
                    i+=1
            return
text= input("enter a phrase   :")
Result= word_count(text)
print(Result,"is the number of words in your phrase")
#print(len(text)-Result+1,"count of letters")


