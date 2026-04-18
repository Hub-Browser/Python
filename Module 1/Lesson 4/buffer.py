sum=0
for i in range(1,8):
    sav=int(input("Day",i,":"))
    sum+=sav
avg=sum/7
print("Total is:",sum)
print("Average is",avg)
note_200=sum//200
note_100=sum%200//100
note_50=sum%200%100//50
note_10=sum%200%100%50//10
print("No of note 200:",note_200)
print("No of note 100:",note_100)
print("No of note 50:",note_50)
print("No of note 10:",note_10)