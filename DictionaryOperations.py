# Create a dictionary representing a person
person = {"name": "Alice","age": 30,"city": "New York"}

# Access values by key
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Add new key-value pairs
person["email"] = "alice@example.com"
print("After adding email:", person)

# Update existing values
person["age"] = 31
person["city"] = "Los Angeles"
print("After updating age and city:", person)

# delete specified key-value pair
del person["age"]
person.pop("city")

print(person)
