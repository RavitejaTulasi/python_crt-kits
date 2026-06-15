#without loops and conditions

num = int(input("Enter the amount: "))
n500=num//500
num=num%500
n200=num//200
num=num%200
n100=num//100
num=num%100
n50=num//50
num=num%50
n20=num//20
num=num%20
n10=num//10
num=num%10
n5=num//5
num=num%5
n2=num//2
num=num%2
n1=num//1
num=num%1

print(f"500: {n500}")
print(f"200: {n200}")
print(f"100: {n100}")
print(f"50: {n50}")
print(f"20: {n20}")
print(f"10: {n10}")
print(f"5: {n5}")
print(f"2: {n2}")
print(f"1: {n1}")