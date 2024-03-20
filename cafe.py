# This program calculates the total stock available in the cafe based on the 4 items in the menu
# The calcualtion is based on the stock availability and the price of the item in the menu
# The print statement welcomes the user to the cafe 
# This list helps the user to understand the items available in the cafe
# The stock dictionary helps to identify the number stock availability for each item
# The price dictionary helps to identify the price  for each item
# Using the for loop we calculate the totalstock value based on the items price and avialability

print("Welcome to Cafe !!")

menu = ["Coffee","Tea","Sandwich","Milkshake"]

print(menu)

stock = { "Coffee": 50,
           "Tea" : 50,
           "Sandwich" :30,
           "Milkshake" : 50}
  
price = {"Coffee" : 4.50 ,
         "Tea" : 3.50 ,
         "Sandwich" : 5.50,
         "Milkshake": 3.75 }
total_stock_value = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_value = item_value + total_stock_value
    
print(float(total_stock_value))    
print(f"The total value of the stock in the cafe is £{total_stock_value}")   
    