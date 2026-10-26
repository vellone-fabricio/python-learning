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
    

    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, item in enumerate(nums):
            complement = target - item
            if complement in seen:
                return [seen[complement], index]
            seen[item] = index

# ----------------------------------------------------------------------------
# Exercise to remove the outer parentheses
test_inputs = [
    "(()())(())",
    "(()()())",
    "()()",
    "(()())(())(()(()))"
]

for test_input in test_inputs:
    print(Solution.removeOuterParentheses(test_input))

print("--------------------------------")

# ----------------------------------------------------------------------------
# Exercise to find the two sum
test_inputs = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([0,4,3,0], 0),
    ([-3,4,3,90], 0),
]

for test_input in test_inputs:
    print(Solution.twoSum(test_input[0], test_input[1]))

print("--------------------------------")
