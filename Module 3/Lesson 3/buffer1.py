word=input("Enter the word:").lower()
vow="aeiou"
for i in word:
    if i in vow:
        print("First vowel is found")
        break
    else:
        print("There is no vowel")