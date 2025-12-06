#1 Split a list into even and odd numbers

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_list = []
odd_list = []

for value in numbers:
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)

print("Even numbers :", even_list)
print("Odd numbers  :", odd_list)


#2 Count primes and build a prime list

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    # check factors only till square root
    limit = int(n ** 0.5) + 1
    for k in range(2, limit):
        if n % k == 0:
            return False
    return True
prime_list = []
for value in numbers:
    if is_prime(value):
        prime_list.append(value)
print("Prime numbers :", prime_list)
print("Count of primes:", len(prime_list))

#3 Count how many numbers are Happy Numbers

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy(num: int) -> bool:
    seen = set()
    current = num
    while current not in seen:
        seen.add(current)
        digit_sum = 0
        for ch in str(current):
            digit_sum += int(ch) ** 2
        current = digit_sum
        if current == 1:
            return True
    return False

happy_numbers = []
for value in numbers:
    if is_happy(value):
        happy_numbers.append(value)
print("Happy numbers :", happy_numbers)
print("How many happy numbers:", len(happy_numbers))


#4 Sum of first and last digit of an integer
n = int(input("Enter an integer: "))
text = str(abs(n))
first_digit = int(text[0])
last_digit = int(text[-1])
digit_sum = first_digit + last_digit
print("First digit :", first_digit)
print("Last digit  :", last_digit)
print("Sum         :", digit_sum)



#5 All ways to make Rs.10 using 1, 2, 5, 10 rupee coins
total_amount = 10
ways = 0

print("Combinations (Rs1, Rs2, Rs5, Rs10):")

for c1 in range(0, total_amount + 1):
    for c2 in range(0, total_amount // 2 + 1):
        for c5 in range(0, total_amount // 5 + 1):
            for c10 in range(0, total_amount // 10 + 1):
                if c1 + 2*c2 + 5*c5 + 10*c10 == total_amount:
                    print(c1, c2, c5, c10)
                    ways += 1

print("Total number of ways:", ways)


#6 Find duplicates in three lists


list_a = [1, 2, 3, 4, 5, 10]
list_b = [3, 4, 5, 6, 7]
list_c = [0, 3, 4, 8, 9, 5]

# convert to sets and take intersection
common_values = set(list_a) & set(list_b) & set(list_c)

print("Values present in all three lists:", list(common_values))

#7 Find non-repeating in two lists

numbers = [9, 2, 3, 2, 6, 6, 7]
count_map = {}

for n in numbers:
    count_map[n] = count_map.get(n, 0) + 1

first_unique = None
for n in numbers:
    if count_map[n] == 1:
        first_unique = n
        break
print("First non-repeating element :", first_unique)

#8 Find the minimum in a rated and sorted list
nums = [5, 6, 7, 1, 2, 3, 4]
low = 0
high = len(nums) - 1

while low < high:
    mid = (low + high) // 2
    if nums[mid] > nums[high]:
        low = mid + 1
    else:
        high = mid
print("Minimum element in rotated list:", nums[low])


#9 Find a triplet whose sum = given value (e.g., 59)
nums = [10, 20, 30, 9]
target = 59
nums.sort()
n = len(nums)
found = False

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        s = nums[i] + nums[left] + nums[right]

        if s == target:
            print("Triplet found:", nums[i], nums[left], nums[right])
            found = True
            break
        elif s < target:
            left += 1
        else:
            right -= 1

    if found:
        break

if not found:
    print("No triplet sums to", target)

#10 Check if any sub-list has sum = 0
nums = [4, 2, -3, 1, 6]
seen_sums = set()
current_sum = 0
zero_sum_exists = False

for n in nums:
    current_sum += n
    if current_sum == 0 or current_sum in seen_sums:
        zero_sum_exists = True
        break
    seen_sums.add(current_sum)

print("Is there a sub-list with sum 0? :", zero_sum_exists)
