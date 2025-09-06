# Count Odd and Even
# You are given an array arr[]. Your task is to count the number of even and odd elements. 
# Return first odd count then even count.

# Examples: 
# Input: arr = [2, 3, 4, 5, 6]
# Output: 2 3 
# Explanation: There are two odds[3, 5] and three even[2, 4, 6] present in the array.

# Input: arr = [22, 32, 42, 52, 62]
# Output: 0 5
# Explanation: All the elements are even.

def countoddeven(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num%2==0:
             even_count+=1
        else:
            odd_count+=1

    print(odd_count, even_count)

arr= [2,3,4,5,6,7]
countoddeven(arr)