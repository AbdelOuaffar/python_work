def fragment_text(text):
    listOfWords =[]
    collectorOfChar = ""
    for char in text :
          if char != " ":
            collectorOfChar += char
          else :
           listOfWords.append(collectorOfChar)
           collectorOfChar= ""
    return listOfWords

def eliminateSpace(text):

    result1=[]
    for index in range(0,len(result)):
        if result[index]!= "":
            result1.append(result[index])
    return result1
def UniqueWords( nonSpaceSentence):
    finalsentencelist = []
    for index in range(0,len(nonSpaceSentence)) :
        if  nonSpaceSentence[index] not in finalsentencelist:
            finalsentencelist.append(nonSpaceSentence[index])

    return finalsentencelist
def writeSentence ( sentence):
    script=""
    for element in sentence :
        script += element + " "

    return script

text = " you are the one   the      34444 one    one    you  "

result = fragment_text(text)
nonSpaceSentence = eliminateSpace(result)
finalresult = UniqueWords(nonSpaceSentence)
print(result)
print(nonSpaceSentence)
print(finalresult)
writeCorrectSentence = writeSentence(finalresult)
print(writeCorrectSentence)






