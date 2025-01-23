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

