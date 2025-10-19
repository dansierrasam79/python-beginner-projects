# Step 1: Create and write to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
    file.write("And here is the third line.")

# Step 2: Open and read the file line by line
line_count = 0
word_count = 0

with open("sample.txt", "r") as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        print(line.strip())  # Print each line without extra newline

# Step 3: Print the counts
print("\nTotal lines:", line_count)
print("Total words:", word_count)
