'''
problem:

string includes '1' '2' and "?" replace ? with 1 or 2
'''

def genStr(s):
    # arg1: str
    # ret: list[str]

    def recgenStr(s,start,res,result):
        if start == len(s):
            result.append(res[:])
            return

        if s[start] == '?':
            recgenStr(s, start+1,res+'1',result)
            recgenStr(s, start+1,res+'2',result)
        else:
            recgenStr(s, start+1,res+s[start],result)

        return


    def itrgenStr(s, result):
        for i in range(len(s)):
            newresult = []
            for item in result:
                if s[i] == "?":
                    newresult.append(item+"1")
                    newresult.append(item+"2")
                else:
                    newresult.append(item+s[i])
            result = newresult
        return result



    result = ['']
    #recgenStr(s,0,'',result)
    #return result
    return itrgenStr(s,result)
    



test = "?"
print genStr(test)

