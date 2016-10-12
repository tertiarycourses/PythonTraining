squares = [i**2 for i in range(10)]
print(squares)

squares3 = [i**2 for i in range(30) if i %3 == 0]
print(squares3)

squares_dict = {i:i**2 for i in range(10)}
print(squares_dict)