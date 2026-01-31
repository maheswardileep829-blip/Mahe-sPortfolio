print("            Budget Calculator         ") #Name
print("-" * 40)


income = float(input("What's your monthly income? $"))       #Calculation of actual budget
rent = float(input("How much do you spend on rent each month? $"))
groceries = float(input("How much do you spend on groceries each month? $"))
gas = float(input("How much do you spend on gas each month? $"))
miscallaneous = float(input("How much do you spend on other things each month? $"))
total_expenses = rent + groceries + gas + miscallaneous
total_budget= income - total_expenses



print ("-" * 40)
print ("MONTHLY BUDGET:")          #Actually displaying the budget
print ("$", total_budget)
print ("-" * 40)
if total_budget > 100:             #Giving advice based on how much you are saving per month
    print ("Great job! You are saving over $100 dollars a month")
elif total_budget > 0:
    print ("Good job, but try to cut the expenses a little")
if total_budget < 0:
    print ("You are spending more than you earn each month. Cut back on spending")
print ("-" * 40)