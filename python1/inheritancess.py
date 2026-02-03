# baap ka sab bete ko dena thst set  bhai  
class User :
    
    def __init__(self):
        
       self.name = "mahesh"
    def login(self) :
        print("login")
class Student(User) :
    
    def __init__(self):
        self.roll = 100
        
    def enroll(self) :
        print("enrol intrenship")

s = Student  ()          
                  
s.login()              