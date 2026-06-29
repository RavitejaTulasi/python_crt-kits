import heapq

def top_k_scores(scores, k):
    heap = []
    for score in scores:
        heapq.heappush(heap, score)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)

scores = [84, 92, 78, 95, 88, 73, 99, 61, 70,  85]
print("All Scores:", scores)
print("Top 3: ", top_k_scores(scores,3))
print("Top 5: ", top_k_scores(scores, 5))

print("\nnlargest(3):", heapq.nlargest(3,scores))
print("\nnsmallest(5):", heapq.nsmallest(5, scores))