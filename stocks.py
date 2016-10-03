"""
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
"""

# simple solution O(n2)


def get_max_profit(prices):
    profit_map = {}
    key = 0
    m_profit = -1
    for i in range(len(prices) - 1):
        temp = [prices[ndx] for ndx in range(i + 1, len(prices))]
        m = max(temp)
        profit = m - prices[i]
        profit_map[prices[i]] = (profit, m)
        if profit > m_profit:
            m_profit = profit
            key = prices[i]

    return m_profit

# O(n)


def better_get_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

if __name__ == '__main__':
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    print get_max_profit(stock_prices_yesterday)
    print better_get_profit(stock_prices_yesterday)
