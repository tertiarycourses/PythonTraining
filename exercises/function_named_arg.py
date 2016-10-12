def main():
    i = sum(inclusive_range(1,20,1))
    print(i)

def inclusive_range(start, stop, step):
    i = start
    while (i <=stop):
        yield i
        i += step
if __name__ == "__main__": main()
