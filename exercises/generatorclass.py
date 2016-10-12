class inclusive_range:
    def __init__(self, *arg):
        numarg = len(arg)
        if numarg < 1:
            raise TypeError("Inputs must not be empty")
        elif numarg == 1:
            self.stop = arg[0]
            self.start = 0
            self.step = 1
        elif numarg == 2:
            (self.start, self.stop) = arg
            self.step = 1
        elif numarg == 3:
            (self.start, self.stop, self.step) = arg
        else:
            raise TypeError("Inputs must be not more than 3")

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
    object1 = inclusive_range(3,25,2)
    for i in object1:
        print(i)

if __name__ == "__main__":main()