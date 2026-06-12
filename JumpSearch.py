import math 
def junmp_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step,n)-1] < target :
        prev =step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step,n):
            return -1
    
    if arr[prev] == target:
        return prev
    return -1

arr = list(map(int,input("Enter the sorted array elements: ").split()))
target = int(input("Enter the target value: "))
idx = junmp_search(arr,target)
print(f"Found element at index {idx}")