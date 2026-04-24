my_dict = {'name':'Ishan','City':'Pune','College':'MIT','Age':26}#stores data in key value pair 
print(my_dict['name']) #accessing value using the key
print(my_dict.get("Age")) # if key is not there programe doesnt crash 
my_dict["Age"]=19 #updating dictionary 
print(my_dict)
my_dict["Trait"]="confident" # adding key value combination 
removed_value = my_dict.pop("City") # removing a specific key 
print(my_dict)
del my_dict["name"]#deleting a key
print(my_dict)
my_dict.clear()#clearing dict 
print(my_dict)







