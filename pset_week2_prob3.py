balance = 120
annualInterestRate = 0.18
bal = balance
ann = annualInterestRate
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12.0
fixedMonthlyPayment = round((lowerBound + upperBound) / 2, 2)
while True:
    for i in range(1, 13):
        remainingBalance = balance - fixedMonthlyPayment
        balance = round((remainingBalance + remainingBalance * annualInterestRate / 12.0), 2)
    if (abs(balance - 0)) < 0.01:
        print("Lowest Payment: " + str(round(fixedMonthlyPayment, 2)))
        break
    else:
        if balance < 0:
            upperBound = fixedMonthlyPayment
        elif balance > 0:
            lowerBound = fixedMonthlyPayment
        fixedMonthlyPayment = (lowerBound + upperBound) / 2
        balance = bal
        annualInterestRate = ann
