import random

SIZE = 11500

random_list = [random.randint(-100, 100) for _ in range(SIZE)]

with open("random_numbers{}.txt".format(SIZE), "w") as file:
    for number in random_list:
        file.write(str(number) + " ")
"""
sorted_list = [i for i in range(SIZE)]

with open("sorted_numbers{}.txt".format(SIZE), "w") as file:
    for number in sorted_list:
        file.write(str(number) + " ")
"""
