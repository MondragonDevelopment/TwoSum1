case1 = [int(2), int(7), int(11), int(15)]
target = int(9)

# O(n^2) time / O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

x = twoNumberSum(case1,target)

print(x)