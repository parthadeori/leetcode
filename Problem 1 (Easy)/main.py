def two_sum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

nums =[7, 3, 2, 5]
target = 8
print(two_sum(nums, target))
