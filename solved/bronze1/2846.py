n = int(input())

arr = list(map(int, input().split()))

ans = 0
prev = arr[0]
for idx in range(1, n):
    if arr[idx] - arr[idx - 1] > 0:
        ans = max(ans, arr[idx] - prev)
        continue
    prev = arr[idx]

print(ans)