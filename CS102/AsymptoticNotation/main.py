def this_function(number):
    i = 1
    while i != number:
        print(i)
        i+= 1
    
    count = 0
    while number != 1:
        count += 1
        number = number // 2
    
    return count

print(this_function(8))