from itertools import combinations

def solution(l):
    # containers
    msg        = []
    divergents = []
    
    # Separating numbers that can/can't be divided by 3
    for digit in l:
        if digit % 3 == 0:
            msg.append(digit)
        else:
            divergents.append(digit)
    
    # Iterating in reverse order to get bigger numbers first
    for size in xrange(len(divergents), 0, -1):
        # Iterating over combinations of the current size
        # combinations() returns lexographically biggest combination
        for com in combinations(sorted(divergents, reverse=True), size):
            # If our combination is divisible with 3; return
            if sum(com) % 3 == 0:
                msg.extend(list(com))
                return ''.join(map(str, sorted(msg, reverse=True)))

    # If there are numbers in msg array and non of the 
    # combinations are divisible with 3
    if any(msg):            
        return ''.join(map(str, sorted(msg, reverse=True)))
    else:
        return 0
        
