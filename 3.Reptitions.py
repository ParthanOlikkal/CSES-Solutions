"""
Find max length substring with same value
"""

def repetitions(s):
    if len(s) == 1:
        return 1
    m = 0
    c = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            c += 1
            m = max(c, m)
        else:
            c = 1

    #print(m)
    if m == 0:
        return c
    return m


if __name__ == "__main__":
    s = input()
    print(repetitions(s))