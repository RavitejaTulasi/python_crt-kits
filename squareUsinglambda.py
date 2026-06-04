sq = lambda x : x*x
n = int(input("Enter a number: "))
print(sq(n))



#sum of variabblle number of arguments
def total(*num):
    print(sum(num))
total(1,2,3,4,5)