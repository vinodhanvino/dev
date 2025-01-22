


def rightPyramid(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=' ')
        print()

def leftPyramid(n):
    for i in range(0, n):
        for j in range(n-i-1):
            print(j, end=' ')
        for k in range(i):
            print("*", end=' ')
        print()

def reverseHalfPyramid(n):
    for i in range(0, n):
        for j in range(n-i-1):
            print("*", end=' ')
        for k in range(i+1):
            print(" ", end=' ')
        print()

def reversrightHalfAnother(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=' ')
        print()

def reverseLeftHalfAnother(n):
    for i in range(0,n):
        for j in range(i):
            print(" ", end=' ')
        for k in range(n-i):
            print("*", end=' ')
        print()

def hollowPattern(n):
    for i in range(0, n):
        for j in range(0, n):
            if j == 0 or j == n-1 or i == 0 or i == n-1:
                print("*", end=' ')
            else:
                print(" ", end=" ")
        print()

def numberIncreasePattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        print()

def numbericalPattern(n):
    num = 0
    for i in range(0, n):
        for j in range(i+1):
            num += 1
            print(num, end=' ')
        print()

def pyraminPattern(n):
    k = n-1

    for i in range(0, n):
        for k in range(0, k):
            print(end=' ')
        for j in range(0, i+1):
            print("*", end=' ')
        print()

def sumOfCharacter(character):
    result = {}
    for i in character.lower():
        result[i] = result.get(i, 0) + 1
    print(result)

def countWords(words):
    res = len(words.split())
    print(res)


from itertools import permutations

def permutation(char):
    char = char
    res = ["".join(x) for x in permutations(char)]
    print(res)
    print(len(res))


def findwordPresent(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    i, j = 0, 0
    while i < len1 and j < len2:
        if word1[i] == word2[j]:
            i += 1
        j += 1

    if i == len1:
        print("yes")
    else:
        print("No")




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



removeDuplicates([0,1,1,2,2,3])
# input_ = "(}"
# print(isvlaid(input_))

# countWords("Lion is our national animal")