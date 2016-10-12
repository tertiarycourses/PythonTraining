# while True:
#     try:
#         i = int(input('Enter an integer: '))
#         print("You enter ",i)
#         break
#     except:
#         print("This is not an integer")

correct_number = 2

while True:
    try:
        guess = int(input('Please guess a number from 1 to 6 '))
        if (guess == correct_number):
            print("good job!")
            break
    except:
        print("Wrong guess, pls try again ")