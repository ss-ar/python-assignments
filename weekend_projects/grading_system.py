grades = []
print("=== UNIVERSITY GRADING PORTAL ===")
student_name = input("Enter student: ")
assignment_1 = float(input("Enter grade for Assignment 1: "))
assignment_2 = float(input("Enter grade for Assignment 2: "))
assignment_3 = float(input("Enter grade for Assignment 3: "))
grades.append(assignment_1)
grades.append(assignment_2)
grades.append(assignment_3)
average = (grades[0]+grades[1]+grades[2])/3
if average>=90.0:
  grade="A"
elif average>=80.0:
  grade="B"
elif average>=70.0:
  grade="C"
else:
  grade="F"

print("\n Generating Report Card...")
print("\n ----------------------------")
print(f"STUDENT: {student_name}")
print(f"GRADES ON RECORD: {grades}")
print(f"FINAL AVERAGE: {average:.1f}")
print(f"LETTER GRADE: {grade}")
print(" ----------------------------")


