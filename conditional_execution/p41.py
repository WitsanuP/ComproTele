astr = input("Enter name score : ")
name,score = astr.split()
score = float(score)
if score >= 82:
    grade = 'A'
elif score >= 68 :
    grade = 'B'
elif score >=54:
    grade = 'C'
elif score >= 40:
    grade = 'D'
else:
    grade = 'F'
print(f"{name} got {score:.2f} and {grade} grade !!!")