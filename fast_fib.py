n = int(input("How high do you want the Fibonacci sequence to go? Enter a number: "))

cache = {}
def fastFib(n,count=0):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fastFib(n-1) + fastFib(n-2)
        
        print(cache[n])
    return cache[n]


print("Your final, freaky-fast Fibonacci number at", n, "is", fastFib(n), "wooow!")