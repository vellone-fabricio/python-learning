class Solution:

    @staticmethod
    def removeOuterParentheses(s: str) -> str:
        control_stack = []
        sequence = [[]]

        sequence_control = 0
        for item in s:
            sequence[sequence_control].append(item)
            if item == "(":
                control_stack.append(item)
            else:
                control_stack.pop()

            if len(control_stack) == 0:
                sequence_control += 1
                sequence.append([])

        output = []
        for seq in sequence:
            if len(seq) == 0:
                continue
            seq.pop()
            output.append("".join(seq[1:]))

        return "".join(output)


test_inputs = [
    "(()())(())",
    "(()()())",
    "()()",
    "(()())(())(()(()))"
]

for test_input in test_inputs:
    print(Solution.removeOuterParentheses(test_input))
