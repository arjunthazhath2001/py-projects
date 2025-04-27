import auction_art
import os

bidList={}

print(auction_art.hammer)

print("WELCOME TO SECRET AUCTION PROGRAM")


def askbid():
    try:
        bid= int(input("\n\n WHATS YOUR BID?: "))
        return bid
    except:
        print('\n\n**********Enter a valid amount**********')
        return askbid()

def bidding():
    name= input("\n\n WHATS UR NAME?: ")
    newbid= askbid()
    print(newbid)
    bidList[name]=newbid
    response= input("\n\n ARE THERE ANY OTHER BIDDERS. Type y or n.: ")
    if response=="y":
        os.system('clear')
        bidding()
    else:
        maxBid= max(bidList.values())
        for key in bidList:
            if bidList[key]==maxBid:
                print("************************************************")
                print(f"\n\nThe winner is {key} with a bid of {maxBid}\n\n")
                print("************************************************")
        return

bidding()