balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for month in range(1,13):
	print "Month: " + str(month)

	monthlyPayment = monthlyPaymentRate * balance
	totalPaid += monthlyPayment
	print "Minimum monthly payment: " + str(round(monthlyPayment, 2))

	balance = (balance - monthlyPayment) * (1 + annualInterestRate/12)
	print "Remaining balance: " + str(round(balance, 2))
    
print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))