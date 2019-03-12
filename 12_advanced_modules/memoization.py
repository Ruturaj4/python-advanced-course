# memoization

import time

ef_cache = {}

def exp_fun(num):
    if num in ef_cache:
        return ef_cache[num]
    print("Computing....")
    time.sleep(1)
    result = num*num
    ef_cache[num] = result
    return result

result = exp_fun(4)
print(result)

result = exp_fun(10)
print(result)

result = exp_fun(4)
print(result)

result = exp_fun(10)
print(result)
