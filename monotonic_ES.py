# Kiểm tra dãy cho trước có đơn điệu không

def increasing(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr)-1))
def decreasing(arr):        
    return all(arr[i] >= arr[i + 1] for i in range(len(arr)-1))
def monotonic(arr):    
    return increasing(arr) or decreasing(arr)

# Test the function
arr1 = [1, 2, 2, 3]  # Monotonic (non-decreasing)
arr2 = [3, 2, 1]     # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4]  # Not monotonic
print("arr1 is monotonic:", monotonic(arr1))
print("arr2 is monotonic:", monotonic(arr2))
print("arr3 is monotonic:", monotonic(arr3))