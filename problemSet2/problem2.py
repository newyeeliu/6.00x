balance = 4773
annualInterestRate = 0.2

for monthlyPayment in range(10, balance, 10):
	testBalance = balance
	for month in range(1, 13):
		testBalance = (testBalance - monthlyPayment) * (1 + annualInterestRate/12)
	if testBalance <= 0:
		print "Lowest payment: " + str(monthlyPayment)
		break