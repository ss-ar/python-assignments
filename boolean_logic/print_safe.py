red = int(input("Enter the red value: "))
green = int(input("Enter the green value: "))
blue = int(input("Enter the blue value: "))
all_sum = red+green+blue
is_print_safe = red>=0 and red<=255 and green>=0 and green<=255 and blue>=0 and blue<=255 and all_sum<700 and red!=0 and green!=0 and blue!=0
print(f"\nIs color safe for printing? {is_print_safe}")

