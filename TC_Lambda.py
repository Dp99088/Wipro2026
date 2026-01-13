add = lambda a,b: a+b
print(add(3,5))

multi = lambda c,d: c*d
print(multi(200,10))

maximum = lambda x, y: x if x > y else y
print(maximum(10,40))

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)