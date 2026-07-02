gems = 500
while gems>=100:
  print(f"You have {gems} gems.")
  spend_gems = input("Spend 100 gems to pull a character? (yes/no): ")
  if spend_gems == "no":
    break
  else:
    gems-=100
    print("** You got a new 5-star Character! **")
print("Thanks for playing! You saved 400 gems.")
