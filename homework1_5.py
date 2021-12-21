income = int(input("Please enter the income of the company:"))
loss = int(input("Please enter company costs:"))

if income > loss:
    print("Good job! You make a profit!")
    print(f"Your profit: {income - loss}")
    print(f"Revenue profitability: {(income - loss) / income * 100}%")
    workers = int(input("How many people in your company?"))
    print(f"Profit per one person is: {(income - loss) / workers}")

elif income < loss:
    print("You are unprofitable.")
    print(f"Your loss: {income - loss}")

else:
    print("You have no profit or loss.")

