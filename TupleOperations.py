numbers = (1, 2, 2, 3, 2, 4)
alphabets = ('a', 'b', 'c', 'a', 'd')
# count method 
# specifies how many times a value occurs in the tuple
count_of_two = numbers.count(2)  # Returns 3
print(count_of_two)

# index method
# returns the idx value where the value occurs first
index_of_c = alphabets.index('c')    # Returns 2
index_of_a = alphabets.index('a')    # Returns 0 (first occurrence)
index_after_one = alphabets.index('a', 1) # Searches from index 1, returns 3
print(index_of_c, index_of_a, index_after_one)
