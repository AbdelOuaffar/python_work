def  Vowel_count(Text):
    Vowel_dictionary ={"Vowels": ["A","a","I","i","O","o","U","u","E","e"]}
    cnt = 0
    for vowel in Vowel_dictionary["Vowels"]:

            compter = 0
            for char in text :
                if char == vowel:
                    compter += 1
            cnt += compter
            print (vowel,compter)

    if  cnt % 2 == 0 and cnt != 0:
         print (cnt, "number of vowels in txt is even ")
    elif cnt % 2 != 0:
         print (cnt," the number is odd ")
    elif cnt == 0 :
         print (" No vowels in you text")
text =input("Enter Text  :")
print(text)
Vowel_count(text)