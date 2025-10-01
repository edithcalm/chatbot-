animal_tuple = tuple(["Yellow anaconda", "Reptile", 30.5, 20])
#print(animal_tuple)
#print(type(animal_tuple))

first_index = animal_tuple.index("Yellow anaconda")
#print(first_index)

# Return the element at index 2 from animal_tuple
third_item = animal_tuple[2]
#print(third_item)


# Slice animal_tuple from index 1 to index 3
sliced_tuple = animal_tuple[1:4]
#print(sliced_tuple)

# Append a new tuple at the end of animal_tuple
animal_tuple_new = animal_tuple + ("Swamp", False)
#print(animal_tuple_new)


# Append a duplicated value at the end of animal_tuple_new
animal_tuple_new = animal_tuple_new + (False,)
#print(animal_tuple_new)

# Return the number of elements in animal_tuple_new
length_of_tuple = len(animal_tuple_new)
#print(f"No. of attributes: {length_of_tuple}")

# Count the occurrence of the value False in animal_tuple_new
count_false = animal_tuple_new.count(False)
#print(count_false)

# Slice animals_combined from index 2 to index 4
animals_combined = ['Lion', 'Elephant', 'Dolphin', 'Eagle', 'Penguin', 'Parrot']
sliced_list = animals_combined[2:5]
# print(sliced_list)







