commission_db ={}
def calculate_total(db):
    total =0
    for prices in db.values():
      total+=prices
    return total

def add_commission(db,client_name,price):
    db[client_name] = price
    return "Added successfully!"

while True:
    print("=== FREELANCE ART MANAGER ===")
    print("1. Add new commission")
    print("2. View tota revenue")
    print("3. Quit")
    option = int(input("Choose an Option: "))

    if option!=1 and option!=2 and option!=3:
        print("Sorry choose the correct option.")
    else:
        if option == 1:
            client_name = input("Client Name: ")
            price = float(input("Price: "))
            add_commission(commission_db,client_name,price)
        elif option == 2:
            print(f"Current Clients: {commission_db}")
            total_revenue = calculate_total(commission_db)
            print(f"Total revenue: ${total_revenue}")
        elif option == 3:
            print(">>> Shutting down... Have a great weekend!")
            break

