balance = 999999
annualInterestRate = 0.18

epsilon = 0.01
testBalance = balance
min = balance / 12.0
max = (balance * (1 + annualInterestRate/12)**12) / 12
monthlyPayment = (min + max) / 2.0

while True:
	for month in range(1, 13):
		testBalance = (testBalance - monthlyPayment) * (1 + annualInterestRate/12)
	if abs(testBalance) < epsilon:
		print "Lowest payment: " + str(round(monthlyPayment, 2))
		break
	if testBalance < 0:
		max = monthlyPayment
	elif testBalance > 0:
		min = monthlyPayment
	monthlyPayment = (min + max) / 2.0
	testBalance = balance

