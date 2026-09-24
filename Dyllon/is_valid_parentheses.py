def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)

    return not stack
# Test Case 1
print(is_valid_parentheses("(a[b]{c})"))
# Expected: True

# Test Case 2
print(is_valid_parentheses("([)]"))
# Expected: False