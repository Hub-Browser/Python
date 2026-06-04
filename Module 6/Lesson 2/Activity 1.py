class iostring():
    def __init__(self) -> None:
        self.str1=""
    def get_str(self):
        self.str1=input("Enter the string:")
    def print_str(self):
        print("Result:",self.str1.upper())
ob=iostring()
ob.get_str()
ob.print_str()