set_a = {10, 20, 30, 40, 50} # collection of values which are all different 
set_b = {30, 40, 50, 60, 70}
print("Created Set A:", set_a)
for element in set_a:
    print(element, end=" ") # accessing using a loop 
union_set = set_a.union(set_b) # union of two sets
intersection_set = set_a.intersection(set_b) #intersection of two sets
difference_set = set_a.difference(set_b) #difference of two sets 



