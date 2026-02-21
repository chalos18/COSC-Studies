def encode(strs: list[str]) -> str:
    new_word = ''
    for word in strs:
        new_word += str(len(word)) + '#' + word
    return new_word


def decode(s: str) -> list[str]:
    res, i = [], 0
    
    # read char by char decoding each string
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        # how many following chars we have to read after j in order to get every char of the string
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res
    
    
def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s: str) -> list[str]:
    res, i = [], 0
    
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        s_length = int(s[i:j])
        word = s[j + 1: s_length + j + 1]
        i = j + s_length + 1
        
        res.append(word)
        
    return res
            
        



dummy_input=["Hello","World"]

result = encode(dummy_input)

decoded = decode(result)

print(result)
print(decoded)