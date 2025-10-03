eats_plants = {"Giraffe", "Elephant", "Bear", "Rabbit", "Fox"}
#print('Habivorous:', eats_plants)

# Create a set from a list using the set constructor
eats_meat = set(["Lion", "Tiger", "Bear", "Hawk", "Fox", "Lion"])
#print('Canivorous:',eats_meat)

# Set containing duplicates
eats_meat = {"Lion", "Tiger", "Bear", "Hawk", "Fox", "Lion"}
#print(eats_meat)  # Output: {'Bear', 'Fox', 'Lion', 'Tiger', 'Hawk'}

# Add the element "Cow" to the set eats_plants
eats_plants.add("Cow")
#print(eats_plants)

# Add multiple elements from another set
eats_meat.update({"Leopard", "Cheetah"})
#print(eats_meat)

# Remove the element "Rabbit" from set eats_plants
eats_plants.remove("Rabbit")
#print(eats_plants)

# Remove the element "Deer" from set eats_plants (no error is raised if the element is not found)
eats_plants.discard("deer")
#print(eats_plants)

# Create a new set with all the animals from the eats_meat and eats_plants sets
all_animals = eats_meat.union(eats_plants)
#print(all_animals)

# Create a new set with animals that are common in both eats_meat and eats_plants sets
omnivores = eats_meat.intersection(eats_plants)
#print(omnivores)

# Create a new set with animals that are only in the eats_meat set
carnivore_only = eats_meat.difference(eats_plants)
#print(carnivore_only)

# Check if eats_plants is a subset of all_animals
eats_plants_subset = eats_plants.issubset(all_animals)
# print(eats_plants_subset)


# creating a list
tree_list = ['Tamboti', 'Baobab', 'Umbrella thorn', 'Yellowwood', 'Fever Tree', 'Moringa',
             'Marula', 'Waterpear', 'Baobab', 'Fountain Tree', 'Papaya Tree', 'Indian Laurel', 'Moringa']

tree_set = set(tree_list)

# print(type(tree_set))   # confirm data type
# print("tree_list =", tree_list)
# print("tree_set =", tree_set)


# print("Number of trees in list =", len(tree_list))
# print("Number of trees in set =", len(tree_set))  # confirm duplicates removed


day_1_trees = {
    "Baobab", "Buffalo Thorn", "Bushwillow", "Jackalberry", "Knob Thorn",
    "Lala Palm", "Marula Tree", "Umbrella Thorn", "Weeping Boer Bean", "Sausage Tree"
}

day_2_trees = {
    "Mopane Tree", "Bushwillow", "Knob Thorn", "Jackalberry", "Nara Plant",
    "Wild Date Palm", "Natal Mahogany", "Tamboti", "Leadwood", "Bushwillow"
}


# Union
union_result = day_1_trees.union(day_2_trees)
#print("Union result:", union_result)

# Intersection
both_days = day_1_trees.intersection(day_2_trees)
#print("Trees in both days:", both_days)

# Difference (day_2 only)
diff_result = day_2_trees.difference(day_1_trees)
#print("Trees only in Day 2:", diff_result)

# Symmetric difference (one set only)
one_set_result = day_1_trees.symmetric_difference(day_2_trees)
#print("Trees in one set only:", one_set_result)



# both_days subset of day_1_trees?
#print(both_days.issubset(day_1_trees)) 


# hardwood trees check
hardwood_trees =  {"Yellowwood", "Leadwood", "Blackwood"}
#print(hardwood_trees.issubset(day_2_trees))


