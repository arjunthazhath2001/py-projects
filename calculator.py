import calc_art
print(calc_art.image)

def asknum():
    try:
        num1= int(input("\n\n WHATS THE FIRST NUMBER?: "))
        return num1
    except:
        print("Enter number only")
        return asknum()

def asknum2():
    try:
        num2= int(input("\n\n WHATS THE NEXT NUMBER?: "))
        return num2
    except:
        print("Enter number only")
        return asknum2()


def doOperation(n1,n2,op):
    if op=="+":
        return n1+n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    elif op=="-":
        return n1-n2


def main():
    num1= asknum()
    
    def calc(num):
        operation= input("+\n-\n*\n/\nPick an operation:")
        if(operation not in "+-/*"):
            print("wrong input")
            return
        num2= asknum2()        
        ans= doOperation(num,num2,operation)        
        print(f"{num} {operation} {num2} = {ans}")
        res= input(f"Type 'y' to continue calculting with {ans} or 'n' to start new calc")

        if res=="n":
            main()
        elif res=="y":
            calc(ans)
        else:
            print("THANKYOU FOR USING")
            return     

    calc(num1)
        # operation= input("+\n-\n*\n/\nPick an operation:")
        # if(operation not in "+-/*"):
        #     print("wrong input")
        #     return
        
        # num2= asknum2()
        
        # newAns= doOperation(ans,num2,operation)
        # print(f"{ans} {operation} {num2} = {newAns}")
   
main()