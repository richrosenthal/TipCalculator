#Trying to code this without actually watching the video 
#Author Richard Rosenthal *with grain of salt
#5-10-21 
#Sample Program
#Welcome to the tip calculator 
#What was the total bill? $124.56
#What percentage tip would you like to give 10, 12, or 15? 
#how many people to split the bill? 7
#Each person should pay:  $19.93


print("Welcome to Ricky's Tip calculator \n")

#Ask end-user for bill amount
totalBillAmount = input("What was the total bill?\n")

#Ask end-user for percentage of bill amount
tipPercentage = input("What percentage tip will you give? 15%, 18%, 20%, or 25% \n")

amountOfPeople = input("How many people are splitting the bill? \n")

#Calculate the amount each person should pay

newTotal = (float(totalBillAmount) * float(tipPercentage)/100) + (float(totalBillAmount))

perPersonAmount = newTotal / int(amountOfPeople)

print(f"Each person should pay: ${round(perPersonAmount, 2)}")

