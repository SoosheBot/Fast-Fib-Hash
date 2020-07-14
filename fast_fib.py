n = int(input("fibonacci count: "))

cache = {}
def hash_fibonacci(n,count=0):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = hash_fibonacci(n-1) + hash_fibonacci(n-2)
        
        print(cache[n])
    return cache[n]


print("Your final, freaky-fast Fibonacci number is", hash_fibonacci(n), "wooow!")