def fizzbuzz(n):
    if n%3==0 and n%5==0:
        print("fizzbuzz")
    elif n%5==0:
        print("buzz")
    elif n%3==0:
        print("fizz")
    return None

print (fizzbuzz(17))
