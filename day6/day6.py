with open("input.txt",'r') as f:
    data=f.read().splitlines()
    
print(data)

def count_unq():
    count =0
    answer =''
    for i in data:
        if i!='':
            answer+=i
        else:
            unique=set(answer)
            count+=len(unique)
            answer =''
    if answer!="":
       # answer = answer.replace(' ', '')
        count+=len(set(answer))
    return count

print(count_unq())



#------------- part-2-----------------------

def common_answers():
    answer=''
    answer_list=[]
    count =0    
    for i in data:
        if i!='':
            answer+=i
            answer_list.append(i)
        else:
            unique=list(set(answer))   
            count+=count_common(list(unique),answer_list)
            answer = ''
            answer_list=[]
    if answer!="":
        count+=count_common(answer,answer_list)
    return count

def count_common(unq_answer,answer_list):
    questions=[]
    for i in unq_answer:
        common = True
        for j in answer_list:
            if i not in j:
                common = False
        if common==True:
            questions.append(i)
    return len(questions)


print("common_answers",common_answers())
    
