grade = ["A","B","C","D","E","F","G"]

for x in grade:
    y = input("What is the weightage of block " + x + "? \nCP for College Prepatory \nH for Honors \nAP for Advanced Placement \nN for Non-Weighted:\n\n")
    for i in range(len(grade)):
        if grade[i] == x:
           grade[i] = y
    pass

for a in grade:
    class_gpa = float(input("What is your percentage in class " + str(grade.index(a) + 1) + "?\n\n"))
    if class_gpa >= 98.0:
        class_gpa = 4.0
    elif class_gpa <= 97.0 and class_gpa >= 93.0:
        class_gpa = 3.7
    elif class_gpa <= 92.0 and class_gpa >= 90.0:
        class_gpa = 3.5
    elif class_gpa <= 89.0 and class_gpa >= 87.0:
        class_gpa = 3.3
    elif class_gpa <= 86.0 and class_gpa >= 83.0:
        class_gpa = 3.0
    elif class_gpa <= 80.0 and class_gpa >= 82.0:
        class_gpa = 2.7
    elif class_gpa <= 77.0 and class_gpa >= 79.0:
        class_gpa = 2.3
    elif class_gpa <= 73.0 and class_gpa >= 76.0:
        class_gpa = 2.0
    elif class_gpa <= 70.0 and class_gpa >= 72.0:
        class_gpa = 1.7
    elif class_gpa <= 67.0 and class_gpa >= 69.0:
        class_gpa = 1.3
    elif class_gpa <= 63.0 and class_gpa >= 66.0:
        class_gpa = 1.0
    elif class_gpa <= 60.0 and class_gpa >= 62.0:
        class_gpa = 0.7
    elif class_gpa <= 59.0:
        class_gpa = 0.0
    
    if a == "H" or a == "h":
        class_gpa = class_gpa + 0.5
    if a == "AP" or a == "ap":
        class_gpa = class_gpa + 1.0
    if a == "N" or a == "n":
        grade.remove(a)
        pass
    for b in range(len(grade)):
        if grade[b] == a:
            grade[b] = class_gpa
    pass

total_gpa = sum(grade)/len(grade)
print("Your total gpa is " + str(total_gpa) + "!")