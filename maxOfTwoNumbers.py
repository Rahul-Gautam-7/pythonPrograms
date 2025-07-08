# Maximum of two numbers

num1=34
num2=32
if type(num1)==int and type(num2) ==int :
    if num1 >num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("Both numbers are the same.")