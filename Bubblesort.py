# Sorting a list of numbers using Bubble Sort in Python
a=[]
for i in input("Enter numbers separated by space:").split(" "):
    a.append(int(i))
print(a)
swapped=0
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        k = j + 1
        if a[j] > a[k]:
            a[j],a[k] = a[k],a[j]
            swapped=1
    if swapped == 0:
        break
print(a)
