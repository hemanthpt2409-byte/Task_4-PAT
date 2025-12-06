#1 Filter people under 18 and map names (using lambda, filter, map)

people = [
    {"name": "Anu",   "age": 17},
    {"name": "Ravi",  "age": 22},
    {"name": "Meera", "age": 19},
    {"name": "Kiran", "age": 16},
]

# keep only people whose age is 18 or more
adults = list(filter(lambda p: p["age"] >= 18, people))

# take only their names
adult_names = list(map(lambda p: p["name"], adults))

print("Adults:", adults)
print("Adult names:", adult_names)



#2  Product of all numbers using reduce + lambda

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)




#3 List comprehension of squares of even numbers (using a lambda to test even)

nums = [1, 2, 3, 4, 5, 6, 7, 8]

is_even = lambda x: x % 2 == 0

squares_of_even = [n ** 2 for n in nums if is_even(n)]

print("Squares of even numbers:", squares_of_even)



#4 Lambda to check if a string is a number

#This allows optional + / - sign and one decimal point.

is_number = lambda s: s.replace('.', '', 1).lstrip('+-').isdigit()

tests = ["123", "-45.6", "3.14.5", "abc"]

for t in tests:
    print(f"{t!r} ->", is_number(t))


#5 Lambda to extract year, month, day from a datetime object

from datetime import datetime

extract_ymd = lambda dt: (dt.year, dt.month, dt.day)

now = datetime.now()
y, m, d = extract_ymd(now)

print("Year:", y, "Month:", m, "Day:", d)


#6 Lambda to generate Fibonacci series up to n terms


from functools import reduce

fib_series = lambda n: (
    [] if n <= 0 else
    [0] if n == 1 else
    reduce(
        lambda seq, _: seq + [seq[-1] + seq[-2]],
        range(n - 2),
        [0, 1]
    )
)

print("Fibonacci (n=1):", fib_series(1))
print("Fibonacci (n=5):", fib_series(5))
print("Fibonacci (n=10):", fib_series(10))