# Contruct a Person class with private data name ,age
# => Create 3 instances of a person class(Dynamic values read from user at runtime in main)
# => Find out averages of three ages
# => Find out youngest,eldest among them
# => Print the person objects with properties


class Person:

    def __init__(self, Pname, Page):
        self.name = Pname
        self.age = Page

    def printdetails(self):
        print(f"The age of {self.name} is {self.age}")

    def average(self):
         self.tot = harry.age+sunny.age+mohit.age 
         self.avg = (self.tot/3)
         print(f'The average age of three of them are : {self.avg}')

    def greatest(self):
        if harry.age>sunny.age and harry.age>mohit.age:
            if sunny.age>mohit.age:
             print(f'Harry is Eldest and Mohit is youngest')
            else:
             print(f'Harry is Eldest and Sunny is youngest')    

        elif harry.age>sunny.age and mohit.age>harry.age:
            print(f'Mohit is Eldest and sunny is youngest')
  

        elif sunny.age>harry.age and sunny.age>mohit.age:
            if harry.age>mohit.age:
                print(f'Sunny is Eldest and Mohit is Youngest')
            else:
                print(f'Sunny is Eldest and Harry is Youngest')


        elif sunny.age>harry.age and mohit.age>sunny.age:
            print(f'Mohit is Eldest and Harry is Youngest')
        



per = Person("Pname",22)
harry = Person("Harry", 25)
sunny = Person("Sunny", 35)
mohit = Person("Mohit", 45)


print(harry.name)
print(mohit.age)
harry.printdetails()
sunny.printdetails()
mohit.printdetails()
per.average()
per.greatest()





  