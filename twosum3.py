case1 = [int(2), int(7), int(11), int(15)]
target = int(9)

# O(nlog(n)) time / O(1) space
def twoNumberSum(array, targetSum):
    array.sort() # This built-in function has a time of O(log(n))
    left = 0
    right = len(array) -1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right-=1
    return []

x = twoNumberSum(case1,target)

print(x)