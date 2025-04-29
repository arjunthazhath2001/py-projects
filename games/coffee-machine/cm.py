MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0



def reduceResources(choice):
    global resources
    global money
    for key in resources:
        resources[key]-= MENU[choice]['ingredients'][key]
    money+= MENU[choice]['cost']
    return



def checkResource(choice):
    for key in resources:
        if not (resources[key] >= MENU[choice]['ingredients'][key]):
            return [False,key]
    return [True,None]



def checkAmount(choice,user_amount):
    if not (MENU[choice]['cost']<=user_amount):
        return [False,0]
    return [True,user_amount-MENU[choice]['cost']]
            


def insertCoins():
    quarters=0
    dimes=0
    nickles=0
    pennies=0
    
    print("Please insert coins.")
    try:
        quarters= int(input("\nHow many quarters? "))
        dimes= int(input("\nHow many dimes? "))
        nickles= int(input("\nHow many nickles? "))
        pennies= int(input("\nHow many pennies? "))
        amount= (quarters * 0.25) + (dimes * 0.10) + (nickles* 0.05) + (pennies* 0.01)
    except:
        print("\nEnter proper amount\n")
        return insertCoins()
    return round(amount,2)


  
def game():
    user_amount=0
    choice= input("What would you like? (espresso/latte/cappuccino): ")

    if choice=="report":
        print(f"Water: { resources['water'] }ml\nMilk: { resources['milk'] }ml\nCoffee: { resources['coffee'] }gm\nMoney: ${money}\n")
    elif choice=="off":
        return
    elif choice in ["latte","espresso","cappuccino"]:
        res,item= checkResource(choice) #checks if resources are available
        
        if res: #if res is true 
            user_amount= insertCoins() #then asks user to insert coins, calculates the total amount and returns that 
            
            allowed, balance= checkAmount(choice,user_amount)
            if allowed:
                reduceResources(choice) 
                print(f"Here is ${balance} in change.")
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry, thats not enough money")
        else:
            print(f"Not enough {item}")
    else:
        print("Wrong choice")
    game()
    
        
    
game()