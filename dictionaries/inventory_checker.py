player_inv = {"gold":1500,"swords":1,"shields":1}
item_needed = input("What item do you want to use? ")
if item_needed in player_inv:
  print(f"You used the {item_needed}!")
else:
  print(f"Error: You don't have any {item_needed} in your inventory.")
