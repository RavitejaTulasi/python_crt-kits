# Binary Search implementation in Python
#Binary search for integer array
def Binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left < right :
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: left = mid + 1
        else : right = mid - 1
    return  -1

arr = list(map(int,input("Enter the sorted array elements: ").split()))
target = int(input("Enter the target value: "))
idx = Binary_search(arr,target)
if idx != -1:
    print(f"Found element {arr[idx]} at index {idx}")
else:
    print("Element not found in the array")


# Binary Search for string array
def Binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left < right :
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: left = mid + 1
        else : right = mid - 1
    return  -1

arr = list(map(str,input("Enter the sorted array elements: ").split()))
target = (input("Enter the target value: "))
idx = Binary_search(arr,target)
if idx != -1:
    print(f"Found element {arr[idx]} at index {idx}")
else:
    print("Element not found in the array")