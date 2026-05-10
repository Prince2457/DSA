import csv

def encrypt(message, shift=3):
    encrypted_message1 = ""
    for char in message:
        shift_action1 = chr(ord(char) + shift) 
        encrypted_message1 += shift_action1
    return encrypted_message1
    
def decrypt(message, shift=3)-> str :
    decrypted_message = ""
    for char in message:
        shift_action = chr(ord(char) - shift) 
        decrypted_message += shift_action
    return decrypted_message    

#big O notation
def two_sum(nums, target):
    seen = {}
    for i in range (len(nums)):
        need = target - nums[i]
        if need in seen: 
            return [seen[need], i]
        seen[nums[i]] = i 
        

def find_duplicates(data):
    for i in range (len(data)):
        for j in range (i+1, len(data)):
            if data[i]== data[j]:
                return True
    return False

def find_duplicates(data):
    seen = set()
    for i in range(len(data)):
        if data[i] in seen :
            return True
        seen.add(data[i])
    return False



def isAnagram( s, t):

    if len(s) != len(t):
        return False
    stored = {}
    for i in s:
        letter_count =s.count(i)
        stored[i] = letter_count 
    for x in t:
        if t not in stored:
            return False
        if stored[t] != t.count(x):
            return False
    return True
t = "rat"    
s  = "car"
def is_Anagram(s,t):
    stored = {}    
    for i in t :
        if i in stored:
            stored[i] += 1
        else:
            stored[i] = 1
    stored2 = {}     
    for x in s:
        if x in stored2:
            stored2[x] += 1
        else:
            stored2[x] = 1
    if stored != stored2:
        return False
    return True


def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]
        if sum < target:
            left += 1
        else:
            right -= 1   


def isPalindrome(s= str) -> bool:
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    left = 0
    right = len(cleaned)-1
    while left < right:
        if cleaned[left] == cleaned[right]:
            left += 1
            right -= 1
        else:
            return False
    return True    

print(two_sum([1,2,3,4], 4))

def three_sum(nums):
    nums.sort()
    result = []
    for i in  range(len(nums)):
        target = -nums[i]
        left = i + 1
        right = len(nums)- 1
        if i > 0 and nums[i] == nums[i-1]:
            continuegit
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                result.append([nums[i],nums[left], nums[right]])
                left +=1
                right -= 1
                while nums[left] < nums[right] and nums[left] == nums[left -1]:
                    nums[left] += 1
    return result    



print(three_sum([-1, 0, 1, 2, -1, -1]))