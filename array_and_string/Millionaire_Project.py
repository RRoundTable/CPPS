'''
link: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE

'''

def max_profit(prices):
    max_price = 0
    profit = 0
    for i in range(len(prices))[::-1]:
        max_price = max(max_price, prices[i])
        profit += max_price - prices[i]
    return profit