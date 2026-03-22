student_name = input("Enter student name: ")
grade1 = float(input("Enter your math grade: "))
grade2 = float(input("Enter your physics grade: "))
grade3 = float(input("Enter your python grade: "))

average = (grade1 + grade2 + grade3)/3
if average >=90:
    scholarship = 35000
else:
    scholarship = 0

gpa = average/25

print("==============================")
print("    STUDENT REPORT CARD")
print("==============================")
print("Student: ", student_name)
print("Math: ",grade1)
print("Physics: ",grade2)
print("Python: ",grade3)
print("------------------------------")
print("Average: ",round(average, 2))
print("GPA: ",round(gpa, 2))
print("Scholarship: ",scholarship,"KZT")
print("==============================")

print("Scholarship granted:", average >= 90)
print("Perfect score:", grade1 == 100 and grade2 == 100 and grade3 == 100)