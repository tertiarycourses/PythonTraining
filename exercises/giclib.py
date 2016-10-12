def grocery(order):

	discount = 20 if order > 200 else 0

	discount_amt = order*discount/100
	amt = order - discount_amt
	tax = amt*0.07

	return(discount_amt,tax)

def fare(distance):
	booking= 2.5
	starting = 3.5
	cost = 1
	fare = booking+starting+distance*cost
	return fare