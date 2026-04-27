class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        #character in string
        for c in s:
        #means it is a closing parenthesis
            if c in closeToOpen:
        #check if it matches and if it does pop
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
            #because not matching
                    return False 
            else:
            #if it is open so we just append it and keep going
                stack.append(c)

        if not stack:
            return True
        else:
            return False