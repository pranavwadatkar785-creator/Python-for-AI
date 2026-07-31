prices = [7,1,5,3,6,4]

def brutef_profit(prices):
    l=len(prices)
    max_profit = 0
    for i in range(l):
        for j in range(i+1,l):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

print(brutef_profit(prices),"Brute Force Solution time complexity O[n^2].")

def best_profit(prices):
    l=len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(l):
        if prices[i]<=min_price:
            min_price = prices[i]
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

print(best_profit(prices),"Solution time complexity O[n].")