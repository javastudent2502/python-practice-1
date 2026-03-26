student_name = input("Enter your name :")
grade1= float(input("Enter your math grade :"))
grade2= float(input("Enter your physics grade :"))
grade3 = float(input("Enter your python grade :"))

average = (grade1+grade2+grade3)/3

if average >= 90:
    letter = 'A'
elif average >= 75:
    letter = 'B'
elif average >= 60:
    letter = 'C'
elif average >=50:
    letter = 'D'
else:
    letter = 'F'
    
scholarship = average >= 90 and grade1 >= 70 and grade2 >= 70 and grade3 >= 70
    
    
print("==============================")
print("    STUDENT REPORT CARD")
print("==============================")
print("Student: ", student_name.upper())
print("Math: ",grade1)
print("Physics: ",grade2)
print("Python: ",grade3)
print("------------------------------")
print("Average: ",round(average, 2))
print("Letter grade: ",letter)
print("Scholarship: ",scholarship)
print("==============================")


grades = [grade1,grade2,grade3]
subjects = ["Math","Physics","Python"]

for i in range(len(grades)):
    grade=grades[i]
    subject=subjects[i]
    
    if grade>=90:
        comment="Excellent"
    elif grade>=75:
        comment="Good"
    elif grade >=60:
        comment="Satisfactory"
    else:
        comment="Fail"
    print(subject,":",grade,"--",comment)

print("Name uppercase :",student_name.upper())
print("Name lowercase :",student_name.lower())
print("Name length :",len(student_name))
print("Masked name:", student_name.replace(student_name[0],"*",1))




