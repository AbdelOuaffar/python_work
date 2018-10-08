
def getWords(text):
    words = []
    currentWord = ""
    for char in text:
        if char == " ":
            words.append(currentWord)
            currentWord = ""
        else:
            currentWord += char
    words.append(currentWord)
    return words


def getUinqueWords(sentence):
    uniqueWords = []
    words = getWords(sentence)
    for word in words:
        if word in uniqueWords:
            continue
        uniqueWords.append(word)
    return uniqueWords


testCase1 = "common is a word used to common to word to express similarities"
result = getUinqueWords(testCase1)
print(result)

testCase2 = "word word word word word"
result = getUinqueWords(testCase2)
print(result)

testCase2 = "word                          word"
result = getUinqueWords(testCase2)
print(result)
Print("This is all")

