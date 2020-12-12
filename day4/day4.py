with open("input.txt",'r') as f:
    lines = f.read()
    data  = lines.splitlines()
valid_values=["ecl","pid","eyr","hcl","byr","iyr","hgt"]



def valid_passport(pass_details):
    for i in valid_values:
        if i not in pass_details:
            return False
    return True



def passport():
    details = ''
    valid = 0
    for i in data:
        if i!='':
            details+=i+' '
        else:
            if valid_passport(details):
               valid+=1
            details =''
    if valid_passport(details):
        valid+=1
    return valid
    
print(passport())
