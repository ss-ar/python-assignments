portfolio_score = float(input("Enter portfolio score: "))
years_experince =int(input("Enter years of experience: "))
knows_3d =input("Do you know 3D software? (yes/no): ")
gets_interview = portfolio_score>=8.5 and (years_experince>=3 or knows_3d=="yes")
print(f"\nGets an interview? {gets_interview}")

