# prints all divisors of a number
num = int(raw_input("What is your number? "))
if (num < 1):
	print ("Your number has no divisors")
else:
	possibleDiv = list(range(1,num+1))
	actualDiv = []
	for divisor in possibleDiv:
		if (num % divisor == 0):
			actualDiv.append(divisor)
	print ("Your number is divisible by: ")
	print (actualDiv)
