def isValid(s: str) -> bool:
    pairings = {'(':')', '{':'}', '[':']'}
    stack = []       
    for char in s:
        if char in pairings.keys():
            stack.append(char)
        else:
            if len(stack) == 0 :
                return False
            top = stack[-1]
            top_pairing = pairings[top]
            if char != top_pairing:
                return False
            stack.pop()
    return len(stack)== 0 
        
s = "([{}])"
s = "[(])"

print(isValid(s))