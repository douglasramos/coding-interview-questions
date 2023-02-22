#  Time O(n) | Space O(1)
def getNthFib(n):
    a = 0
    b = 1

    if n == 1: return a
    if n == 2: return b

    fn = 0
    for _ in range(3, n+1):
        fn = a + b
        b, a = fn, b
        
    return fn

print(getNthFib(6))