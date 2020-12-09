file = open('./input.txt','r')
data = file.read()
inp = [int(i) for i in data.splitlines()]
file.close()

def find_two_entries(inp):
    for c1,e1 in enumerate(inp):  
        for c2 in inp[c1+1:]:
            if inp[c1]+c2 ==2020:
                return(inp[c1],c2,inp[c1]*c2)


def find_three_entries(inp):
    for c1,e1 in enumerate(inp):
        for c2 in inp[c1+1:]:
            for c3 in inp[c1+2:]:
                if inp[c1]+c2+c3 ==2020:
                    return(inp[c1],c2,c3,inp[c1]+c2+c3,inp[c1]*c2*c3)

print(find_two_entries(inp)) 
print(find_three_entries(inp))
