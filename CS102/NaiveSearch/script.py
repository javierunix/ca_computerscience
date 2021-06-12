# At the top of the code editor, define a function called pattern_search. 
# Give pattern_search two parameters: text and pattern, and have it print both inputs.
# Below the initialized variables, text and pattern, 
# invoke pattern_search with these two variables passed in as arguments.

def pattern_search(text, pattern):
    #print("Input Text: %s. Input Patter: %s." %(text, pattern))
    for index in range(len(text)):
        #print("Text Index: %d" %index)
        match_count = 0
        
        for char in range(len(pattern)):
            #print("Pattern Index: %d" %char)

            if text[index + char] == pattern[char]:
                #print("Matching index found!")
                #print("Match Count: %d" %match_count)
                match_count += 1

            else:
                break
        
        if match_count == len(pattern):
            print(pattern, "found at index: ", index)



text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"

pattern_search(text, pattern)