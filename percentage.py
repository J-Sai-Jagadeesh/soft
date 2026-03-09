m=int(input("marks of maths:"))
a=int(input("marks of english:"))
s=int(input("marks of science:"))

total_marks=(m+a+s)
avg=total_marks/3
percentage= (total_marks/300)*100
grade=""
if percentage>=90:
    grade="A"
elif percentage>=80:
    grade="B"
elif percentage>=70:
    grade="C"
else:
    grade="P"    
print(f"total Marks:{total_marks}")
print(f"average Marks:{avg}")
print(f"grade:{grade}")


