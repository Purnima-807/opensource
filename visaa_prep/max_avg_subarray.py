def find_max_average(nums, n, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, n):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum/k
n, k = map(int, input().split())
nums = list(map(int, input().split()))
if len(nums)==n:
    result = find_max_average(nums, n, k)
    print(f"{result:.4f}")
