def VowelsCount(text):
    vowel = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    for i in range(0, len(vowel)):
        VowelCount = 0

        for char in text:
            if char == vowel[i]:
                VowelCount += 1
        print(vowel[i], VowelCount)


text = "a chAin Is Only as strong As its wEakest lInk"  # when using an input text code give a syntax error
Reveal = VowelsCount(text)
print (Reveal)