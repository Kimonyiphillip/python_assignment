my_list = [] #create a list

#  Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15) #Insert 15 at the second position (index 1)

# Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])

my_list.pop() # Remove the last element

#  Sort in ascending order
my_list.sort()

# Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Optional: print final list
print("Final list:", my_list)
