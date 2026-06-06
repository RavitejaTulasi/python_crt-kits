n=7
revenue = []
for i in range(n):
    ele = int(input("Enter revenue for day {}: ".format(i+1)))
    revenue.append(ele)
print(f"Total Revenue: {sum(revenue)} | Best Day: {max(revenue)} | Worst Day: {min(revenue)}")


#using higher order functions
Revenue = list(map(int,input("Enter the revenue for 7 days :").split()))
print(f"Total Revenue: {sum(Revenue)} | Best Day: {max(Revenue)} | Worst Day: {min(Revenue)}")