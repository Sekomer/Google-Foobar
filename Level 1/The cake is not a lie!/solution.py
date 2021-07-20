def solution(s):
    # reducing repetitive function calls    
    s_len = len(s)
    
    # If the string is shorter than 2 chars, it can't be shared
    if s_len < 2:
        return 1
    
    # substring size values greater than half of the s_len are redundant.
    for substr_size in xrange(1, (s_len / 2) + 1):
        # Commander Lambda hates waste 
        # and will not tolerate any leftovers!
        if s_len % substr_size == 0:
            num_sub = s_len / substr_size

            for j in xrange(num_sub - 1):
                c_sub = s[(substr_size) * (j)   : (substr_size) * (j+1)]
                n_sub = s[(substr_size) * (j+1) : (substr_size) * (j+2)]

                # If substrings are not equal, break the loop
                if c_sub != n_sub:
                    break
            
            # The else clause executes after the loop completes normally.
            # This means that the for didn't encounter a break statement.
            else: 
                return num_sub

    # no slices, default case => 1
    return 1