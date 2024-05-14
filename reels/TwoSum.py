# array = [2,7,11,15]
# target = 9
# ans = (0,1)

def twoSum(nums, target):
        hash_map = {}

        for i in range(len(nums)):
            x = target - nums[i]
            
            if x in hash_map:
                return i, hash_map[x]
                
            hash_map[nums[i]] = i


l = [2,7,11,15]
target = 9

print(twoSum(l, target))