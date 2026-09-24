def top_words(text,n): 
    freq = {}
    prohibited_chars = [".", ",", "!", "?", ";", ":"] 
    text = text.lower()                                             #turning every character into lowercase so case sensitIvity is not a problem
    cleaned_text = ""                                               #cleaned_text will hold the text without any punctuation marks 
    for char in text: 
        if char not in prohibited_chars:                            #checking to see if original text contains any punctuation 
            cleaned_text += char     
        else: 
            continue 
    new_text = cleaned_text.strip().split()                         #making sure the new formatted text does not have trailing spaces and every word seperated by a space is turned into a list

    single_words = []                                               #single_words list will hold each unique word in the text only once
    for word in new_text: 
        if word not in single_words: 
            single_words.append(word)
    for word in single_words:                                       #looping through each unique word to assign it a value of it's frequency in a dictionary 
        freq[word] = new_text.count(word)

    items = list(freq.items())                                      #turning each key-value pair into a tuple and storing all the tuples in a list 
    result = [] 
    while len(items) > 0:                                           #this loop is used to sort through each tuple in the list 'items' and sort it by frequency one by one from highest to lowest  
        highest = items[0]  
        for item in items: 
            if item[1] > highest [1]: 
                highest = item 
            elif item [1] == highest [1] and item[0] < highest[0]:  #making sure that we sort alphabetically aswell if frequency is same between 2 words 
                highest = item 
            else: 
                continue 
        result.append(highest)                                      
        items.remove(highest)                                      #removing (word, frequency) tuple from list 'items' to sort through remaining tuples and decide which will be ranked higher from those

    return result[:n]                                               #since the frequencies are sorted highest to lowest, we use slicing to get the exact number of words and the amount highest respective frequencies that the user wants from the string given 

text = "The cat and the hat. The cat sat!"
print(top_words(text, 2))



"""
2 other uses cases: 

input: "Apple, banana apple? orange banana! apple."
expected_output: [("apple", 3), ("banana", 2)]

input: "dog cat bird dog cat bird"
expected_output: [("bird", 2), ("cat", 2), ("dog", 2)]

"""