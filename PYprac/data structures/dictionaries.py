our_first_dictionary = {}
type(our_first_dictionary)
our_first_dictionary['first_key']='first_value'

#print(our_first_dictionary)
duplicate_key_dict = {
    'first_key': 'first_value',
    'first_key': 'second_value',
    'extra_key': 'extra_value'
}
#print(duplicate_key_dict)

#print("Before update:", our_first_dictionary)
our_first_dictionary['first_key'] = 100  # updating existing key
#print("After update:", our_first_dictionary)

# add multiple key-value pairs
an_extra_key_value_dict = {'extra_key': 'extra_value', 'another_extra_key': 'another_value'}
our_first_dictionary.update(an_extra_key_value_dict)
#print("After adding new pairs:", our_first_dictionary)

del our_first_dictionary['another_extra_key']
#print("After deleting:", our_first_dictionary)







