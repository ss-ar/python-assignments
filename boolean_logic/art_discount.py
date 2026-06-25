total_cart_price = float(input("Enter total cart price: "))
if(total_cart_price>100):
    discount=total_cart_price*0.20
elif(total_cart_price>50):
  discount= total_cart_price*0.10
else:
  discount = 0
final_price = total_cart_price+discount
print("-- CHECKOUT ---")
print(f"")

