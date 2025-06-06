def number_of_coin(coins,amount):
    dp=[float("inf") for i in range(amount+1)]#creating a list upto amount and keeping each number of coin infinity cuz we don't know real number of coin required
    dp[0]=0#base case if the amount is zero we need zero coins
    for i in range (amount+1):#To got the coins required from amount  0 to amount given by user
        for coin in coins:# To check which coin is more suitable to use
            if coin<= amount:# To check wether the coin is greater then amount or not
                dp[i]=min(dp[i],dp[i-coin]+1)#Checks given the minimum number of coins required 
    
    return dp[amount]#Returinig the minimum number of coins 

coins =[1,2,4]#list of coins that are available 
amount = int(input("Enter the ammount:- "))  #taking the amount from user
print(number_of_coin(coins, amount))# calling the function 
