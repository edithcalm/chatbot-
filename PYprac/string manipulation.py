# Example: concatenation

string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)

# Example: replication

original_string = "Python"
replicated_string = original_string * 3
print(replicated_string)

# Example: slicing – positive indexing

text = "Python is amazing"
substring = text[0:6]
print(substring)

# Example: upper() method

original_string = "hello, world!"
uppercase_string = original_string.upper()
print(uppercase_string)

# Example: strip() method

raw_input = "    This is a sentence with spaces.    "
trimmed_input = raw_input.strip()
print(trimmed_input)

# Example: replace() method

original_text = "Python is a powerful programming language."
modified_text = original_text.replace("Python", "JavaScript")
print(modified_text)

sentence = "Searching for a keyword in this sentence."
index = sentence.find("keyword")
print(index)



# Example: formatted concatentation
forest_name = "Mau Forest"
area = 400000
forest_type = "closed‐canopy montane"

print("The name of the forest is " + forest_name)
print("The area is " + str(area) + " hectares")
print("The forest type is " + forest_type)

# Example: format()
growth_rate = 2.5
forest_region = "Amazon"

print("The annual growth rate of trees in the {} forest is {}%.".format(forest_region, growth_rate))


# Example: f-strings
sfm_concept = "Sustainable Forest Management" 
biodiversity_importance = "maintaining biodiversity"
print(f"{sfm_concept} is crucial for {biodiversity_importance}.")
