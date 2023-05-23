case1 = [int(2), int(7), int(11), int(15)]
target = int(9)

# O(n) time / O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum-num, num]
        else:
            nums[num] = True
    return []

x = twoNumberSum(case1,target)

print(x)