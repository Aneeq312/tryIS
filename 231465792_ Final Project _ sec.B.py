#Global variables:
inventory=[]
cart=[]
ordernum=1000
customers={}
feedbacklist=[]

#Parent Class:
class person:
    
    def __init__(self,name,address,phonenumber):
        #Constructor
        
        self.name=name
        self.address=address
        self.phonenumber=phonenumber

    def displayinfo(self):
        #To Display information
        
        print()
        print("\n Name: %s\n Address: %s\n Phonenumber:%s"%(self.name,self.address ,self.phonenumber))
    

#Child class:
class employee(person):
    def __init__(self,empnum,name, address, phonenum):
        #Constructor
        
        self.empnum=empnum
        super().__init__(name,address,phonenum)
        self.orderstatus=""
        self.rider=""
        self.revenue=0.0
        
    "len() function will be used to make sure that customers{} is not empty"

    def displayorders(self):
        #To display orders of all customers
        
        if len(customers)>=1:
            for c in customers:
                c.displayinfo()
                c.displaydetails(customers[c])
        else:
            print("There are no customers!")
            
            
    def displaythisorder(self):
        #To display a specific order
 
        if len(customers)>=1:
            self.ordernum=int(input("Enter the order number: "))
            for c in customers:
                if self.ordernum==c.ordernum:
                    c.displayinfo()
                    c.displaydetails(customers[c])
                    break
            else:
                print("Not found!")
        else:
            print("There are no customers!")

    def changestatus(self):
        #To Change Order Status of a specific order
        
        if len(customers)>=1:
            self.ordernum=int(input("Enter the order number: "))
            for cust in customers:
                if self.ordernum==cust.ordernum:
                    self.orderstatus=input("Enter the status of Order: ")
                    cust.setstatus(self.orderstatus)
                    cust.getstatus()
                    break
            else:
                print("Not found!")
        else:
            print("There are no customers!")


    def updaterider(self):
        #To Update the rider of an order
        
        if len(customers)>=1:
            self.ordernum=int(input("Enter the order number: "))
            for cust in customers:
                if self.ordernum==cust.ordernum:
                    self.rider=input("Enter the name of rider: ")
                    cust.setrider(self.rider)
                    cust.getrider()
                    break
            else:
                print("Not found!")
        else:
            print("There are no customers!")

    def totalrevenue(self):
        #To Display total revenue earned by the restaurant
        
        for cust in customers:
            self.revenue=self.revenue+cust.bill
        print("Total Revenue: RS.",self.revenue)

#Child Class:
class customer(person):
    def __init__(self,name,address,phonenumber):
        #Constructor
        
        self.name=name
        self.address=address
        self.phonenumber=phonenumber
        super().__init__(self.name,self.address,self.phonenumber)
        "Global variable is called so its value can be changed"
        global ordernum
        self.ordernum=ordernum
        ordernum=ordernum+100        
        self.bill=0
        self.orderstatus="Pending."
        self.rider="Currently unavailable!"

    def setstatus(self,orderstatus):
        #Setter function
        self.orderstatus=orderstatus

    def getstatus(self):
        #Getter function
        return self.orderstatus

    def setrider(self,rider):
        #Setter function
        self.rider=rider

    def getrider(self):
        #Getter function
        return self.rider
        

    def displayinfo(self):
        #To Display Customer information.
        
        super().displayinfo()

    def calculatebill(self,corder):
        #To Calculate Bill of the order
        
        for items in corder.cart:
            self.bill=self.bill+(corder.q*items.itemprice)

    def displaydetails(self,corder):
        #To Display order Details
        
        print("- - - - - - - - - - - - - - - - - - -")
        print(" Order number: %d"%(self.ordernum))
        print("- - - - - - - - - - - - - - - - - - -")
        print("Items in cart:")
        corder.printcart(corder)
        print("Current order status: %s,\nRider: %s"%(self.orderstatus, self.rider))
        print("- - - - - - - - - - - - - - - - - - -")
        print("TOTAL BILL: RS.",self.bill)
        print("- - - - - - - - - - - - - - - - - - -\n")

    def payment(self,custobj,orderobj):
        #To receive Payment and update customers{}
        
        "Global variable is called so its value can be changed"
        global customers
        self.money=float(input("Enter the amount please: "))
        
        if self.money>=self.bill:
            self.change=self.money-self.bill
            print("Here is your change: RS.",self.change)
            value={custobj:orderobj}
            customers.update(value)


        else:
            print("Please provide the correct amount of money!")
            self.payment(custobj,orderobj)


class order:

    def setcart(self):
        #Setter Function
        self.cart=[]
    def getcart(self):
        #Getter Function
        return cart
    
    def addtocart(self,value):
        #To add item to cart
        
        if value not in self.cart:
            "This 'if' statement is used to verify that an item does not get added multiple times and just the quantity is updated if it is changed by the user."
            self.cart.append(value)

    def removefromcart(self,value):
        #To remove item from cart
        
        self.cart.remove(value)

    def setq(self,q,value):
        #Setter Function
        self.q=q
            
    def getq(self):
        #Getter Function
        return self.q
    
    def displayorderdetail(self,value):
        #To display information of the item
        print("\tItem Number:",value.itemnum,"\n\tItem Name:",value.itemname,"\n\tItem Price: RS.",value.itemprice,"\n\tTotal Quantity:",self.q,"\n\tTotal Price: RS.",(self.q*value.itemprice),"\n")

    def printcart(self,orderobj):
        #To print the whole cart
        
        for items in self.cart:
            orderobj.displayorderdetail(items)

class item:
    
    def __init__(self, itemnum, itemname, itemprice):
        #Constructor
        
        self.itemnum=itemnum
        self.itemname=itemname
        self.itemprice=itemprice
        

    def printdetails(self):
        #To Print Details
        print(self.itemnum,"||",self.itemname,"|| RS.",self.itemprice)
    
class allinventory:
    "This class is made to set the menu and view or make changes"
    #Constructor
    
    def __init__(self,todaysinventory):
        self.inventory=todaysinventory
        self.item1=item(1,"PlayStation 5", 150000.0)
        self.inventory.append(self.item1)
        self.item2=item(2,"XBOX 1 S", 127000.0)
        self.inventory.append(self.item2)
        self.item3=item(3,"Nitendo Switch",100000.0)
        self.inventory.append(self.item3)

    def addtoinventory(self,itemnum,itemname, itemprice):
        #To add item to menu
        
        self.item=item(itemnum,itemname,itemprice)
        self.inventory.append(self.item)

    def removefrominventory(self,itemnum):
        #To remove item from menu
        
        for item in self.inventory:
            if itemnum == item.itemnum:
                self.inventory.remove(item)

    def editprice(self,itemnum,price):
        #To Edit price of an item in current menu
        self.price=price
        for item in self.inventory:
            if itemnum == item.itemnum:
                item.itemprice=self.price

    def displayinventory(self):
        #To Display complete menu
        
        for i in self.inventory:
            i.printdetails()

class feedback:
    
    def __init__(self,name,phonenum,text):
        #Constructor
        
        self.name=name
        self.phonenum=phonenum
        self.text=text

    def displaythankyou(self):
        #To display Thankyou
        print("Thank you %s for you valueable feedback!"%(self.name))

    def addtolist(self,obj):
        #To add feed back to the list

        "Global variable is called"
        global feedbacklist
        feedbacklist.append(obj)

    def displayfeedback(self):
        print("========================================================")
        print(" Name: %s\n Phone Number: %s\n Feedback: %s"%(self.name,self.phonenum,self.text))
        print("========================================================")

    
def main():
    todaysinventory=[]
    inventory=allinventory(todaysinventory)
    #For the ease of the viewer or the user:
    
    print("...................................................................................\n")
    print("\t\t\t*** IMPORTANT INFORMATION ***:\n\nThe customer is allowed to make one choice, after that the Customer must press enter again to continue!\n\nFor the Employee There are **Three** Valid employee codes:\n\t\t1445\n\t\t1446\n\t\t1447,\n\nThe Employee does not have to enter password 'letmepass123'again unless he/she presses '9' to exit.\n")   
    print("...................................................................................\n\n\n")

    print("\nWelcome to GamersGeist\n")
    
    mainchoice=input("\nPress enter to continue: ")
    while mainchoice== "" or mainchoice== "letmepass123":
        #For Customer:
        
        if mainchoice=="":
            print("\n\t\t*Format*\nItem Number || Item Name || Item Price\n")
            inventory.displayinventory()
            
            choice=int(input("\n 1: Order now!\n 2: Display order details\n 3: Display contact details\n 4: Provide Feedback!\n 5: Exit.\n"))
            while choice !=5:
                "While loop is used so that when the user inputs 5 he can exit."
                if choice==1:
                    "A new order is set for the customer."
                    corder=order()
                    "An empty cart is attached with the new order."
                    corder.setcart()
                    corder.getcart()
                    orderchoice=int(input("\n 1: Add item to cart\n 2: Remove item from cart\n 3: View items in cart\n 4: Proceed to checkout\n"))
                    while orderchoice!=4:
                        "While loop is used so that if the user enters 4 he proceeds to checkout."
                        found=False
                        "'found' variable is used to check if the item selected exists in the menu of not."
                        if orderchoice == 1:
                            itemchoice= int(input("\n Enter item number: "))

                            for i in todaysinventory:
                                if itemchoice==i.itemnum:
                                    q=int(input(" Enter Total Quantity: "))
                                    corder.addtocart(i)
                                    corder.setq(q,i)
                                    corder.getq()
                                    found=True
                                
                            if found == False:
                                print("\n Nothing found!")
                            else:
                                print("\n Succesful!")

                        elif orderchoice == 2:
                            if len(corder.cart) >=1:
                                itemchoice= int(input("\n Enter item number: "))
                                for i in todaysinventory:
                                    if itemchoice==i.itemnum:
                                        corder.removefromcart(i)
                                        found= True
                                    
                                if found == False:
                                    print("\n Nothing found!")
                                else:
                                    print("\n Succesful!")
                            else:
                                print("*** Your cart is empty ***")
            
                        elif orderchoice == 3:
                            if len(corder.cart)>=1:
                                corder.printcart(corder)
                            else:
                                print("*** Your Cart is empty ***")


                        orderchoice=int(input("\n 1: Add item to cart\n 2: Remove item from cart\n 3: View items in cart\n 4: Proceed to checkout\n"))

                    if orderchoice==4:
                        if len(corder.cart)>=1:
                            name=input("\n Enter your name: ")
                            address=input(" Enter the address: ")
                            phnumber=input(" Enter your phonenumber: ")
                            cust=customer(name,address,phnumber)
                            cust.calculatebill(corder)

                            cust.displayinfo()
                            cust.displaydetails(corder)
                            cust.payment(cust,corder)

                        else:
                            print("*** Your Cart is empty ***")
                        break
                    
                elif choice==2:
                    if len(customers)>=1:
                        f=0
                        ordernum=int(input("Enter the order number: "))
                        for c in customers:
                            if ordernum==c.ordernum:
                                c.displaydetails(customers[c])
                                f=1
                        if f==0:
                            print("Order not found!")
                            
                    else:
                        print("There are no customers yet!")
                    break
                    
                
                elif choice==3:
                    print("\n* * * * * * * * * * * * *")
                    print("\tGamersGeist!!")
                    print("* * * * * * * * * * * * *\n")
                    print("\t\t\tPhone number: +92333-3333333")
                    print("\t\t\tE-mail: gamersgeistshop@gmail.com")
                    print("\t\t\tAddress: 25/H DHA phase 1, Lahore.")
                    break
            
        
                elif choice==4:
                    name=input("\nEnter your name: ")
                    phonenum=input("Enter your number: ")
                    text=input("Enter your feedback: ")
                    cfeedback=feedback(name,phonenum,text)
                    cfeedback.displaythankyou()
                    cfeedback.addtolist(cfeedback)
                    break
                    
                else:
                    print("Invalid choice!!")
                    break

            print("\nThank You for coming!\nGood bye!")
                    
                


        #For Employee:
        allemployee=[employee(1445,"Rahim","DHA p2","0323-4444444"),employee(1446,"Asad","DHA p3","0324-5555555"),employee(1447,"Zulfiqar","Cant","0320-6666666")]
        
        empfound=False
        "'empfound' variable is used to check if the employee exists in the allemployee list or not"
        if mainchoice=="letmepass123":
            empcode=int(input("\nEnter your Employee code: "))
            for emp in allemployee:
                "To check if the code entered matches some employee's number"
                if empcode == emp.empnum:
                    empfound=True
                    print("Welcome %s! \nPlease select what to you want to do:"%(emp.name))

                    choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))

                    while choice!=9:
                        "'choice' is inputed in every condition to initiate the while loop again, and the user does not have to press 'B' again and again."
                        if choice==1:
                            mchoice=int(input("1: Add to inventory.\n2: Remove from inventory.\n3: Edit price of an item.\n"))
                            if mchoice==1:
                                itemnum=int(input("\nEnter item number: "))
                                itemname=input("Enter item name: ")
                                itemprice=float(input("Enter item price: "))
                                inventory.addtoinventory(itemnum,itemname,itemprice)
                                

                            elif mchoice==2:
                                itemnum=int(input("\nEnter item number: "))
                                inventory.removefrominventory(itemnum)

                            elif mchoice==3:
                                itemnum=int(input("\nEnter item number: "))
                                itemprice=float(input("Enter item price: "))
                                inventory.editprice(itemnum,itemprice)

                            print("\nUpdated menu:")
                            inventory.displayinventory()
                           
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))

                        elif choice==2:
                            emp.displayorders()
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))

                        elif choice==3:
                            emp.displaythisorder()
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))
            
                        elif choice==4:
                            emp.changestatus()
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))
    
                        elif choice==5:
                            emp.updaterider()
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))

                        elif choice ==6:
                            if len(feedbacklist)>=1:
                                for feedbacks in feedbacklist:
                                    feedbacks.displayfeedback()
                            else:
                                print("There are no Feedbacks available!")
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))
                            
                        elif choice==7:
                            emp.totalrevenue()
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))

                        elif choice==8:
                            emp.displayinfo()
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))

                        else:
                            print("Invalid choice!")
                            choice=int(input("\n1: Edit inventory.\n2: Display all orders.\n3: Display a specific order.\n4: Set Status of an order.\n5: Set Rider of an order.\n6: Display all feedbacks.\n7: Display Total revenue.\n8: Display your information.\n9: Exit.\n"))
                    break
                
            if empfound==False:
                print("Nothing was found!")

        mainchoice=input("\nPress enter to continue: ")
        
        
    print("Take care! Stay Safe!")


main()
    
