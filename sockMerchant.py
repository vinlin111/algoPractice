def sockMerchant(n, ar):
    maxpairs = n // 2
    count = 0
    pairs = {}
    for i in ar:
        if i not in pairs:
            pairs[i] = 1
        else:
            pairs[i] += 1
            if pairs[i] % 2 == 0:
                count += 1
    return pairs, count

print(sockMerchant(9,[10,20,20,10,10,30,50,10,20]))