# Create a list of student scores
scores = [85, 92, 78, 95, 88]

# Calculate the average score
average_score = sum(scores) / len(scores)

# Find the highest and lowest scores
highest_score = max(scores)
lowest_score = min(scores)

# Count how many scores are above a certain threshold (e.g., 90)
threshold = 90
count_above_threshold = sum(1 for score in scores if score > threshold)

# Print the results
print("Scores:", scores)
print("Average score:", average_score)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print(f"Number of scores above {threshold}:", count_above_threshold)
