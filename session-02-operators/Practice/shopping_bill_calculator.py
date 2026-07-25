print("========== SHOPPING BILL ==========")

customer_name = input("Enter your name: ")
product_name = input("Enter the product name: ")
price_of_product = int(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))

total_price = price_of_product * quantity

print("\n========== BILL ==========")
print("Customer Name:", customer_name)
print("Product Name:", product_name)
print("Price:", price_of_product)
print("Quantity:", quantity)
print("Total Price:", total_price)
print("==========================")
print("Thank you for shopping with us!")