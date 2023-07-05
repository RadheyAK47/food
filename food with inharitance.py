class parent ():
    def __init__(self):
        print("this is parent class")
    def menu(dish):
        if (dish=="Burger"):
            print("you can add the following toppings")
            print("More Cheese | More Veggies")
        elif (dish=="Coffee"):
            print("you can add the following toppings")
            print("More Ice-cream | More Chocolate")
        else :
            print("Enter an valid dish")
            
    def finalAmount(dish,addOns):
        if(dish=="Burger" and addOns=="More Cheese"):
            print("you need to pay Rs.80")
        elif(dish=="Burger" and addOns=="More Veggies"):
            print("you need to pay Rs.60")
        elif(dish=="Coffee" and addOns=="More Ice-cream"):
            print("you need to pay Rs.200")
        elif(dish=="Coffee"and addOns=="More Chocolate"):
            print("you need to pay Rs.150")
            
class child1 (parent):
    def __init__(self,dish):
        self.dish=dish
        
    def getMenu(self):
        parent.menu(self.dish)
        
class child2 (parent):
    def __init__(self,dish,addOns):
        self.dish=dish
        self.addOns=addOns
        
    def getFinalAmount(self):
        parent.finalAmount(self.dish, self.addOns)
        
child1Obj=child1("Burger")
child1Obj.getMenu()

child2Obj=child2("Coffee","More Ice-cream")
child2Obj.getFinalAmount()

        