def divide(num1,num2):
    return num1/num2

print("select operation -\n"\
      "divide\n")

select = int(input("select operation"))

Number1 = int(input("Enter the first number"))
Number2 = int(input("Enter the second number"))
print(Number1, "/", Number2, "=",
      divide(Number1, Number2))