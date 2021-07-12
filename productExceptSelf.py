from  random import randint as rand

array = [rand(1, 50) for x in range(10)]

def productExceptSelf(arr):
    products = []
    
    for i in range(len(arr)):
        cur_product = 1
        for left in arr[:i]:
            cur_product *= left
        if i != len(arr) - 1:
            for right in arr[i + 1: ]:
                cur_product *= right
        products.append(cur_product)
    
    return products

print(productExceptSelf(array))
