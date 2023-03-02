def longestPalindromicSubstring(string: str) -> str:
    # putting '#' between each caracter so we convert even length to odd length
    # That way we can use one unique solution for both cases.
    # Note that putting this extra caracters don't change the palindromic property of a substring
    # we're also adding '^' and '$' to the begining and end of the file respectively so we can acess the left side and right side of the array (of characters)
    # without having the index out of range error. the idex (i) will work from 1 to n-2 so acessing s[i+1] or s[i-1] is ok
    # PS2.: we could implement tha logic without this. the tradeoff here is that 
    # in the code we would have to always check for i < len(s)-1 and if >= 1 to perform calculations on the edge of the array
    s = '#'.join('^{}$'.format(string))
    P = [0] * len(s)
    C, R = 0, 0

    for i in range(1, len(s)-1):
        if R > i:

            # R > i checks if the current position i is within the boundary of the rightmost palindrome found so far. 
            # If i is outside this boundary, we cannot use the symmetry property to make any assumptions about the length of the palindrome centered at i, 
            # and we need to start expanding the palindrome from scratch.

            # Finding the index x that is the mirror of i from center C: C - x = i - C -> x = 2C-i
            P[i] = min(R-i, P[2*C-i])
        
        # expand palindrome around the center

        while s[i+P[i]+1] == s[i-P[i]-1]:  
            P[i] += 1
        
        # update the pointers if necessary
        if i + P[i] > R:
            R = i + P[i]
            C = i
            
    maxLen, centerIndex = max((n,i) for i,n in enumerate(P))
    # we do //2 so we can   
    start = (centerIndex - maxLen) // 2
    end = start + maxLen -1
    return string[start:end+1]



print(longestPalindromicSubstring("abaxyzzyxf"))
# print(longestPalindromicSubstring("vixe"))
