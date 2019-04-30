# Sorting a list of numbers using Bubble Sort in Python
a=[int(i) for i in input("Enter numbers separated by space:").split(" ")]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        k = j + 1
        if a[j] > a[k]:
            a[j],a[k] = a[k],a[j]
print(a)
