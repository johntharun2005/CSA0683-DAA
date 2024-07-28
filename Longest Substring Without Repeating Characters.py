def length_of_longest_substring(s):
    n = len(s)
    char_index = {}
    max_length = 0
    start = 0
    
    for i in range(n):
        if s[i] in char_index:
            start = max(start, char_index[s[i]] + 1)
        char_index[s[i]] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length
print(length_of_longest_substring("abcabcbb")) 
print(length_of_longest_substring("bbbbb")) 
