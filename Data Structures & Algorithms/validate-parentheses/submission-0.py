class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"}":"{", ")":"(", "]":"["}
        opening = ["{", "[", "("]

        for char in s:
            if char in opening:
                stack.append(char)
            elif stack and stack[-1] == matches[char]:
                stack.pop()
            else:
                return False
        
        return stack == []

        