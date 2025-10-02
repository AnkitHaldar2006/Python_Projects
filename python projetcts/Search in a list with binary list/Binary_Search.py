def binary_search(arr, target):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = [34, 7, 23, 32, 5, 62]
target = int(input("Enter number to search: "))
result = binary_search(nums, target)
print("Found at index:" if result != -1 else "Not found", result)