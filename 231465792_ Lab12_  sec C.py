#Question1
class Employee:
    def setbasic(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print()
        print("Name:",self.name,"\nSalary:",self.salary)

class Manager(Employee):
    def __init__(self):
        self._department=""

    def setdepartment(self,department):
        self._department=department

    def display(self):
        super().display()
        print("Department:",self._department)
        


class Executive(Manager):
    def __init__(self):
        self.reward=[]

    def setreward(self,reward):
        self.reward=reward

    def display(self):
        x=1
        super().display()
        print("Rewards:")
        for reward in self.reward:
            print(x,reward)
            x=x+1

def main():
    m1=Manager()
    m1.setbasic("Aneeq",50000)
    m1.setdepartment("CS")
    m1.display()

    e1=Executive()
    e1.setbasic("Hamza",150000)
    e1.setdepartment("CS+")
    e1.setreward(["Honda","Free dinner"])
    e1.display()
main()

#Question2
from abc import ABC, abstractmethod
class Polygon:
    @abstractmethod
    def getnoofsides(self):
        pass
    def getarea(self):
        pass
    
class Triangle(Polygon):
    def setinfo(self,base,height):
        self.base=base
        self.height=height
        
    def getnoofsides(self):
        self.sides=3
        
    def getarea(self):
        self.area=1/2*self.base*self.height

    def display(self):
        print("Shape: Triangle","\n\tSides:",self.sides,"\n\tBase:",self.base,"\n\tHeight:",self.height,"\n\tArea:",self.area)
        
    
class Rectangle(Polygon):
    def setinfo(self,length,width):
        self.length=length
        self.width=width
        
    def getnoofsides(self):
        self.sides=4
        
    def getarea(self):
        self.area=self.length*self.width
        
    def display(self):
        print("Shape: Rectangle","\n\tSides:",self.sides,"\n\tLength:",self.length,"\n\tWidth:",self.width,"\n\tArea:",self.area)
        

class Square(Polygon):
    def setinfo(self,length):
        self.length=length
        
    def getnoofsides(self):
        self.sides=4
        
    def getarea(self):
        self.area=self.length*self.length
        
    def display(self):
        print("Shape: Square","\n\tSides:",self.sides,"\n\tLength:",self.length,"\n\tArea:",self.area)

def main():
    shapes=[]
    no=1
    shape1=Triangle()
    shape1.setinfo(10,5)
    shapes.append(shape1)
    
    shape2=Rectangle()
    shape2.setinfo(7,3)
    shapes.append(shape2)
    
    shape3=Square()
    shape3.setinfo(10)
    shapes.append(shape3)

    

    for shape in shapes:
        shape.getnoofsides()
        shape.getarea()
        print("\n",no,end="-")
        shape.display()
        no=no+1

main()




#Question3
from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def InterestRate(self):
        pass

    def getStatus(self):
        pass

class SBI(Account):
    def setbasic(self, accountTitle, currentBalance):
        self.accountTitle=accountTitle
        self.currentBalance=currentBalance


    def InterestRate(self):
        self.Interest=self.currentBalance*5/100
        self.updatedBalance= self.currentBalance+self.Interest

    def getStatus(self):
        print("\nName:",self.accountTitle,"\nCurrent Balance:",self.currentBalance,"\nInterest:",self.Interest,"\nUpdated Balance:",self.updatedBalance)

class ICICI(Account):
    def setbasic(self, accountTitle, currentBalance):
        self.accountTitle=accountTitle
        self.currentBalance=currentBalance



    def InterestRate(self):
        self.Interest=self.currentBalance*6/100
        self.updatedBalance= self.currentBalance+self.Interest

    def getStatus(self):
        print("\nName:",self.accountTitle,"\nCurrent Balance:",self.currentBalance,"\nInterest:",self.Interest,"\nUpdated Balance:",self.updatedBalance)

class AXIS(Account):
    def setbasic(self, accountTitle, currentBalance):
        self.accountTitle=accountTitle
        self.currentBalance=currentBalance


    def InterestRate(self):
        self.Interest=self.currentBalance*8/100
        self.updatedBalance= self.currentBalance+self.Interest

    def getStatus(self):
        print("\nName:",self.accountTitle,"\nCurrent Balance:",self.currentBalance,"\nInterest:",self.Interest,"\nUpdated Balance:",self.updatedBalance)


def main():
    ac1=SBI()
    ac1.setbasic("Aneeq",50000)
    ac2=ICICI()
    ac2.setbasic("Hamza",25000)
    ac3=AXIS()
    ac3.setbasic("Reham",300000)
    allac=[ac1,ac2,ac3]

    for ac in allac:
        ac.InterestRate()
        ac.getStatus()
        

main()



