import random as rnd 


def sorted_square(array):
    output = [0] * len(array)
    in_l, in_r = 0, -1
    out_point = -1
    for i in range(len(array)):
        if abs(array[in_l]) >= abs(array[in_r]):
            output[out_point] = array[in_l] ** 2
            in_l += 1
        elif abs(array[in_r]) >= abs(array[in_l]):
            output[out_point] = array[in_r] ** 2
            in_r -= 1
        out_point -= 1

    return output



index_range = rnd.randint(1, 10000)

input_arr = []

for i in range(index_range):
    input_arr.append(rnd.randint(-10000, 10000))
input_arr = sorted(input_arr)

output = sorted_square(input_arr)




