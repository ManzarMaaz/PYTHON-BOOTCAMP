print("Hey, Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10% 12% 15% : "))
people = int(input("How many people to split the bill? "))

tip_amount = tip/100
total_bill = bill + bill*tip_amount
bill_per_person = total_bill/people

print('Bill amount is ', bill)
print(f"Tip percentage is {tip}%")
print('Total tip amount is ',bill*tip_amount)
print('Total Bill amount is ',total_bill)
print('Bill per person is ', bill_per_person)
