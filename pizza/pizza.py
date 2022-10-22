import numpy as np
test_cases = int(input())

for _ in range(test_cases):
    arr = np.fromstring(input(), sep = " ")[1:]
    if arr.size == 0:
        print(1)
        continue
    arr = np.mod(arr, 180)
    slices = np.unique(arr).size * 2
    print(slices)

