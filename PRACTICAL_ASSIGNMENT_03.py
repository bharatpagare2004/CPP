print("Enter Five Subject Marks to Generate Reslt:")
marks =[]
for i in range(5):
    m = int(input("Enter Subjet Maarks:"))
    marks.append(m)
minMarks = min(marks)
maxMarks = max(marks)
totalMarks =sum(marks)
percent = (totalMarks*100)/500
if (minMarks<40):
    print("Student Status is Fail")
elif (maxMarks>100):
    print("You have Entered Wrong Marks for the Subjet")
elif(percent >=75):
    print("Student Passed with Distinction")
elif(percent>=60 and percent<75):
    print("Student Passed with First Class")
elif(percent>=50 and  percent< 60):
    print("Student Passed with Second Class")
elif(percent>=40 and percent<50):
    print("Student Passed with First Class")        



