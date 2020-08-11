import multiplication
import PowerFunc
import Add
import Subtract
import dividenew
choice=''
while(choice!='done'):
    print("Choose:\n")
    print("1) Addition\n")
    print("2) Subtraction\n")
    print("3) Multiplication\n")
    print("4) Division\n")
    print("5) Power\n")
    s = int(input())
    if s==1:
        num1=int(input("Enter number 1"))
        num2=int(input("Enter number 2"))
        add(num1, num2)
    if s==2:
        num1=int(input("Enter number 1"))
        num2=int(input("Enter number 2"))
        subtract(num1, num2)
    if s==3:
        num1=int(input("Enter number 1"))
        num2=int(input("Enter number 2"))
        multiplication(num1, num2)
    if s==4:
        num1=int(input("Enter number 1"))
        num2=int(input("Enter number 2"))
        divide(num1, num2)
    if s==5:
        num1=int(input("Enter number 1"))
        num2=int(input("Enter number 2"))
        power(num1, num2)
    print("If done, enter 'done'")
    choice=input()