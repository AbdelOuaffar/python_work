def VowelsCount(text):

        vowel = ["a" , "e", "o", "i","u"]
        for i in range (0 , len(vowel)) :
            VowelCount = 0

            for char in text:
                 if char == vowel[i] :
                     VowelCount += 1
            print(vowel[i], VowelCount)

text = "a chain is only as strong as its weakest link" # when using an input text code give a syntax error
Reveal = VowelsCount(text)
print (Reveal)
