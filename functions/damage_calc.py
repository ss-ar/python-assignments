def calculate_damage(base_attack,combo_multiplier):
  final_damage = base_attack*combo_multiplier
  if combo_multiplier>=10:
    final_damage+=500
  return final_damage

print(calculate_damage(50,3))
print(calculate_damage(50,10))
  
