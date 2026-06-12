class book:
    def __init__(self,title,author,is_borrowed) -> None:
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        if self.is_borrowed==False:
            print(f"The book {self.title} by {self.author} has been borrowed")
            self.is_borrowed=True
        else:
            print("Book has already been borrowed")
    def returnBook(self):
        if self.is_borrowed==True:
            print(f"The book {self.title} by {self.author} has been returned")
            self.is_borrowed=False
        else:
            print("The book has already been returned")
book1=book("Harry Potter","JK Rowling",False)
book2=book("Oxford dictionary","Oxford university",False)
book3=book("Chemistry O level book","Cambridge board",False)

def action():
    print("Please select the next course of action: (1/2)")
    act=input("1. Borrow a book: \n2. Return a book: ")
    if act == "1" or act =="2":
        a=input("Please enter book name:").lower()
        b=input("Please enter book author:").lower()
        if act=="1":
            if (book1.title.lower(), book1.author.lower())==(a,b):
                book1.borrow()
            elif (book2.title.lower(), book2.author.lower())==(a,b):
                book2.borrow()
            elif (book3.title.lower(), book3.author.lower())==(a,b):
                book3.borrow()
            else:
                print("Book does not exist")
        if act=="2":
            if (book1.title.lower(), book1.author.lower())==(a,b):
                book1.returnBook()
            elif (book2.title.lower(), book2.author.lower())==(a,b):
                book2.returnBook()
            elif (book3.title.lower(), book3.author.lower())==(a,b):
                book3.returnBook()
            else:
                print("Book does not exist")
    else:
        print("Invalid action try again")
        action()
while True:
    action()