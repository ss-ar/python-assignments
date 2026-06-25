print("--- HERO ASSOCIATION SYSTEM ---")
character_power = int(input("Enter character's power: "))
print("\nAnalyzing power level....")
if(character_power>=10000):
  print("Rank: S-CLASS (Legendary)")
elif(character_power>=5000):
    print("Rank: A-CLASS (Elite)")
elif(character_power>=1000):
  print("Rank: B-CLASS (Pro)")
else:
  print("Rank: C-CLASS (Needs Training)")


