
print("тоннаж: ")
m = int(input())
n = int(input("рыбаков: "))
boat = 0
weight =[]
if (n >= 1) and (n <= 100):
    print(f"вес: ")
    for i in range(n):
        a = int(input())
        if (a >= 1) and (a <= m):
            weight.append(a)
        else:
            print(f"превышен вес лодки: {m}.")
        
else:
    print("нарушено число рыбаков:  1 ≤ n ≤ 100.")
 
while len(weight):
    boat += 1
    for i in range(len(weight)):
        t = min(weight)
        if weight[i] + t <= m:
            weight.pop(i)
            weight.pop(t)
        else:
            weight.pop(i)
print(boat)