scores=list(map(int,input("Enter the scores: ").split()))
average=(sum(scores)/len(scores))
print("Average NPS score:{:.2f}".format(average))
#print(f"Average NPS score:{average:.2f}")
