
class Animal:
	def talk(self):
		print("I have something to say")
	def walk(self):
		print("I am walking")
	def clothes(self):
		print("I have nice clothes")
class Duck (Animal):
  def __init__(self,value):
    self.c = value
  def quack(self):
    print "quaaaaaak ",self.c
  def walk(self):
    print "walk like a duck ",self.c

def main():
  donald = Duck(47)
  donald.quack()
  donald.walk()
  donald.talk()
  donald.clothes()

if __name__ == "__main__" : main()