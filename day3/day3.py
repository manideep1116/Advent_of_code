
import numpy

file = open("./input.txt",'r')
data = file.read()
inp= data.splitlines()
file.close()

def find_trees(right,down):
    col =0
    trees=0
    for i in range(0,len(inp)-1,down):
        col+=right
        if inp[i+down][col % len(inp[i+down])]=='#':
                trees+=1
    return trees


def multi(func_list):
    result = numpy.prod(func_list)
    return result


total_trees =[find_trees(1,1),find_trees(3,1),find_trees(5,1),find_trees(7,1), find_trees(1,2)]

print(multi(total_trees))

