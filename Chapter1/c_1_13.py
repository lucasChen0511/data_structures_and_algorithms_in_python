# pseudocode
# function(list):
#   reversed_list = []
#   for i in range(reversed_list_length - 1, 0, -1):
#       append list[i] to reversed_list
#   return reversed_list

def reverse_list_of_integers(list):
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list
print(reverse_list_of_integers([1,2,3,4,5,6,7]))
