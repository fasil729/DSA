class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token in operators:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                exp = operand_2 + token + operand_1
                val = int(float(eval(exp)))
                stack.append(str(val))
            else:
                stack.append(token)
            
        
        return int(float(stack[0]))
        