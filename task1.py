import math

# Displaying the menu options and storing input as program in upper case
program =(input("""Choose either 'investment' or 'bond' from the menu below to proceed:\n
\nInvestment:\t -to calculate the amount of money you will earn on interest\n
Bond:\t\t -to calculate the amount you will have to pay on a home loan\n""")).upper()

# Using if and elif to determine what type of calculation to run
# If neither options are inputted then an error message is shown
if (program == "INVESTMENT"):
    present_value = float(input("How much money are you depositing? "))
    rate = float(input("What is the interest rate percentage? e.g '8' "))
    time = float(input("How many years will the investment be for? "))
    interest = input("What type of interest will it be? Compound or simple? ").upper() # using upper() to make sure user entry is not case sensitive

# Using a nested if conditional to determine what type of interest is to be used
# If neither options are inputted an error message is shown
    if (interest == "COMPOUND"):
        amount = present_value * math.pow((1 + rate/100), time)
        print(f"The final amount after {time} years is: R{round(amount,2)}") 
    elif(interest == "SIMPLE"):
        amount = present_value * (1 + (rate/100) * time)
        print(f"The final amount after {time} years is: R{amount}")
    else:
        print("You have not entered an applicable answer, please try again using 'compound' or 'simple'")

elif (program == "BOND"):
    present_value = float(input("What is the present property value."))
    rate = float(input("What is the interest rate percentage? e.g '8' "))/100/12
    time = int(input("How many months do you plan to pay over? "))
    amount =round((rate * present_value) / (1 - (1 + rate) **(-time)), 2)
    print(f"You will have to pay R{amount} each month for {time} months")


# Using an else statement here to display the error message if neither of the previous conditionals are true
else:
    print("You have not entered an applicable answer, please try again using 'investment' or 'bond'")
