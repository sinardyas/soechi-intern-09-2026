def check_brackets(string): 
    brackets = []
    open_brackets = ["[", "(", "{"]
    closed_brackets = ["]", ")", "}"]
    for char in string: 
        if char in open_brackets: 
            brackets.append(char)
        elif char in closed_brackets: 
            if len(brackets) > 0:                           #checks to see if there is atleast one opening bracket for a closed bracket encountered, else return False 
                if char == ")" and brackets [-1] == "(":    #compares the earliest close bracket found with the latest open bracket found in order to be logically correct 
                    brackets.remove(brackets[-1])
                elif char == "]" and brackets [-1] == "[": 
                    brackets.remove(brackets[-1])
                elif char == "}" and brackets [-1] == "{": 
                    brackets.remove(brackets[-1])
                else: 
                    return False                            #if a close bracket is found and the latest open bracket is not a matching pair, it is logically incorrect 
            else: 
                return False                                #if no open brackets are found and a close bracket is, it is logically incorrect 
    if len(brackets) == 0:                                  #if all open brackets have been correctly accounted for by matching closed brackets, remaining open brackets in the list to check should be zero 
        return True 
    else: 
        return False 

print(check_brackets("(a[b]{c})"))

"""
2 test cases: 

input: "{[()]}"
output: True

input: "{[(])}"
output: False


*QUESTION: 
what is the time and space complexity of your solution?*
Since my program searches through every character in the string in a linear pattern, its time complexity is O(n), in terms of space complexity, since the 'brackets' list can hold 'n' number of opening brackets, I would also say that it's space complexity is O(n).    

"""