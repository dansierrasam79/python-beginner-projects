# 1. Print numbers from 1 to 10 using a for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=' ')
print("\n")  # Newline for separation

# 2. Calculate the sum of numbers from 1 to 100 using a for loop
total_sum = 0
for i in range(1, 101):
    total_sum += i
print("Sum of numbers from 1 to 100:", total_sum)

# 3. Print numbers from 10 down to 1 using a while loop
print("Numbers from 10 down to 1:")
n = 10
while n >= 1:
    print(n, end=' ')
    n -= 1
print()  # Final newline
