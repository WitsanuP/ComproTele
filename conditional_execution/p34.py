astr = input("Enter num1 num2 : ")
num1,num2 = astr.split()
num1 = int(num1)
num2 = int(num2)
if num2==0:
    print("Error divided by zero")
else:
    print(f"{num1} / {num2} = {num1/num2}")