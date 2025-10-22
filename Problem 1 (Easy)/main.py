# Step 1: Define a function and create a dictionary

# Step 2: Loop through each number using enumerate()

# Step 3: Find the complement

# Step 4: Check if complement exists

# Step 5: Add the current number to the dictionary

# [2, 7, 11, 15]
# target = 9

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
        