class Solution:
    def isValid(self, s: str) -> bool:
        brackets=[]
        l=list(s)
        for b in l:
            if b in {"(", "[", "{"}:
                brackets.append(b)
            elif len(brackets) > 0:
                if brackets[-1] == "(" and b == ")":
                    brackets.pop()
                elif brackets[-1] == "[" and b == "]":
                    brackets.pop()  
                elif brackets[-1] == "{" and b == "}":
                    brackets.pop()
                else:
                    return False
            else: 
                return False
        return len(brackets) == 0
s=Solution()
a=s.isValid("()()()[{}}]")
print(a)