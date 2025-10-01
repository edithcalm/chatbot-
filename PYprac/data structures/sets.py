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

