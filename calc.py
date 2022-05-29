
sum = 0
sub = 0
mult= 1
div = 0
mod = 0

print("===SIMPLE CALCULATOR====")
print("Conventions used in this code: \n ")
print("for Addition PRESS + \n")
print("for substraction PRESS - \n")
print("for multiplication PRESS * \n")
print("for division PRESS \\ \n")
print("for substraction PRESS % \n")

print("Let's calculate!\n")

looper = True

while looper:
    num1 = int(input("\nEnter first number: \n"))
    num2 = int(input("\nEnter second number: \n"))

    operators = ["+" , "-" , "/" , "%", "*" ]

    opr = input("what operation you want to perform?")

    if opr not in operators:
        print("\nInvalid operator: Please enter a valid operator\n")
    else:

        print("\n -----Results------\n")

        #testing for the type of operatins to perform on the numbers 
        if opr == "+" :
            sum = num1 + num2
            print(f"{num1} + {num2} = {sum}\n")
        elif opr == "-":
            sub = num1 - num2
            print(f"{num1} - {num2} = {sub}\n")
        elif opr == "*" :
            mult = num1 * num2
            print(f"{num1} * {num2} = {mult}\n")
        elif opr == "%":
            mod = num1%num2
            print(f"{num1} % {num2} = {mod}\n")
        else:
            if num1==0 or num2==0:
                print("cannot divide with 0")
            else:
                div = float(num1/num2)
                print(f"{num1} / {num2} = {div}")
        
    more = input( "\nDo you want to perform more calculations?\n\npress (n) to end stop ")

    if more == "n":
        looper = False
        break
        

