f = open("Day4_input.txt")
f2 = open("Day4_output.txt","w")

full_line = ""
for line in f:
    if line.islower():
        full_line = full_line + line.rstrip() + " "
    else:
        #print(full_line)
        f2.write(full_line + "\n")
        full_line = ""
f2.write(full_line + "\n")

final = 0
f.close()
f2.close()

f2 = open("Day4_output.txt", "r")

for passport in f2:
    print(passport)
    
    failed = False
    if passport.find('byr:') == -1:
        failed = True
    if passport.find('iyr:') == -1:
        failed = True
    if passport.find('eyr:') == -1:
        failed = True
    if passport.find('hgt:') == -1:
        failed = True
    if passport.find('hcl:') == -1:
        failed = True
    if passport.find('ecl:') == -1:
        failed = True
    if passport.find('pid:') == -1:
        failed = True
        
    if not failed:
        print(passport)
        final += 1
    
print(final)
        
