num = int(input("What number will you enter? "))
numSum = 0

while num != 0:
	numSum = numSum + num
	num = int(input("What number will you enter? "))

print ("The sum of the numbers entered is " + str(numSum))