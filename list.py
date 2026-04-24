my_list = [10,20,30,69,67] #ordered and changable
print("created list",my_list) #creating a list and printing it
print("Accessing index 2", my_list[2])# accessing a perticular index index starts from 0 
my_list.append(60)# adding to the last of the list
print(my_list)
my_list.insert(2,169)# inserting value at perticular position 
my_list.remove(10)# removing a perticular value 
popped_element = my_list.pop() # removing element from the end
print("popped element",popped_element)
my_list.sort() #sorting in ascending order
print(my_list)
my_list.sort(reverse=True)# sorting in descending order
print(my_list)  
my_list.reverse() # just reverses the list 
print(my_list)
