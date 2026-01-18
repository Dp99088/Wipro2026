class Count_N:
    def __init__(self,n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            val=self.current
            self.current+=1
            return val
        else:
            raise StopIteration

numbers = Count_N(5)

for num in numbers:
    print(num)


#Question 2
def fibonacci(n):
    a,b = 0,1
    count = 0

    while count < n:
        yield a
        a,b = b,a+b
        count += 1
n = 7
for num in fibonacci(n):
    print(num)

#Question 3
num_iter = Numiterator(5)

for num in num_iter:
    print(num)

