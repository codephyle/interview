# Given a stream of incoming "buy" and "sell" orders (as lists of limit price, quantity, and side, like ["155", "3", "buy"]), determine the total quantity (or number of "shares") executed.

# A "buy" order can be executed if there is a corresponding "sell" order with a price that is less than or equal to the price of the "buy" order. Similarly, a "sell" order can be executed if there is a corresponding "buy" order with a price that is greater than or equal to the price of the "sell" order.

# It is possible that an order does not execute immediately if it isn't paired to a counterparty. In that case, you should keep track of that order and execute it at a later time when a pairing order is found. You should ensure that orders are filled immediately at the best possible price. That is, an order  should be executed when it is processed, if possible. Further, "buy" orders should execute at the lowest possible price and "sell" orders at the highest possible price at the time the order is handled.

# Note that orders can be partially executed.

# Sample Input 
# orders = [
#   ['150', '5', 'buy'],    # Order A
#   ['190', '1', 'sell'],   # Order B
#   ['200', '1', 'sell'],   # Order C
#   ['100', '9', 'buy'],    # Order D
#   ['140', '8', 'sell'],   # Order E
#   ['210', '4', 'buy'],    # Order F
# ]

# Sample Output
# 9

def process_orders(orders):
    
    buy, sell = [], []
    executed = 0

    for order in orders:
        price, quantity, side = int(order[0]), int(order[1]), order[2]

        if side == 'buy':
            # Match with the lowest sell order possible
            while sell and sell[0][0] <= price and quantity > 0:
                sell_price, sell_qty = heapq.heappop(sell)
                if sell_qty <= quantity:
                    executed += sell_qty
                    quantity -= sell_qty
                else:
                    executed += quantity
                    heapq.heappush(sell, (sell_price, sell_qty - quantity))
                    quantity = 0
            if quantity > 0:
                heapq.heappush(buy, (-price, quantity))
        
        elif side == 'sell':
            # Match with the higest buy order possible
            while buy and -buy[0][0] >= price and quantity > 0:
                buy_price, buy_qty = heapq.heappop(buy)
                if buy_quantity <= quantity:
                    executed_quantity += buy_quantity
                    quantity -= buy_quantity
                else:
                    executed_quantity += quantity
                    heapq.heappush(buy_orders, (buy_price, buy_quantity - quantity))
                    quantity = 0
                    
                if quantity > 0:
                    heapq.heappush(sell_orders, (price, quantity))

        else:
            print("invalid side. {side}") 

    return executed_quantity