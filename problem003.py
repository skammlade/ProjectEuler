#find factors of number
import math
myNum=600851475143
myFactors=[]
for i in range(1,int(math.ceil(math.sqrt(myNum)))):
	if myNum%i==0:
		#print str(i)+', '+str(myNum/i)
		myFactors.append(i)
		myFactors.append(myNum/i)
maxPrimeFactor=2		
#for each of the factors of myNum
for currentFactor in myFactors:
	#print currentFactor
	isPrime=True
	#for every int from 2 to sqrt of current factor
	for i in range(2,int(math.ceil(math.sqrt(currentFactor)))):
		if currentFactor%i==0:
			isPrime=False
			#returns what int current factor is divisible by
			print str(currentFactor) + " is divisible by " + str(i)
			break

	if isPrime:
		if currentFactor>maxPrimeFactor:
			maxPrimeFactor=currentFactor
		print str(currentFactor)+ ' is prime :)' 
	else:
		print str(currentFactor)+ ' is NOT prime'
print 'largest prime factor is: ' + str(maxPrimeFactor) 