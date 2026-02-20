#can be used to find things in the code....

input_string = "swiss miss"

def find_first_unique_char(text):
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in text:
        if char_count[char] == 1:
            return char
            
    return None

print(find_first_unique_char(input_string))
