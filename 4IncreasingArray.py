"""
Given an array, make it increasing by adding one at each turn
"""

def makeIncreasing(arr):
    c = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            diff = abs(arr[i-1] - arr[i])
            c += diff
            arr[i] += diff
        elif arr[i] >= arr[i-1]:
            continue

    return c

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    count = makeIncreasing(arr)
    print(count)