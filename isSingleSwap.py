def isSingleSwap(s,t):

    if len(s) != len(t): return False

    mp = {}
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            if len(mp.keys()) > 0:
                if t[i] not in mp or mp[t[i]] != s[i]: 
                    return False
            else:
                mp[s[i]] = t[i]
                count += 1
    return count == 1


test_cases = [
    ('converse', 'conserve', True),
    ('iduhaiust', 'dfuirnaa', False)
]

for test_case in test_cases:
    if test_case[2]:
        assert(isSingleSwap(test_case[0], test_case[1]))
    else:
        assert(not isSingleSwap(test_case[0], test_case[1]))


assert(isSingleSwap('converse', 'conserve'))
assert(not isSingleSwap('foo', 'bar'))

###############
s = "converse"
t = "conserse"
s = 'foo'
t = 'bar'
print isSingleSwap(s,t)
