class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        print(folders)

        stack = []

        for folder in folders:
            if folder == '' or folder == '.':
                continue
            if not stack and folder == "..":
                continue

            
            if stack and folder == "..":
                stack.pop()
                continue
            
            stack.append(folder)
        
        return "/" + "/".join(stack)
        