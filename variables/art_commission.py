artist_name = "KASANOVA"
client_name = "Ssewanyana T."
commission_type = "Full Body Colour"
base_price = 250000.00
number_of_extra_characters = 2
extra_charater_fee = 50000.0
background_fee = 100000.0

total_extra_character_cost = number_of_extra_characters*extra_charater_fee
total_price = base_price+total_extra_character_cost+background_fee
deposit_required = total_price/2

print("************************************")
print(f"\tART COMMISSIONS BY {artist_name}")
print("************************************\n")
print(f"Billed To: {client_name}")
print(f"Project: {commission_type}\n")
print("--- CHARGES ---")
print(f"Base Price: Ush{base_price}")
print(f"Extra Characters (2 @ Ush{extra_charater_fee} each): Ush{total_extra_character_cost}")
print(f"Detailed Background: Ush{background_fee}\n")
print("====================================")
print(f"TOTAL PROJECT COST: Ush{total_price}")
print("====================================")
print("*** PLEASE NOTE: A 50% deposit is required to start. ***")
print(f">> DEPOSIT DUE: Ush{deposit_required}")
print("************************************")



