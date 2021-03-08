def buy_and_sell_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        min_price_so_far = min(min_price_so_far, price)
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
    return max_profit

a = [310,370,275,275,260,260,260,230,230,230]
b = [324,23,54,2321,56,24,11,5,565,2,723,63,3]
print(buy_and_sell_once(a))
print(buy_and_sell_once(b))
