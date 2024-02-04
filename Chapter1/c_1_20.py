from random import randint

def my_shuffle(list):
    shuffle_list = []
    while len(shuffle_list) < len(list):
        while True:
            randomly_chosen = list[randint(0, len(list) - 1)]
            if randomly_chosen in shuffle_list:
                randomly_chosen = list[randint(0, len(list) - 1)]
            else:
                shuffle_list.append(randomly_chosen)
                break
    return shuffle_list

print(my_shuffle([1,2,4,5,6,7]))