sen=input("Enter a sentence: ")
vow=0
con=0
sp=0
vl="aeiouAEIOU"
for i in sen:
    if i==" ":
        sp+=1
    elif i.isalpha():
        if i in vl:
            vow+=1
        else:
            con+=1
print(f"Vowels:{vow}, Consonants:{con}, Spaces:{sp}")
