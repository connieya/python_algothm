import sys
from collections import defaultdict
n = int(sys.stdin.readline())
answer = []

dict = defaultdict(bool)

for _ in range(n):
    arr = list(sys.stdin.readline().split())
    flag = False
    for idx , a in enumerate(arr):
        if flag : break
        if not dict[a[0].lower()]:
            flag = True
            dict[a[0].lower()] = True
            arr[idx] = '['+a[0]+']'+a[1:]
    if not flag:
        for i , ar in enumerate(arr):
            if flag : break
            for idx , a in enumerate(ar):
                if flag:break
                if not dict[a.lower()] :
                    flag = True
                    dict[a.lower()] = True
                    arr[i] = ar[:idx]+'['+ar[idx]+']'+ar[idx+1:]

    answer.append(arr)



for a in answer:
    print(*a)