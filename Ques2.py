from DAY1_Assignment.Ques1 import even_numbers

numbers = [1, 2, 3, 4, 5, 6, 2, 4]

#Question 1
squares_numbers = [x ** 2 for x in numbers]
print(squares_numbers)

#Question 2
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)

#Question 3
cube_numbers = {x: x ** 3 for x in numbers}
print(cube_numbers)