def min(a,*b):
	m = a
	for i in b:
		if i<m: m=i
	return m

def sum(a,b,*c):
	s = a+b
	for i in c:
		s += i
	return s

def grocery(order):
	discount = 25 if order > 200 else 0
	discount_amt = discount*order/100
	tax = 0.07*(order-discount_amt)
	return discount_amt,tax

def fare(distance):
	booking_fee = 2.5
	starting_price = 3
	cost = 1
	return booking_fee + starting_price + distance * cost

def main():
	order = 260
	discount,tax = grocery(order)
	print(discount)
	print(round(tax,2))

if __name__ == "__main__":main()
