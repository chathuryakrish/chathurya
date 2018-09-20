import random
a=input("if 'r' to roll a dice 'q'to quit")
while True:
	if(a=="r"):
		print(random.randint(1,6))
	elif(a=="q"):
		print("quit")
		exit()
	else:
		print("give either 'r' or 'q'")