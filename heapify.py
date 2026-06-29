import heapq
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 2]
heapq.heapify(nums)
print("Heapified list: ", nums)
print("Root (min):", nums[0])
result = []
while nums:
    result.append(heapq.heappop(nums))
print("Sorted output:", result)