f = open("Day3_input.txt", "r")

#Code for right 1, down 1
tree_counter_1_1 = 0
digit_counter_1_1 = 0
for line in f:
    list_of_chars = []
    list_of_chars[:0] = line
    #print(list_of_chars[digit_counter_1_1])

    if list_of_chars[digit_counter_1_1] == "#":
        tree_counter_1_1 = tree_counter_1_1 + 1
    
    if digit_counter_1_1 == 30:
        digit_counter_1_1 = 0
    else:
        digit_counter_1_1 = digit_counter_1_1 + 1

print(tree_counter_1_1)
f.close()


#Code for right 3, down 1
f = open("Day3_input.txt", "r")
tree_counter_1_3 = 0
digit_counter_1_3 = 0
for line in f:
    list_of_chars = []
    list_of_chars[:0] = line
    #print(list_of_chars[digit_counter_1_3])

    if list_of_chars[digit_counter_1_3] == "#":
        tree_counter_1_3 = tree_counter_1_3 + 1
    
    if digit_counter_1_3 == 30:
        digit_counter_1_3 = 2
    elif digit_counter_1_3 == 29:
        digit_counter_1_3 = 1
    elif digit_counter_1_3 == 28:
        digit_counter_1_3 = 0
    else:
        digit_counter_1_3 = digit_counter_1_3 + 3

print(tree_counter_1_3)
f.close()


#Code for right 5 , down 1
f = open("Day3_input.txt", "r")
tree_counter_1_5 = 0
digit_counter_1_5 = 0
for line in f:
    list_of_chars = []
    list_of_chars[:0] = line
    #print(list_of_chars[digit_counter_1_5])

    if list_of_chars[digit_counter_1_5] == "#":
        tree_counter_1_5 = tree_counter_1_5 + 1
    
    if digit_counter_1_5 == 30:
        digit_counter_1_5 = 4
    elif digit_counter_1_5 == 29:
        digit_counter_1_5 = 3
    elif digit_counter_1_5 == 28:
        digit_counter_1_5 = 2
    elif digit_counter_1_5 == 27:
        digit_counter_1_5 = 1
    elif digit_counter_1_5 == 26:
        digit_counter_1_5 = 0
    else:
        digit_counter_1_5 = digit_counter_1_5 + 5

print(tree_counter_1_5)
f.close()


#Code for right 7, down 1
f = open("Day3_input.txt", "r")
tree_counter_1_7 = 0
digit_counter_1_7 = 0
for line in f:
    list_of_chars = []
    list_of_chars[:0] = line
    #print(list_of_chars[digit_counter_1_7])

    if list_of_chars[digit_counter_1_7] == "#":
        tree_counter_1_7 = tree_counter_1_7 + 1
    
    if digit_counter_1_7 == 30:
        digit_counter_1_7 = 6
    elif digit_counter_1_7 == 29:
        digit_counter_1_7 = 5
    elif digit_counter_1_7 == 28:
        digit_counter_1_7 = 4
    elif digit_counter_1_7 == 27:
        digit_counter_1_7 = 3
    elif digit_counter_1_7 == 26:
        digit_counter_1_7 = 2
    elif digit_counter_1_7 == 25:
        digit_counter_1_7 = 1
    elif digit_counter_1_7 == 24:
        digit_counter_1_7 = 0
    else:
        digit_counter_1_7 = digit_counter_1_7 + 7

print(digit_counter_1_7)
f.close()

#Code for right 1, down 2
f = open("Day3_input.txt", "r")
tree_counter_2_1 = 0
digit_counter_2_1 = 0
row_counter_1_2 = 1
for line in f:
    if row_counter_1_2 == 1:
        list_of_chars = []
        list_of_chars[:0] = line
        #print(list_of_chars[digit_counter_2_1])

        if list_of_chars[digit_counter_2_1] == "#":
            tree_counter_2_1 = tree_counter_2_1 + 1
        
        if digit_counter_2_1 == 30:
            digit_counter_2_1 = 0
        else:
            digit_counter_2_1 = digit_counter_2_1 + 1
        
        row_counter_1_2 = 0
    else:
        row_counter_1_2 = 1

print(tree_counter_2_1)
f.close()

result  = tree_counter_1_1 * tree_counter_1_3 * tree_counter_1_5 * tree_counter_1_7 * tree_counter_2_1
print("Answer = " + str(result))
