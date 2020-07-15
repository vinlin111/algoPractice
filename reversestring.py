def reverseString(s):

    start = 0
    end = len(s) - 1
    while start < end:
        s[end], s[start] = s[start], s[end]
        start += 1
        end -= 1
    


print(reverseString(['h', 'e', 'l', 'l', 'o']))