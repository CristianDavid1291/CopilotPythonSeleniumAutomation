tuples=(1, 2, 3, 4, "Cristian")  # Tuple of integers
print(tuples)  # Printing the tuple

#Dictionaries
my_dict = {
    "name": "Cristian",
    "age": 30,
    "city": "New York",
    3.14: "Pi",  # Key-value pair with a float key
} 
print(my_dict)  # Printing the dictionary
print(my_dict["name"])  # Accessing the value associated with the key "name"
print(my_dict.get("age"))  # Accessing the value associated with the key "age" using get method
print(my_dict.get(3.14))
