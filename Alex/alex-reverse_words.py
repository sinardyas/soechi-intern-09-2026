# Alex - Internship Assessment - 4.1

def f(text):
    words = []
    current_word = "" 

    for char in text:
        if char != " ":
            current_word += char
        else:
            if current_word != "":
                words.append(current_word)
                current_word = ""  

    if current_word != "":
        words.append(current_word)
    
    result = ""
    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if i > 0:
            result += " "


    end_idx = len(result) - 1
    while end_idx >= 0 and result[end_idx] == " ":
        end_idx -= 1

    start_idx = 0
    while start_idx <= end_idx and result[start_idx] == " ":
        start_idx += 1

    cleaned_result = ""
    in_space = False

    for idx in range(start_idx, end_idx + 1):
        char = result[idx]
        if char == " ":
            if not in_space:
                cleaned_result += " "
                in_space = True
        else:
            cleaned_result += char
            in_space = False

    return cleaned_result

# Test Cases
print(repr(f("  the ship   sails at dawn "))) # 'dawn at sails ship the'
print(repr(f("hello   world")))              # 'world hello'