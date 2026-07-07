slayer_db = {}
def add_record(db, name, demons_defeated):
  db[name]= demons_defeated
  return "Record Updated successfully!"

def calculate_total_demons(db):
  total = 0
  for demons in db.values():
    total+=demons
  return total

while True:
  print("== DEMON SLAYER CORPS TERMINAL ==\n1. Log Slayer Record\n2. View Corps Stats\n3. Quit")
  option = input("Choose an option: ")
  if option=="1":
    slayer_name = input("\nWhat is your name? ")
    demons_defeated = int(input("How many demons have you defeated? "))
    print(add_record(slayer_db,slayer_name,demons_defeated))
  elif option=="2":
    print(f"\nCurrent Roster: {slayer_db}")
    print(f"Total demons defeated by Corps: {calculate_total_demons(slayer_db)}")
  elif option=="3":
    print("\nShutting down..... Keep your sword sharp!")
    break
  else:
    print("\nInvalid Input, try again!")

