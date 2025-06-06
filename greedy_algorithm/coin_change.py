import random
list_of_coin=[1,2,3,4]
money_req=int(input("Enter the req money = "))
coins_req =[]
def largest_coin(list_of_coin):
    greatest=random.choice(list_of_coin)
    
    for i in list_of_coin:
            if i > greatest:
                greatest = i
    return greatest



def number_of_coins(money_req,list_of_coin,coins_req):
    
    while money_req != 0:
        

        largest =largest_coin(list_of_coin)
        if largest <= money_req:
            coins_req.append(largest)
            money_req= money_req - largest
        else :
            list_of_coin.remove(largest)
        
    return [len(coins_req),coins_req]

print(number_of_coins(money_req,list_of_coin,coins_req))