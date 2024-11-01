# if elif else

people = 9

if people > 10:
    print("too much people around")
elif people < 10:
    print("not enough people around")
else:
    print("we have the right number of people in")

# calculator python basic
operator = input("Enter an operator(+, -, /, *);")
num1 = int(input("Enter Number 1"))
num2 = int(input("Enter Number 2"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
else:
    print(num1 * num2)

# logic operators are and, or , not