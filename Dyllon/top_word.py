def top_words(text, n):
    import re
    from collections import Counter

    text = text.lower()
    text = re.sub(r'[.,!?;:]', '', text)

    words = text.split()

    word_counts = Counter(words)

    most_common = word_counts.most_common()
    most_common.sort(key=lambda x: (-x[1], x[0]))

    return most_common[:n]

# Test Case 1
print(top_words("The cat and the hat. The cat sat!", 2))
# Expected: [('the', 3), ('cat', 2)]

# Test Case 2
print(top_words("Apple apple banana, banana orange!", 2))
# Expected: [('apple', 2), ('banana', 2)]