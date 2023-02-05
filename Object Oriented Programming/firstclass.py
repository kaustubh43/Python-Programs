class Name:
   
    def __init__(self,first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.get_name()
    
    def get_name(self):
        '''
        This Function Prints your name
        '''
        print(f"Your name is {self.fname} {self.lname}")

print("Hellooo")
X = Name("Kaustubh", "Ajgaonkar")
