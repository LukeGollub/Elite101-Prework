#Resturaunt chat program
#Prints out the menu and prices, can take orders
#Keywords are "Menu, Reservation, Special" as well as any Menu item

#Sets up order list
order = []

def generate_response(user_input):
  #Expected menu:
  # ---Menu---
  # Hamburger : $7.99
  # Chicken Sandwich : $8.29
  # Chicken Nuggets : $7.39
  # Fries : $2.99
  menuItems = [
    "Hamburger",
    "Chicken Sandwich",
    "Chicken Nuggets" ,
    "Fries"
  ]
  menuPrices = [
    "$7.99",
    "8.29",
    "$7.39",
    "$2.99"
  ]
  special = "Peppermint Mocha"
  specialPrice = "5.99"
  #Checks if user asks for menu and returns it
  if "menu" in user_input.casefold():
    menuResponse = "\n   ---Menu---\n"
    for item in menuItems:
      menuResponse+= item + " : " + menuPrices[menuItems.index(item)]+ "\n"
    return menuResponse
  #Checks if user asks for the special and returns it (with price)
  elif "special" in user_input.casefold():
    return f"\nTodays special is a {special} ({specialPrice})\n"
  
  
  #Checks to see if user asks to make a reservation
  elif "reservation" in user_input.casefold():
    y_n = input("\n\nWould you like make a reservation?\n")
    if y_n.casefold() == "yes":
      time = input("\n\nWhat time would you like to make the reservation?\n")
      name = input("\n\nWhat is the name for this reservation?\n")
      return f'Thank you {name}, a reservation has been made for {time}.'
    else:
       return "\n" + "Ok, anything else?\n"
  #If user asks for the special by name, ask them if they want to order it and add it to order
  elif special.casefold() in user_input.casefold():
     y_n = input("\n\nWould you like to add " + special + "(" + specialPrice+ ")" +" to your order?\n")
     if y_n.casefold() == "yes":
      order.append(f"{special} : {specialPrice}")
      newOrder = ""
      for orders in order:
        newOrder += f"--{orders}--\n"
      return f"\nYour current order is: \n{newOrder}"
  #Checks if user is asking for a menu item
  #Checks if user mentions a menu item then asks to add it to the order
  for item in menuItems:
    if item.casefold() in user_input.casefold():
      y_n = input(f"\n\nWould you like to add {item} ({menuPrices[menuItems.index(item)]}) to your order?\n")
      if y_n.casefold() == "yes":
        order.append(f"{item} : {menuPrices[menuItems.index(item)]}")
        newOrder = ""
        for orders in order:
          newOrder += f"-- {orders} --\n"
        return "\nYour current order is: \n" + newOrder
      #Else redirect user to the functions of the chat bot
      else:
       return "\n" + "Ok, anything else?"#"\n" + random.choice(responses) 
  else:
    return "\nTry asking FAQ about the menu, make a reservation, or make an order"#"\n" + random.choice(responses)

def init_chat():
  quit_character = 'q'
  #Starter Message that takes the first input
  user_input = input("\n \n \nHello, this is [generic fast food restraunt]'s automated chatbot, how can I help you?\n")
  
  while user_input.casefold() != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = f"{input(generate_response(user_input))}\n"

if __name__ == "__main__":
  init_chat()