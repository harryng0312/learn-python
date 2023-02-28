arr = [i for i in range(10)]
arr1 = arr[:6]

for v in arr:
    print(f"v: {id(v)}")
    pass


for i in range(len(arr)):
    print(f"arr[{i}]: {id(arr[i])}")
    pass
