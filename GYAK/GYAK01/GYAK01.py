#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list


from ast import List, parse
from numbers import Number
from pickle import FALSE, TRUE
from xmlrpc.client import boolean



def contains_odd(input_list):
    hasodd = False
    for i in input_list:
        if i % 2 == 1:
            hasodd = True
            pass
        pass
    return hasodd



def taskmain1():
    print("task1")
    odd_list = [6,4,2,8,10,4,1]
    print(odd_list)
    if contains_odd(odd_list):
        print("has odd!")
    else:
        print("there are no odds!")

    print()
    no_odd_list = [6,4,2,8,10,4]
    print(no_odd_list)
    if contains_odd(no_odd_list):
        print("has odd!")
    else:
        print("there are no odds!")
    print("-------------------")
taskmain1()
    
     

#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

def is_odd(input_list):
    bool_list = []
    for i in input_list:
        if i % 2 == 1:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list





def taskmain2():
    print("task2")
    odd_list = [6,4,2,8,10,4,1]
    print(odd_list)
    print(is_odd(odd_list))
    

    no_odd_list = [6,4,2,8,10,4]
    print(no_odd_list)
    print(is_odd(no_odd_list))
    print("-------------------")
taskmain2()



#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2


def element_wise_sum(input_list_1, input_list_2):
    #1. list_1 is longer on deafult
    longer = False
    length = len(input_list_2)
    sum_list=input_list_1
    
    

    if len(input_list_2) > len(input_list_1):
        longer = True
        length = len(input_list_1)
        
        sum_list=input_list_2


    for i in range(length):
        if longer:
            sum_list[i] += input_list_1[i]
        else:
            sum_list[i] += input_list_2[i]
        
        
    return sum_list



def taskmain3():
    print("task3")
    list_1 = [6,4,2,8,10,6]
    print(list_1)

    list_2 = [6,4,2,8,10,7,1]
    print(list_2)
    print(element_wise_sum(list_1,list_2))

    print("-------------------")
taskmain3()     


     

#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

def dict_to_list(input_dict):
    output_list = []
    for i in input_dict.items():
        output_list.append(i)
        pass
    return output_list


def taskmain4():
    print("task4")
    dicty = {"asd" : 2, "dsa" : 4}
    print(dicty)

    print(dict_to_list(dicty))
    print("-------------------")
taskmain4()       


     

#If all the functions are created convert this notebook into a .py file and push to your repo

