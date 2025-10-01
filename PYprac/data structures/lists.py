first_trees = [1,2,3,4,5,]  # Define firsttrees as an empty list or assign the appropriate value
#print('Option 1: ',first_trees)

tree_list = list(range(20,141,4))
#print('Option 2: ', tree_list)

tree_list.append(400)
#print('After appending 400: ', tree_list)

old_trees= [440,444,448,452]
combined_trees = tree_list + old_trees
#print('After combining old trees: ', combined_trees)

gymnosperms = [
   ["Pine", "Cedar", "Spruce"],        # conifers
   ["Cycas", "Sago palm", "Zamia"],    # cycads
]

# Extract conifers and cycads from gymnosperms
conifers = gymnosperms[0]
cycads = gymnosperms[1]

# Select Cycas and Sago palm
selected_plants = gymnosperms[1][1:3]
print(selected_plants)


ordered_plants = sorted(conifers + cycads)
print(ordered_plants)




