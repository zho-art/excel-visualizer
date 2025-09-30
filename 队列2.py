l_person = [
    {'name':'A','sex':'M'},
    {'name':'B','sex':'F'},
    {'name':'C','sex':'M'},
    {'name':'D','sex':'M'},
]
def dance_partner(l_person:list):
    mdancers = SqQueue()
    fdancers = SqQueue()
    for p in l_person:
        if p['sex']=='F':
            fdancers.en_queue(p)
        else:
            mdancers.en_queue(p)
        print('The dancing partners:')
        while len(fdancers) !=0 and len(mdancers) !=0:
            f = fdancers.de_queue()
            m = mdancers.de_queue()
            print('{0}{1}'.format(f['name'],m['name']))
            if len(fdancers) != 0:
                p = fdancers.get_head()
                print('The first woman to get a partner is :{0}'.format(p['name']))
            elif len(mdancers)!=0:
                p = mdancers.get_head()
                print('The  is:{0}'.format(p['name']))      



from collections import deque
def dance_partner(l_person: list):  
    mdancers = deque()  
    fdancers = deque()  
    # 分类舞者  
    for p in l_person:  
        if p['sex'] == 'F':  
            fdancers.append(p)  
        else:  
            mdancers.append(p)  
    # 配对并打印  
    print('The dancing partners:')  
    while fdancers and mdancers:  
        f = fdancers.popleft()  
        m = mdancers.popleft()  
        print(f'{f["name"]} and {m["name"]}')  
    # 打印剩余的舞者（如果有）  
    if fdancers:  
        print('Remaining women without partners:')  
        for f in fdancers:  
            print(f'{f["name"]}')  
    if mdancers:  
        print('Remaining men without partners:')  
        for m in mdancers:  
            print(f'{m["name"]}')  
  
# 示例使用  
l_person = [  
    {'name': 'A', 'sex': 'M'},  
    {'name': 'B', 'sex': 'F'},  
    {'name': 'C', 'sex': 'M'},  
    {'name': 'D', 'sex': 'M'},  
    {'name': 'E', 'sex': 'F'},  
]  
dance_partner(l_person)                                