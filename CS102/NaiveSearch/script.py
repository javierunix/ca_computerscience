# At the top of the code editor, define a function called pattern_search. 
# Give pattern_search two parameters: text and pattern, and have it print both inputs.
# Below the initialized variables, text and pattern, 
# invoke pattern_search with these two variables passed in as arguments.

def pattern_search(text, pattern, replacement, case_sensitive = True):
    fixed_text = ""
    num_skips = 0
    counter = 0
    if case_sensitive == False:
        text = text.lower()
        pattern = pattern.lower()

    for index in range(len(text)):
        counter += 1
        if num_skips > 0:
            num_skips -= 1
            continue
        match_count = 0
        
        for char in range(len(pattern)):
            counter += 1
            if text[index + char] == pattern[char]:
                match_count += 1
            else:
                break
        
        if match_count == len(pattern):
            fixed_text += replacement
            num_skips = len(pattern) - 1
        else:
            fixed_text += text[index]
    print(counter)
    return(fixed_text)



text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "needle"

print(pattern_search(text, pattern, "chains", False))