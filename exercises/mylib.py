def sum(a,b,*c):
	s = a +b
	for i in c:
		s = s +i
	return s

def min(*a):
	m = a[0]
	for i in a:
		if i<m:m=i
	return m

def grocery(order):
	discount = 25 if order > 200 else 0
	discount_amt = (discount/100)*order
	amt = order - discount_amt
	tax = 0.07*amt
	return discount_amt,tax

def main():
	order = 300
	discount, tax  = grocery(order)
	print("discount = {}".format(discount))
	print("tax = {}".format(tax))

if __name__ == "__main__":main()