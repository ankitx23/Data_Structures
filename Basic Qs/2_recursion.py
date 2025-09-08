# Given an array, the task is to find average of that array. 
# Average is the sum of array elements divided by the number of elements.

# Examples : 

# Input : arr[] = {1, 2, 3, 4, 5}
# Output : 3
# Sum of the elements is 1+2+3+4+5 = 15 
# and total number of elements is 5.
# So average is 15/5 = 3

# Input : arr[] = {5, 3, 6, 7, 5, 3}
# Output : 4.83333
# Sum of the elements is 5+3+6+7+5+3 = 29
# and total number of elements is 6.
# So average is 29/6 = 4.83333.

def find_sum(arr, n):
    if n==0:
        return 0
    return find_sum(arr, n-1) + arr[n-1]

def find_average(arr):
    n = len(arr)
    total_sum = find_sum(arr, n)
    return total_sum / n if n != 0 else 0

arr=[1, 2, 3, 4, 5]
n= len(arr)
print(" ",find_average(arr))
