## TIP CALCULATOR
print("Welcome to the tip calculator !")
total_bill = int(input("What was the total bill ?  $   "))
tip= int(input("How much tip would you like to give? 10, 12, or 15 ?   "))
people= int(input("how many people to split the bill?  "))
each_pay = (total_bill + tip)/people
print(f"Each person should pay: ${each_pay}")