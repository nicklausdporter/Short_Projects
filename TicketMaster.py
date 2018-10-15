#This is a program that calculates cost for customers to purchase tickets
TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100
#Run code continuously until we run out of tickets
while tickets_remaining > 0:
	print(f"\nThere are {tickets_remaining} tickets remaining!")
	user_name = input("What is your name?\n")
	tickets_wanted = input(f"\nHow many tickets would you like {user_name}?\n")
	try:
		tickets_wanted = int(tickets_wanted)
	except ValueError:
		print("Oh no, we ran into an issue, please try again")
	else:
		amount_tickets = tickets_wanted * TICKET_PRICE
		amount_due = amount_tickets + SERVICE_CHARGE

		print(f"""\nThe total cost for your tickets will be ${amount_tickets}.
There is a ${SERVICE_CHARGE} service fee.
The total amount you owe is ${amount_due}.
""")

		decision = input("Would you like to continue with this purchase?\nYes or No?\n")
		if decision.lower() == "yes" :
			print(f"\nFantastic {user_name}!\n")
			if tickets_wanted > tickets_remaining:
				print(f"\nWait! There are only {tickets_remaining} tickets left, {user_name}")
			else:
				tickets_remaining = tickets_remaining - tickets_wanted
				print(f"Your tickets have been purchased {user_name}!")
		#TODO: Gather Credit card information and Process it
		else:
			print(f"\nOkay! We hope you will change your mind, {user_name}!")
print("\nThere are no more tickets left! We look forward to seeing you at the show!")
