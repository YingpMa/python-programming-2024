# Write your solution here
def everything_reversed(my_list: list):
    new_list = []
    for item in my_list[::-1]:
        new_list.append(item[::-1])
    return new_list
