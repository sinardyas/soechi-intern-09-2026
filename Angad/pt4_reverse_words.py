def reverse(word): 
    word = word.split()         #converting word into element wherever seperated by any amount of spaces 
    new_word = ""
    for i in range((len(word)-1), -1, -1):  #referencing each word in reverse order 
        new_word += word[i] + " "     #re-writing the word to ensure that there is only one space between words 
    new_word = new_word.strip() #removing and trailing or leading spaces from final word 
    return new_word

print(reverse("  the ship   sails at dawn "))


"""
2 test cases: 

input: " hello all  this      is  my test  "
expected output: "test my is this all hello"

input = " char actor   sun      set       "
expected output: "set sun actor char"

"""


