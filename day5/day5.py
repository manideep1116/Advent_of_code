with open("input.txt",'r') as f:
    data = f.read().splitlines()
id = []


def rows(number):
    a =0
    b =127
    for i in number[0:6]:
        half = (a+b)//2
        if i[0]=="F":
            b = half
        elif i[0]=="B":
            a = half+1
    if number[6]=="F":
        return a
    if number[6]=="B":
        return b

def coloumns(number):
    a=0
    b=7
    for i in number[7:9]:
        half = a+b//2
        if i =="R":
            a =half+1
        elif i =="L":
            b = half
    if number[9]=="R":
        return b
    else:
        return a


for i in data:
    r= rows(i)
    c= coloumns(i)
    id.append((r*8)+c)


print(max(id))


#-------part-2-------

def my_seat():
    for seat in range(896):
        if (seat-1 in id) and (seat+1 in id) and (seat not in id):
             return seat
print(my_seat())    
