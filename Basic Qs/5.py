# Check if a large number is divisible by 6 or not
# Given a number, the task is to check if a number is divisible by 6 or not.
# The input number may be large and it may not be possible to store even if we use long long int.

# Examples: 
# Input  : n = 2112
# Output: Yes
# Input : n = 1124
# Output : No
# Input  : n = 363588395960667043875487
# Output : No

def divisble(a):

    if a%6==0:
         print("the number is divisble by 6")
    else:
        print('the number is not divisble by 6')

print(divisble(2112))