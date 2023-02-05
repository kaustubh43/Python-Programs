class Name:
    def __init__(self,first_name, last_name):
        self.fname = first_name
        self.lname = last_name 
        self.get_name()
    
    def get_name(self):
        print(f"Your name is {self.fname} {self.lname}")

X = Name("Kaustubh", "Ajgaonkar")
