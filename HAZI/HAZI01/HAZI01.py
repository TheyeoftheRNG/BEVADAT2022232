#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index
     
def subset(input_list, start_index, end_index):
    return input_list[start_index:end_index+1]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_index = 2
end_index = 6
my_subset = subset(my_list, start_index, end_index)
print("task1")
print(my_subset)  
print("-------------")

     

#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size
     
def every_nth(input_list, step_size):
    return input_list[::step_size]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
step_size = 2
my_subset = every_nth(my_list, step_size)

print("task2")
print(my_subset)  
print("-------------")


     

#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list
def unique(input_list):
    return len(input_list) == len(set(input_list))

     

print("task3")
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 3, 4]
print(unique(my_list1))  
print(unique(my_list2))  
print("-------------")


#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list
def flatten(input_list):
    flattened_list = []
    for i in input_list:
        if type(i) == list:
            flattened_list.extend(flatten(i))
        else:
            flattened_list.append(i)
    return flattened_list

print("task4")
my_nested_list = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
my_flattened_list = flatten(my_nested_list)
print(my_flattened_list)  
print("-------------")
     

#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args

def merge_lists(*args):

    concatenated_list = []
    for arg in args:
        concatenated_list.extend(arg)
    return concatenated_list

print("task5")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
my_merged_list = merge_lists(list1, list2, list3)
print(my_merged_list)  
print("-------------")

     


     

#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list
def reverse_tuples(input_list):
    reversed_list = [(t[1], t[0]) for t in input_list]
    return reversed_list

print("task6")     
my_list_of_tuples = [(1, 2), (3, 4), (5, 6)]
my_reversed_list_of_tuples = reverse_tuples(my_list_of_tuples)
print(my_reversed_list_of_tuples)  
print("-------------")


     

#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list
def remove_duplicates(input_list):
    return list(set(input_list))

print("task7")     
my_list_with_duplicates = [1, 2, 3, 2, 4, 3, 5]
my_list_without_duplicates = remove_duplicates(my_list_with_duplicates)
print(my_list_without_duplicates)  
print("-------------")

     

#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list
def transpose(input_list):
    return [list(x) for x in zip(*input_list)]
     
print("task8")  
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_transposed_matrix = transpose(my_matrix)
print(my_transposed_matrix)  
print("-------------")
     

#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size
def split_into_chunks(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]
    #x = [l[i:i + n] for i in range(0, len(l), n)]
    #https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
     

print("task9")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_chunks = split_into_chunks(my_list, 3)
print(my_chunks)  
print("-------------")     

#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict
def merge_dicts(*dicts):

    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict

print("task10")
my_dict1 = {"a": 1, "b": 2}
my_dict2 = {"c": 3, "d": 4}
my_dict3 = {"e": 5, "f": 6}
my_merged_dict = merge_dicts(my_dict1, my_dict2, my_dict3)
print(my_merged_dict)
print("-------------")



     

#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

def by_parity(input_list):
    even = []
    odd = []
    for num in input_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return {"even": sorted(even), "odd": sorted(odd)}

print("task11")
my_list = [1, 2, 3, 4, 5, 6, 7, 12, 10, 9]
my_dict = by_parity(my_list)
print(my_dict)  
print("-------------")
     


     

#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict
def mean_key_value(input_dict):

    output_dict = {}
    for key, value_list in input_dict.items():
        output_dict[key] = sum(value_list) / len(value_list)
    return output_dict
     

my_dict = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8], "c": [9, 10, 11, 12]}
output_dict = mean_key_value(my_dict)
print(output_dict)

     

#If all the functions are created convert this notebook into a .py file and push to your repo
     
