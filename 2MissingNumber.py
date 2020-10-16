"""
Given n and an array of 1 to n-1. Find the missing number
"""


def missingVal(arr):
    actual_length = len(arr) + 1
    total = (actual_length * (actual_length+1))//2
    missed = total - sum(arr)
    return missed
if __name__ == "__main__":
    n = int(input())
    values = list(map(int,input().split()))
    print(missingVal(values))