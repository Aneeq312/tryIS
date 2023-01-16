#task 1
class car:
    def __init__(self,efficiency,fuel=0):
        self._efficiency=efficiency
        self._fuel=fuel

    def addfuel(self, fuel):
        self._fuel= self._fuel + fuel


    def drive(self, d):
        self._fuel= self._fuel - (d/(self._efficiency))

    def getgaslevel(self):
        return self._fuel

def main():
    carobj= car(100)
    carobj.addfuel(60)
    carobj.drive(200)
    print(carobj.getgaslevel())

main()

#task 2
class employee:
    def __init__(self,em_id,em_name,em_salary):
        self._em_id=em_id
        self._em_name=em_name
        self._em_salary=em_salary
        self.type_emp="Lower grade"

    def displayempinfo(self):
        print (self._em_id, self._em_name, self._em_salary, self.type_emp)
        print()
        
class manager:
    def __init__(self, ma_id,ma_name):
        self._ma_id= ma_id
        self._ma_name= ma_name
        self.type_emp="Higher grade"
    def displaymaninfo(self):
        print (self._ma_id, self._ma_name, self.type_emp)
        print()

def main():
    manlist=[]
    emplist=[]
    for i in range(0,3):
        em_id= input("Enter employee id: ")
        em_name= input("Enter employee name: ")
        em_salary= input("Enter employee salary: ")
        print()
        empobj = employee(em_id, em_name, em_salary)
        emplist.append(empobj)
    for x in range(0,2):
        ma_id= input("Enter manager id: ")
        ma_name= input("Enter manager name: ")
        print()
        manobj = manager(ma_id, ma_name)
        manlist.append(manobj)

    for q in emplist:
        q.displayempinfo()

    for r in manlist:
        r.displaymaninfo()

main()

#task 4
class Actor:
    def __init__(self,movlist):
        self._actorname= ""
        self._DoB= ""
        self._g= ""
        self._movlist=movlist

    def setname(self, actorname):
        self._actorname= actorname
    def setdob(self, DoB):
        self._DoB=DoB
    def setgender(self, g):
        self._g= g

    
    def getname(self):
        return self._actorname
    def getdob(self):
        return self._DoB
    def getgender(self):
        return self._g

    def displayactor(self):
        print(self._actorname,self._DoB,self._g,self._movlist)

    def addmovie(self,movlist,movie):
        self._movlist.append(movie)


def compareActor(actor1list,actor2list):
        if actor1list in actor2list:
            print("They both were casted in",actor1list)

def main():
    actor1list=[]
    actor1=Actor(actor1list)
    
    actor1.setname("Aneeq")
    actor1.setdob("3rd Dec")
    actor1.setgender("m")
    actor1.displayactor()
    x = input("Do you want to add more movies to this actors list? y for yes n for no: ")
    while x!="n":
        movie=input("Enter a movie: ")
        actor1.addmovie(actor1list,movie)
        x = input("Do you want to add more movies to this actors list? y for yes n for no: ")
    print()
    actor1.displayactor()  
    
    print()
    print()
    
    actor2list=[]
    actor2=Actor(actor2list)    
    actor2.setname("Hamza")
    actor2.setdob("13th Nov")
    actor2.setgender("m")
    actor2.displayactor()

    x = input("Do you want to add more movies to this actors list? y for yes n for no: ")
    while x!="n":
        movie=input("Enter a movie: ")
        actor2.addmovie(actor2list,movie)
        x = input("Do you want to add more movies to this actors list? y for yes n for no: ")
    print()
    actor2.displayactor()
    
    compareActor(actor1list,actor2list)
    
    
main()


#task 5 is attached with pdf
