class Solution:
    def multiply(self, s:str, n:int) -> str:
        res = ""
        for i in range(n):
            res += s
        return res
    def decodeString(self, s: str) -> str:

        stack = []
       
        for c in s:
            if c == ']':
                curr = ""
                while stack[-1] != '[':
                    print(stack)
                    curr = stack.pop() + curr
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    print(stack)
                    k = stack.pop() + k
                
                result = self.multiply(curr, int(k))

                stack.append(result)
            else:
                stack.append(c)
        return "".join(stack)
                

                    



        
        