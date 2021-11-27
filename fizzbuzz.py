# This code snippet lets you do the infamous fizz buzz code challenge in a one liner python code
print(list(map(lambda x: (('Fizz' if x % 3 == 0 else '') + ('Buzz' if x % 5 == 0 else '')) or x, [num + 1 for num in range(100)])))
