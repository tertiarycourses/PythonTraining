def fare(distance):
	start = 3
	booking = 3
	cost = 1
	return start+booking+cost*distance

def grocery(order):
	dis = 25 if order > 200 else 0
	dis_amt = dis*order/100
	tax = 0.07*(order-dis_amt)
	return dis_amt, tax

