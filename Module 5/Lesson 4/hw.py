class reverse:
    def __init__(self,s) -> None:
        self.s=s
    def reverse(self):
        rev_s=""
        for i in range(len(self.s),0,-1):
           rev_s+=self.s[i-1]
        return rev_s

while True:
    s=input("Enter the string:")
    rev=reverse(s)
    print(rev.reverse())
            

