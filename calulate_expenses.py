qty = int(input("Enter Qualnity: "))
price_per_item = float(input("Enter price in float: "))

total_cost = qty * price_per_item

if (total_cost > 5000):
    discount = total_cost * 0.10
    final_cost = total_cost - discount
    print(f'A discount of 10% is applied. Discount amount: {discount:.2f}')
    print(f'Total expenses: {final_cost:.2f}')
else:
    print("No discount")
    print(f'Total expenses: {total_cost:.2f}')