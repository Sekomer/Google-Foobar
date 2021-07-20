# this function changes base of a number 
# returns string
def changebase(decimal, base):
    new_number = 0
    counter    = 0

    while decimal != 0:
        decimal, mod = divmod(decimal, base)

        new_number += mod * (10**counter)
        counter    += 1

    return str(new_number)


# this function creates a new id from given string and base
# returns string
def calculate(number, base):
    # descending and ascending
    # Used reversed to avoid twice sort cost => O(n.log(n))
    y = ''.join(sorted(str(number)))
    x = ''.join(reversed(y))
    
    z = int(x, base) - int(y, base) # base change for subtraction operation
    new_id = changebase(z, base).zfill(len(number)) # filling empty parts of the string    

    return new_id


def solution(n, b):
    array = []

    # iterate until there is a cycle
    while n not in array:
        array.append(n)
        n = calculate(n, b)

    return len(array) - array.index(n)
