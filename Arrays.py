scores = [85,90,78,92,88]

for i in range(len(scores)):
    print(f"scores[{i}] = {scores[i]}")

for score in scores: print(score)

for idx,val in enumerate(scores):
    print(f"Index {idx} -> {val}")

print([x*2 for x in scores ])



arr=[10,20,30,40]
#append
arr.append(50)
#insert
arr.insert(2,55)
#extend
arr.extend([60,70])
#concatination
new_arr=arr+[80,90]


#python built-in-Timsort O(n log n)
arr=[64,34,25,12,22,11,90]

arr.sort()                  #in-place ascending
arr.sort(reverse=True)      #in-place descending
s=sorted(arr)                       #returns a new sorted list


words = ["banana","apple","grape","orange"]
words.sort(key=len)     #using length of the word as key for sorting
print(words)