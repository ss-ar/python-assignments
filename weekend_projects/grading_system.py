#Option 1
# def average_calc(a,b,c):
#   avg = (a+b+c)/3
#   return avg

#Cleaner approach using the builtin sum and len functions
def average_calc(grade_list):
  total = sum(grade_list)
  avg = total/len(grade_list)
  return avg
  
grades = []
print("=== UNIVERSITY GRADING PORTAL ===")
student_name = input("Enter student: ")
assignment_1 = float(input("Enter grade for Assignment 1: "))
assignment_2 = float(input("Enter grade for Assignment 2: "))
assignment_3 = float(input("Enter grade for Assignment 3: "))
grades.append(assignment_1)
grades.append(assignment_2)
grades.append(assignment_3)
# average = average_calc(grades[0],grades[1],grades[2])
average = average_calc(grades)
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


