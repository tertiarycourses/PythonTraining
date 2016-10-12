class Duck:
	def __init__(self,color):
		self.color = color
	def quack(self):
		print("quaaaaaak")
	def walk(self):
		print("walk like a duck")
	def look(self):
		print("got a %s color" %self.color)

def main():
  donald = Duck('white')
  donald.quack()
  donald.walk()
  donald.look()

if __name__ == "__main__" : main()