# Check if given number is perfect square

# Given a number n, check if it is a perfect square or not. 

# Examples : 

# Input  : n = 36
# Output : Yes

# Input : n = 2500
# Output : Yes
# Explanation: 2500 is a perfect square of 50

# Input  : n = 8
# Output : No

n=int(input("Enter a number: "))

root = int (n**0.5)

if root*root==n:
    print(f"the number {n} is square of: ",root)
else:
    print("it is not").
