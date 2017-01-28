balance = 20
annualInterestRate = 0.2
fixedMonthlyPayment = 0
b = balance
a = annualInterestRate
while True:

    for i in range(1, 13):
        remainingBalance = balance - fixedMonthlyPayment
        balance = (remainingBalance + remainingBalance * annualInterestRate / 12.0)
    if balance <= 0:
        print("Lowest Payment: " + str(fixedMonthlyPayment))
        break
    else:
        fixedMonthlyPayment += 10
        balance = b
        annualInterestRate = a
