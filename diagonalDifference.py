array_input = [
    [3, 2, 5, 6, 10],
    [5, 6, 7, 6, 9],
    [2, 9, 7, 5, 8],
    [3, 2, 7, 5, 5],
    [5, 6, 7, 5, 7]
]

def diagonal_diff(array):
    l_diagonal, r_diagonal = 0,0
    for i in range(len(array)):
        
        l_diagonal += array[i][i]
    for j in range(0, len(array)):
        
        r_diagonal += array[j][0-(j + 1)]
    
    diff = abs(l_diagonal - r_diagonal)

    return diff


print(diagonal_diff(array_input))






