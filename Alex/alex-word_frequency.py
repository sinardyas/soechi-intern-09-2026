def top_words(text, n):
	text = text.lower()

	for punctuation in ".,!?:;":
		text = text.replace(punctuation, " ")

	words = text.split()
	counts = {}

	for word in words:
		if word not in counts:
			counts[word] = 0
		counts[word] += 1

	sorted_words = sorted(counts, key=lambda word: (-counts[word], word))

	return [(word, counts[word]) for word in sorted_words[:n]]

# Test Cases
print(top_words("The cat and the hat. The cat sat!", 2)) 
# Expected: [('the', 3), ('cat', 2)]

print(top_words("Apple apple banana banana orange", 2)) 
# Expected: [('apple', 2), ('banana', 2)]