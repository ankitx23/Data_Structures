# Given a number N, the task is to convert every digit of the number into words.
# Examples: 
# Input: N = 1234 
# Output: One Two Three Four 
# Explanation: 
# Every digit of the given number has been converted into its corresponding word.

def printValue(digit):

    if digit == 0:
        print("ZERO",end =" ")
    elif digit == 1:
        print ("ONE",end =" ")
    elif digit == 2:
        print("Two",end =" ")
    elif digit == 3:
        print("Three",end =" ")
    elif digit == 4:
        print("Four",end =" ")
    elif digit == 5:
        print("Five",end =" ")
    elif digit == 6:
        print("Six",end =" ")
    elif digit == 7:
        print("Seven",end =" ")
    elif digit == 8:
        print("Eight",end =" ")
    elif digit == 9:
        print("Nine",end =" ")

def printWord(N):
    i= 0
    length = len(N)
    while i < length:
        printValue(N[i])
        i+=1

N="456"
printWord(N)