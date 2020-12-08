

file = open('./input.txt','r')
data = file.read()
input = data.splitlines()
file.close()

s = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

def part1(input):	
    valid =0
    for x in input:
        s = x.split(' ')
        least,most =[int(e) for e in s[0].split('-')]
        c = 0
        for i in s[2]:
            if i == s[1][0]:
                c+=1
        if least<=c<=most:
            valid+=1
    return valid	 

#part1(input)


def part2(input):
     valid =0 
     for n in input:
         print(n) 
         e = n.split(' ') 
         a,b =[int(i) for i in e[0].split('-')] 
         if e[2][a-1] ==e[1][0] and e[2][b-1] ==e[1][0]:  
             continue 
         elif e[2][a-1] ==e[1][0] or e[2][b-1] ==e[1][0]: 
            valid+=1 
            print('***VALID****')
         else: 
            continue 
                  
     return valid 



