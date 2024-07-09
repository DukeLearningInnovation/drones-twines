'''
item as single let abbreviation
Example we are using:
(s)hirt 26.00, (p)ants 32.50, (j)acket 65.00, (h)at 21.80
(u)mbrella 14.50
'''
def get_price(item_abbrev):
   # Given the abbreviation of an item, returns the price of the item
   # Parameters:
   #   item_abbrev (type: string): A string of one letter representing an item to buy
   # Returns (type:float): returns the price of the item
   if item_abbrev == "s":
       return 26.00
   elif item_abbrev == "p":
       return 32.50
   elif item_abbrev == "j":
       return 65.00
   elif item_abbrev == "h":
       return 21.80
   elif item_abbrev == "u":
       return 14.50
   else:
       return 0.0

def get_name(item_abbrev):
   # Given the abbreviation for an item, returns the name of the item.
   # Parameters:
   #   item_abbrev (type: string): A string of one letter representing an item to buy
   # Returns (type: string): the name of the item
   if item_abbrev == "s":
       return "shirt"
   elif item_abbrev == "p":
       return "pants"
   elif item_abbrev == "j":
       return "jacket"
   elif item_abbrev == "h":
       return "hat"
   elif item_abbrev == "u":
       return "umbrella"
   else:
       return "NO_ITEM"

def print_choices(items):
   # Prints all the items available in the store
   # Parameters:
   #   items (type: string): A string of abbreviations of all unique items in the store
   # Returns: None. The function should not return anything.
   print("You can buy any of these items.")
   for index in range(len(items)):
       print(items[index], "-", get_name(items[index])+",", get_price(items[index]))
   print()


def print_cart(cart):
   # Prints the items from the cart, one item per line, numbering them starting with 0
   # Parameters:
   #   cart (type: string): A string of abbreviations of items to buy
   # Returns: None. The function should not return anything.
   print("\nYou have the following "+str(len(cart)) + " items in your cart:")
   for index in range(len(cart)):
       print("item " + str(index+1), get_name(cart[index]))
   print()

def calculate_total(cart):
   # Calculate and return the total cost of all the items in the cart
   # Parameters:
   #   cart (type: string): A string of abbreviations of items to buy
   # Returns (type:float): The total price to purchase all the items in the cart.
   total = 0
   for index in range(len(cart)):
       total += get_price(cart[index])
   return total

def calculate_total_with_coupon(cart, item_number, coupon):
   # Calculates and returns the total cost of all the items in the cart, giving one item a discount
   # Parameters:
   #   cart (type: string): A string of abbreviations of items to buy
   #   item_abbrev (type: string): The abbreviation of the item that can receive a discount percentage off
   #   coupon (type: float): the percent discount for item_coupon
   # Returns (type: float): The total cost of all items in the cart, with
   #          item_coupon receiving the percentage discount given with coupon
   total = 0
   for index in range(len(cart)):
       price = get_price(cart[index])
       if item_number == index+1:
           price = price - (price * coupon/100.0)
       total += price
   return total

def driver():
   # Ask for the items and discount item and it's discount, then print
   #   the cost of all the items without the discounted item, followed by the
   #   the cost of all the items with the one item discounted.
   # Parameters:
   #   None
   # Returns: None: There is nothing to return.
   print("Welcome to Latoya's Cool Clothes!")
   print_choices("hsupj")
   print("Enter items to buy by their abbreviation.")
   print("Enter $ to stop")
   cart = ""
   count = 1
   item = input("enter item 1: ")
   while (item != "$"):
       cart += item
       count += 1
       item = input("enter item "+ str(count) + ": ")
   count -= 1
   print_cart(cart)
   item_for_coupon = int(input("Which item number has a coupon: "))
   coupon = float(input("What is the percent discount: "))
   print()
   total_no_coupon = calculate_total(cart)
   total_with_coupon = calculate_total_with_coupon(cart,item_for_coupon,coupon)
   print("Total without coupon is", total_no_coupon )
   print("Total with coupon is", total_with_coupon )
   print("You saved", total_no_coupon - total_with_coupon)
   print("Thank you for shopping with us. We hope you enjoy your items!")



if __name__ == '__main__':
   driver()
