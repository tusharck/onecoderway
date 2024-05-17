array = [2,11,7,15]
target = 9
# ans = (0,2)

def twoSum(nums, target):
        hash_map = {}

        for i in range(len(nums)):
            x = target - nums[i]
            
            if x in hash_map:
                return hash_map[x], i
                
            hash_map[nums[i]] = i

print(twoSum(array, target))