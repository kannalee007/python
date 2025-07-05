nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4

window_sum = 0
for i in range(k):
    window_sum += nums[i]
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum = window_sum - nums[i - k] + nums[i]
    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum sum of subarray of size", k, "is:", max_sum)