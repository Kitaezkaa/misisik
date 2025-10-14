def min_max(nums):
    if len(nums) == 0:
        raise ValueError("Список пуст")
    
    min_val = nums[0]
    max_val = nums[0]
    
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return (min_val, max_val)
def unique_sorted(nums):
    unique_nums = []
    
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    
    unique_nums.sort()
    return unique_nums
def flatten(mat):
    result = []
    
    for item in mat:
        if not isinstance(item, list) and not isinstance(item, tuple):
            raise TypeError("Элемент не является списком или кортежем")
        
        for element in item:
            result.append(element)
    
    return result