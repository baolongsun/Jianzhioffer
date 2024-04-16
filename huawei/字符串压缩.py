def decodeString(s: str) -> str:
    stack, res, multi = [], "", 0
    for c in s:
        if c == '[':
            stack.append([multi, res])
            res, multi = "", 0
        elif c == ']':
            cur_multi, last_res = stack.pop()
            res = last_res + cur_multi * res
        elif '0' <= c <= '9':
            multi = multi * 10 + int(c)
        else:
            res += c
    return res

def decodeString2(s):
    stack,res,multi = [],"",0
    for c in s:
        if '0' <= c <= '9':
            multi = multi*10 + int(c)
        elif c == '[':
            stack.append([multi,res])
            res,multi = "",0
        elif c == ']':
            cur_multi,last_res = stack.pop()
            res = last_res + cur_multi*res
        else:
            res += c
    return res


print(decodeString2("13[a2[c]]"))
