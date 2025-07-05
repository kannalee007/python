#two pointer
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [nums[left], nums[right]]  # Found pair
        elif current_sum < target:
            left += 1  # Move left pointer right
        else:
            right -= 1  # Move right pointer left
            
    return None  # No pair found

# Your test case:
nums = [2, 4, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print("Result:", result)