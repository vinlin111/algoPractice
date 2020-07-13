def find_missing(sequence):

    tally_dict = {}
    for i in range(len(sequence) - 1):
        diff = sequence[i+1] - sequence[i]

        if diff not in tally_dict:
            tally_dict[diff] = 1
        else: tally_dict[diff] += 1

    sort_dict = sorted(tally_dict.items(), key=lambda x:(x[1], x[0]), reverse=True)
    
    x = [j for j in range(sequence[0], sequence[-1]+1, sort_dict[0][0])]
    
    return [num for num in x if num not in sequence][0]


def find_missing(sequence):

    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]
    step = max(set(diffs), key=diffs.count)
    return [num for num in range(sequence[0], sequence[-1], step) if num not in sequence][0]


    

print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))