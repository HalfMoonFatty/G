'''
Problem:

Given a word and a dictionary, can remove any number of chars in the string to become a string t. 

Return if t is in the dictionary.

'''
def fuzzystr(s):
	d = set(['h','hel'])
	def rec(s,start,res,result):
		cur = ''.join(res)
		if cur in d:
			result.append(cur)

		for i in range(start,len(s)):
			if i > 1 and s[i] == s[i-1]:
				continue
			res.append(s[i])
			rec(s,i+1,res,result)
			res.pop()
		
		return

	result = []
	rec(s,0,[],result)
	return result


test = 'hello'
print fuzzystr(test)
