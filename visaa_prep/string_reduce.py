s = input()
def reduced_str(s):
    res =""
    count = 1
    for i in range(1, len(s)):
        if(s[i] == s[i-1]):
            count += 1
        else:
            res += s[i-1] + str(count)
            count = 1
    res += s[-1] + str(count)
    return res
print(reduced_str(s))