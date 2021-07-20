from fractions import gcd

def solution(x, y):
    x, y = int(x), int(y)
    
    # base case
    if x == y == 1:
        return "1"
    
    # erroneous inputs
    if x < 1 or y < 1:
        return "impossible"
    if gcd(x, y) != 1:
        return "impossible"
    
    big = max(x, y)
    small = min(x, y)
    counter = 0
    
    # for optimization I used divmod function
    # at some point one of the numbers end up being 1
    # divmod(n, 1) returns n, we need n-1 
    # therefore at the end we need to subtract 1 from counter
    while big != 0 and small != 0:
        div, mod = divmod(big, small)
        big = mod
        counter += div
        
        if big < small:
            big, small = small, big
    
    return str(counter - 1)