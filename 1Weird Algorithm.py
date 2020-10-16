"""
Idea :
Even : Divide by 2
Odd : Multiply by 3 + 1
Do this till n == 1

o/p : all the values of n during the working of the algo
"""

def weirdAlgo(n):
    if n == 1:
        return [1]
    else:
        values = [n]
        while n > 1:
            if n%2 == 0:
                val = n//2
                values.append(val)
            else:
                val = (n * 3) + 1
                values.append(val)
            n = val
        return values

if __name__ == "__main__":
    n = int(input())
    ans = weirdAlgo(n)
    for a in ans:
        print(a, end = " ")