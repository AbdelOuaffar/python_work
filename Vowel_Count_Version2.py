def  Vowel_count(Text):
    Vowel_dictionary ={"Vowels": ["A","a","I","i","O","o","U","u","E","e"]}
    for vowel in Vowel_dictionary["Vowels"]:
            compter = 0
            for char in text :
                if char == vowel:
                    compter += 1
            print (vowel,compter)
text =input( "Enter text:  ")
Vowel_count(text)