
Price_list = [4,8,1,23,6,5,2,7,3,8]

def maxProfit(prices): 
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    max_profit = 0
    min_price = prices[0] #first buy price is equal to the first price in price list
    for i in range(1,len(prices)): # traverse through list of stock prices starting after the first price
        min_price = min(prices[i], min_price) #lowest price is either current price in price list or previous lowest price
        current = prices[i] - min_price #current profit is equal to current price minus the current lowest price
        max_profit = max(max_profit, current) #maximum profit is equal to current profit or previous maximum price
    return max_profit #return final maximum price

print(maxProfit(Price_list))
