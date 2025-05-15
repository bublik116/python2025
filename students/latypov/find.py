my_list = [5, 3, 7, 3, 9, 10]
target_element = 3
def first_index(my_list, target):
    for index, value in enumerate(my_list):
        if value == target:
            return index
    return -1
result = first_index(my_list, target_element)
print(result) 
