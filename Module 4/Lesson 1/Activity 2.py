def match_words(words):
    c=0
    list1=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            c+=1
            list1.append(word)
    print("List of characters with same first and last letters",list1)
    return c

count=match_words(["abc","wow","xyz","madam","python"])
print(count)
