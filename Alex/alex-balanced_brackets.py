def is_balanced(text):
	open_brackets = "([{"
	close_brackets = ")]}"
	matching_brackets = {
		")": "(",
		"]": "[",
		"}": "{"
	}
	stack = []

	for character in text:
		if character in open_brackets:
			stack.append(character)
		elif character in close_brackets:
			if not stack or stack.pop() != matching_brackets[character]:
				return False

	return len(stack) == 0

# Test Cases
print(is_balanced("(a[b]{c})")) # Expected: True
print(is_balanced("([)]"))      # Expected: False

# Complexity Answer:
# Time Complexity: O(n) because we iterate through the string once.
# Space Complexity: O(n) in the worst-case scenario (e.g., all open brackets "(((").