global Sword
global BowAndArrow
global money

Sword = False
BowAndArrow = False
import time
money = 100

def store():

	global Sword
	global BowAndArrow
	global money
				
	print"Store"
	time.sleep(1)
	print""
	if Sword == False:
		print"Sword -- $100"
		time.sleep(1)
	if BowAndArrow == False:
		print"Bow an Arrow -- $150"
		time.sleep(1)
	
	moneyStr = str(money)
	print("You have $" + moneyStr)
	time.sleep(1.5)	
	print""
	print("Do you want to buy anything today?('yes' or 'no')  ").lower()
	buy = raw_input("> ")
	if buy == "yes":
		print("What do you want to buy?('Sword','Bow and Arrow' or 'nothing')")
		choice = raw_input("> ").lower()
		if choice == "bow and arrow":
			if money >= 150:
				print"You just bought a Bow and Arrow!"
				BowAndArrow = True
				money = money - 150
			else:
				print("You don't have enough money.")
		if choice == "sword":
			if money >= 100:
				print"You just bought a Sword!"
				Sword = True
				money = money - 100
				print"hi"
			else:
				print"You don't have enough money."	
		if choice == "nothing":
			print "Now get out there and hammer those monsters!"
			time.sleep(1)
	if buy == "no":
		print "Now get out there and hammer those monsters!"
		time.sleep(1)

def storeStats():

	global Sword
	global BowAndArrow
	
	if Sword == True:
		print"Sword"
	
	else:	
		if BowAndArrow == True:
			print"Bow and Arrow"
	
		else:
			print"You haven't bought anything yet. Go to the Store to buy stuff"
	
			
	return Sword, BowAndArrow
	
def moneyValue():
	global money
	return money