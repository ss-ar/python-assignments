age = int(input("Enter the characters age: "))
hair_color = input("Enter the characters hair color: ")
has_secret_power = input("Does the character has secret power(yes/no): ")
is_shonen_protagonist = age>=14 and age<=17 and hair_color!="black" and hair_color!="brown" and has_secret_power=="yes"
print(f"\nFits the protagonist trope? {is_shonen_protagonist}")

