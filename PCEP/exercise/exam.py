names = ['Alice', 'Lance', 'Bob', 'Mike']
all_names_1 = names[:]  # This will create a new list based of names
all_names_2 = names   # This will make the same list have different named variable
names.append('Brock')

print(sorted(all_names_1))      # Will return a new list withour Brock
print(sorted(all_names_2))      # Will return the original list named names.

print(sorted(names))            # Original list named names