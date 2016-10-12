def add(a,b,*c):
	sum = a+b
	for i in c:
		sum += i
	return sum

def min(a,*c):
	min = a
	for i in c:
		if min > i:
			min = i
	return min
		
def circle(radius):
    pi = 3.1417
    area = pi*radius*radius
    perimeter = 2*pi*radius
    return (area,perimeter)

def sphere(radius):
    pi = 3.1417
    area = 4*pi*radius**2
    volumn = (4/3)*pi*radius**3
    return (area,volumn)

def areaoftri(base=3,height=8):
    return 0.5*base*height

def taxifare(distance,startprice=2.8):
	return startprice+2.8*0.5*distance

def main():
	smallest = min(7,8,5,9)
	print(smallest)

if __name__ == "__main__" : main()