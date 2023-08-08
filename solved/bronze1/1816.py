import sys

n = int(sys.stdin.readline())
mx = 1000001
prime = []
isPrime = [True] * (mx)

for idx in range(2, int(mx ** 0.5)):
    if not isPrime[idx]: continue

    for y in range(idx * idx, mx, idx):
        isPrime[y] = False

for idx in range(2, mx):
    if isPrime[idx]: prime.append(idx)



def isVaild(num):
    for p in prime:
        if num % p == 0: return False
    return True


for _ in range(n):
    num = int(input())
    if isVaild(num):
        print("YES")
    else:
        print("NO")
