
inp_1 = "[{{([])}}]"
inp_2 = ")([({}){})"



def isBalanced(s):
    # pretend stack
    
    stack = []

    for i in range(len(s)):
        if s[i] in  ["(", "{", "["]:
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return "NO"
            else:
                pop_val = stack.pop()
                if pop_val == "(" and s[i] != ")":
                    return "NO"
                elif pop_val == "{" and s[i] != "}":
                    return "NO"
                elif pop_val == "[" and s[i] != "]":
                    return "NO"
    if not len(stack) == 0:
        return "NO"
    return "YES"

print(isBalanced(inp_1))
print(isBalanced(inp_2))