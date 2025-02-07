def removeDuplicates(nums):
    result = set()
    k = 0
    for i in range(0,len(nums)):
        if i not in  result:
            result.add(i)
            nums[k] = i
            k += 1
        else:
            nums.pop(k)
    return k


def solve(nums, target):
    hv = []
    tmp = 0

    try:
        return nums.index(target)
    except:
        idx = 0
        for i in range(len(nums)):
            if nums[i] > target:
                return i
        return len(nums)

def isvlaid(char):
    open = {
            '(': ')',
            '{':'}',
            '[':']',
             }
    result = []
    for i in char:
        if i in open :
            result.append(open[i])
        elif result and i == result[0] :
            result.pop()
        else:
            return False

    return not result

def check_polimer(word):
    word = word.lower()
    return word == word[::-1]


def missingNumber(numbers):

    for i in range(min(numbers),len(numbers)+1):
        if i not in numbers:
            return i
    return -1

print(missingNumber([9,6,4,2,3,5,7,0,1]))
