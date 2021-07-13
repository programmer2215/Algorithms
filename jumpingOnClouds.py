a = [0, 0, 1, 0, 0, 1, 0, 1, 0]


def jumpingOnClouds(c):
    i = 0
    jump_count = 0
    while i < len(c) - 1:
        if i + 2 == len(c) or c[i + 2] == 1:
            i += 1
            jump_count += 1
        else:
            i += 2
            jump_count += 1
    return jump_count


print(jumpingOnClouds(a))

