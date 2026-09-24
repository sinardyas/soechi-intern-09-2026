def split_input(Input):
    words = Input.split()
    result = ""

    for i in range(len(words) - 1, -1, -1):
        result += words[i]

        if i != 0:
            result += " "

    return result

# Test Case 1
print(split_input("  the ship   sails at dawn "))
# Expected: dawn at sails ship the

# Test Case 2
print(split_input("hello world"))
# Expected: world hello