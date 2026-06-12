def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr=list(map(int,input("Enter the array elements: ").split()))
target=int(input("Enter the target value: "))
idx = linear_search(arr,target)
print(f"Found element at index {idx}")