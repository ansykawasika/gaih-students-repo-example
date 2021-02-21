def prime_first(x):
    if x < 500 and x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            print(f"prime_first -> {x}")
    
def prime_second(x):
    if x > 500:
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            print(f"prime_second -> {x}")

for x in range(1000):
    prime_first(x)
    prime_second(x)

