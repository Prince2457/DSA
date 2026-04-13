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
    for x in s:
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
print(is_Anagram(s,t))          

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




