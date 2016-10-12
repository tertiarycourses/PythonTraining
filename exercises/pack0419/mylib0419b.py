def min(a,*b):
	m = a
	for i in b:
		if i<m: m=i
	return m

def grocery(order):
	discount = 25 if order > 200 else 0
	tax = 0.07*(order-discount*order/100)
	return (discount,tax)

