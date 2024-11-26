cost_price = float(input("Enter the Cost Price of the product: "))
sell_price = float(input("Enter the selling price of the product: "))
if (cost_price<sell_price):
    print("The Seller has made profit")
    profit = sell_price - cost_price
    print(f'Cost Price: {cost_price}, Selling Price: {sell_price}, Profit Made: {profit}')
else:
    print("The Seller has incurred Loss")
    loss = cost_price - sell_price
    print(f'Cost Price: {cost_price}, Selling Price: {sell_price}, Profit Made: {loss}')