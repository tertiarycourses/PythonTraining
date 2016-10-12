class Animal:
  count = 0
  def __init__(self,color):
    self.color = color
    Animal.count += 1

  def talk(self):
    print("talk like an animal")

  def displaycolor(self):
    print("color is ",self.color)

  def displaycount(self):
    print("number of animals are ",Animal.count)

class Duck (Animal):
  def __init__(self,name):
    self.name = name
  def quack(self):
    print("quaaaaaak ")
  def walk(self):
    print("walk like a duck ")
  def displayname(self):
    print("my name is ",self.name)

class Dog (Animal):
  def bark(self):
    print("woooooooof ")
  def walk(self):
    print("walk like a dog ")

def main():
  duck1 = Duck("donald")
  duck1.quack()
  duck1.walk()
  duck1.talk()
  duck1.displayname()

  dog1 = Dog("white")
  dog1.bark()
  dog1.walk()
  dog1.talk()
  dog1.displaycolor()

if __name__ == "__main__" : main()