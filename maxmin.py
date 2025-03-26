def maxMinSelect(array, left, right):

    if left == right:
        return array[left], array[left]
    
    if right - left == 1:
        if array[left] < array[right]:
            return array[left], array[right]
        else:
            return array[right], array[left]
        
    mid = (left + right) // 2
    min_left, max_left = maxMinSelect(array, left, mid)
    min_right, max_right = maxMinSelect(array, mid + 1, right)
    
    overall_min = min(min_left, min_right)
    overall_max = max(max_left, max_right)
    
    return overall_min, overall_max
    
arr = [5, 4, 10, 15, 98, 30, 2]
min_val, max_val = maxMinSelect(arr, 0, len(arr) - 1)
print(min_val)
print(max_val)