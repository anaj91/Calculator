# Lekcija 6 (3. domača naloga)

print ("Welcome to my simple calculator! You can try simple calculating operations.")

a = int(input("Add your first number:"))
b = int(input("Add your second number:"))
operation = input("Add operation (pick between + - * /)")

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)
else:
    print("Wrong input")