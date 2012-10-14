balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1,13):
	print "Month: " + str(month)

	monthlyPayment = monthlyPaymentRate * balance
	print "Minimum monthly payment: " + str(round(monthlyPayment, 2))

	balance = (balance - monthlyPayment) * (1 + annualInterestRate/12)
	print "Remaining balance: " + str(round(balance, 2))