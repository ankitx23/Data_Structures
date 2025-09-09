# Program to count vowels in a string (Iterative and Recursive)
# Given a string, count the total number of vowels (a, e, i, o, u) in it. 
# There are two methods to count total number of vowels in a string.
# Iterative 
# Recursive
# Examples: 

# Input : abc de
# Output : 2

# Input : geeksforgeeks portal
# Output : 7

# iterative

def countvowels(x):
    vowels = "AEIOUaeiuo"
    count = 0
    for ch in x:
        if ch in vowels:
            count+=1
    return count


print(countvowels("abc de"))

