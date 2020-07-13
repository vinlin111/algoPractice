def goodVsEvil(good, evil):

    goods = [1,2,3,3,4,10]
    evils = [1,2,2,2,3,5,10]

    good_counts = [int(x) for x in good.split(" ")]
    evil_counts = [int(x) for x in evil.split(" ")]

    good_sum = sum([goods[i] * good_counts[i] for i in range(len(goods))])
    evil_sum = sum([evils[j] * evil_counts[j] for j in range(len(evils))])

    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    
    elif evil_sum > good_sum:
        return "Battle Result: Evil eradicates all trace of Good"

    else:
        return "Battle Result: No victor on this battle field"

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))