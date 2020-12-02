counter = 0

f = open("day2_input.txt")

def parse_line(line):
    line = line[:-1]
    return line.split(": ")

def testCharacters(input, character, top_limit, bottom_limit):
    result = {}
    for keys in input:
        result[keys] = result.get(keys, 0) + 1
    try:
        number_of_chars = result[character]
    except:
        number_of_chars = 0
    if number_of_chars >= int(bottom_limit) and number_of_chars <= int(top_limit):
        return True
    else:
        return False

for x in f:
    result = parse_line(x)
    frequency = result[0].split(" ")
    character = frequency[1]
    limits = frequency[0].split("-")
    top_limit = limits[1]
    bottom_limit = limits[0]
    password = result[1]
    
    final = testCharacters(password, character, top_limit, bottom_limit)
    print(final)
    if final is True:
        counter = counter + 1
print(counter)
