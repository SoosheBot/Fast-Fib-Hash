n = int(input("How high do you want the Fibonacci sequence to go? Enter a number: "))

def recurse_fibonacci(n):
    if n <= 1:
        return n
    else:
        total = recurse_fibonacci(n-1) + recurse_fibonacci(n-2)
        print(total)
        return(total)

# complexity 2^n -- soooo slow
print("Your sad, slow Fibonacci total at",n, "is", recurse_fibonacci(n), "booooo!")