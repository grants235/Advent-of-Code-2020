counter = 0

f = open("day2_input.txt")

def parse_line(line):
    line = line[:-1]
    return line.split(": ")

def check_posititons(input, occurance1, occurance2, character):
    list_of_chars = []
    list_of_chars[:0]=input
    try:
        if list_of_chars[int(occurance1) - 1] == character and list_of_chars[int(occurance2) - 1] != character:
            return True
        elif list_of_chars[int(occurance1) - 1] != character and list_of_chars[int(occurance2) - 1] == character:
            return True
        else:
            return False
    except:
        return False

for x in f:
    result = parse_line(x)
    frequency = result[0].split(" ")
    character = frequency[1]
    limits = frequency[0].split("-")
    occurance1 = limits[1]
    occurance2 = limits[0]
    password = result[1]
    
    final = check_posititons(password, occurance1, occurance2, character)
    
    print(final)
    if final is True:
        counter = counter + 1
print(counter)
