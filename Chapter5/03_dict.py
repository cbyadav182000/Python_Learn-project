# /some dictonary method
# Creating a dictionary
person = {'name': 'Chnadrabhan', 'age': 21, 'city': 'New delhi'}

# Accessing a value
print(person['name'])  # Output: Chandrabhan

# Adding a new key-value pair
person['email'] = 'cy6997898@gmail.com'

# Updating a value
person['age'] = 20

# Removing a key-value pair
person.pop('city')

# Checking if a key exists
if 'name' in person:
    print('Name is present')

# Getting all keys, values, and items
print(person.keys())   # Output: dict_keys(['name', 'age', 'email'])
print(person.values()) # Output: dict_values(['Chnadrabhan', 21, 'cy6997898@gmail.com'])
print(person.items())  # Output: dict_items([('name', 'Chandrabhan'), ('age', 21), ('email', 'cy6997898@gmaile.com')])

# Copying the dictionary
person_copy = person.copy()

# Clearing the dictionary
person.clear()
