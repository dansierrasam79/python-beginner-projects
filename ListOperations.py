# Create a list of numbers
my_numbers = [1, 5, 8, 12]

# Access elements by index
print("First element:", my_numbers[0])
print("Last element:", my_numbers[-1])

# Add elements
my_numbers.append(20)  # Add 20 at the end
print("After append:", my_numbers)

# Remove elements
my_numbers.remove(5)  # Remove the element 5
print("After remove:", my_numbers)

popped_value = my_numbers.pop()  # Remove and return the last element
print("Popped value:", popped_value)
print("After pop:", my_numbers)

# Calculate sum, mean, min, and max
total = sum(my_numbers)
mean = total / len(my_numbers)
minimum = min(my_numbers)
maximum = max(my_numbers)

# Print results
print("Sum:", total)
print("Mean:", mean)
print("Min:", minimum)
print("Max:", maximum)
