[1,2,3,"a",5,6,"b",7,8,"c"]

correct_number = 2

while True:
    try:
        guess = int(input('Please guess a number from 1 to 6 '))
        if (guess == correct_number):
            print("good job!")
            break
        else:
            guess = "not correct"
        for i in range(guess):
            pass
    except:
        print("Wrong guess, pls try again ")