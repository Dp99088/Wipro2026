from functools import reduce
#Question 1
for i in range(1, 21):
    print(i)

#Question 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#Question 3
square_numbers = list(map(lambda x: x**2, numbers))
print(square_numbers)

#Question 4
sum_of_even_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_even_numbers)

#Question 5
for index, number in enumerate(square_numbers):
    print(index, number)


