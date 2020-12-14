import re
with open("input.txt",'r') as f:
    lines = f.read()
    data  = lines.splitlines()
valid_values=["ecl","pid","eyr","hcl","byr","iyr","hgt"]
valid_passports = []


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
               valid_passports.append(details)
               valid+=1
            details =''
    if valid_passport(details):
        valid_passports.append(details)
        valid+=1
    return valid
print("valid passports",valid_passports)
print("passports valid part1:",passport())

#---------part-2-----
def passport_details():
    details = ''
    valid = 0
    print(valid_passports)
    for i in valid_passports:
        if validate_details(i):
            valid+=1
    return valid

def valid_passport_details(pass_details):
    '''
    validate if all the fields have present and pass on to validate the content ot fields
    '''
    for i in valid_values:
        if i not in pass_details:
            return False
    return validate_details(pass_details)
        

def validate_details(pd):
    '''
    validate the content of fields
    '''
    for j in pd.split(' '):
        if j[:3] =='hcl':
             hcl = validate_hcl(j[4:])
             if hcl == False:
                 return False
        if j[:3]=="byr":
            byr= validate_byr(j[4:])
            if byr == False:
                return False
        if j[:3]=="iyr":
            iyr= validate_iyr(j[4:])
            if iyr == False:
                return False
        if j[:3]=="eyr":
            eyr= validate_eyr(j[4:])
            if eyr == False:
                return False
        if j[:3]=="hgt":
            hgt= validate_hgt(j[4:])
            if hgt == False:
               return False

        if j[:3]=="ecl":
            ecl= validate_ecl(j[4:])
            if ecl == False:
               return False

        if j[:3]=="pid":
            pid= validate_pid(j[4:])
            if pid == False:
                return False
    return True

def validate_byr(byr):
    return (1920<=int(byr)<=2002)

def validate_iyr(iyr):
    return (2010<=int(iyr)<=2020)

def validate_hcl(hcl):
    return bool(re.search("^#.*[0-9a-f]", hcl))    

def validate_eyr(eyr):
    return (2020<=int(eyr)<=2030)

def validate_hgt(hgt):
    if hgt[-2:] =='cm':
        return (150<=int(hgt[:-2])<=193)
    if hgt[-2:] =='in':
        return (59<=int(hgt[:-2])<=76)

def validate_ecl(ecl):
    return bool(re.search('[abgho][mlrzt][buynlh]',ecl))

def validate_pid(pid):
    return bool(re.search('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',pid))




print(passport_details())


