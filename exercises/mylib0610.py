def taxifare(distance):
	booking_fee = 2.5
	starting_fee = 3
	cost = 0.5
	fare = booking_fee+starting_fee+cost*distance
	return fare


def grocery(order):
	discount = 25 if order > 200 else 0
	discount_amt = order*discount/100
	tax = 0.07*(order - discount_amt)
	return discount_amt,tax

def main():
	distance = 7
	print(taxifare(distance))

#print(__name__)

if __name__ == "__main__":main()
