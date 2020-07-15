def twoSum(nums, target):
    l = {}
    for ind, val in enumerate(nums):
        val_to_find = target - val
        if val_to_find in l:
            return [l[val_to_find], ind]
        l[val] = ind
    return
    




print(twoSum([2,7,11,15],9))
