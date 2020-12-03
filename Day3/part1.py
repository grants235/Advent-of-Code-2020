tree_counter = 0
digit_counter = 0

f = open("Day3_input.txt", "r")

for line in f:
    list_of_chars = []
    list_of_chars[:0]=line
    #print(list_of_chars[digit_counter])

    if list_of_chars[digit_counter] == "#":
        tree_counter = tree_counter + 1
    
    if digit_counter == 28:
        digit_counter = 0 
    elif digit_counter == 29:
        digit_counter = 1
    elif digit_counter == 30:
        digit_counter = 2
    else:
        digit_counter = digit_counter + 3

print(tree_counter)
