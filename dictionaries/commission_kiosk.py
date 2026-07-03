prices = {"sketch":15,"lineart":30,"color":60,"custom":100}
total_bill = 0
while True:
  art = input("What type of art would you like? ")
  if art=="done":
    break
  elif art in prices:
    total_bill+=prices[art]
    print(f"Added to cart!")
  else:
    print("Sorry, we don't offer that.")
print("\n--- RECEIPT ---")
print(f"Your total comes to: ${total_bill}")
    
