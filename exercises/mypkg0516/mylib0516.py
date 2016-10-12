def min(a,*b):
	min = a
	for i in b:
		if i<min: min=i
	return min

def sum(a,b,*c):
	sum = a+b
	for i in c:
		sum += i
	return sum

def fare(distance):
	booking = 3
	start = 3
	cost = 0.5
	fare = cost*distance+start+booking
	return fare

def grocery(order):
	discount = 25 if order > 200 else 0
	discount_amt = order*discount/100
	tax = 0.07*(order*(1-discount/100))
	return discount_amt, tax

def main():
	print(min(4,8,6,3,7,8))

if __name__=='__main__':main()