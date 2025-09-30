max_size =100 
class SqQueue: 
    def __init__(self):

#初始化一个空队列
        self.elem= [None]* max_size #为队列分配一个最大容量为max size的数组空间
        self.front, self.rear =0,0 #头指针和尾指针置为零，队列为空
        self.max_size - max_size 
def __len__(self): 
#返回队列的元素个数，即队列的长度
    return (self.rear -self.front + self.max _size)% self.max_size 
def en_queue (self, e): 
#把元素e加入队尾
    if (self.rear +1)% self.max_size ==self.front: 
#尾指针在循环意义上加1后等于头指针，表明队满
        raise Exception('队列已满') 
    self.elem[self.rear]=e#新元素插入队尾
    self.rear=(self.rear+1)% self.max_size #队尾指针加1 
def de_queue (self): 
#删除队头元素并将其返回
    if self.front ==self.rear:
        #队空
        raise Exception('队列已空') 
    e=self.elem[self.front]#保存队头元素
    self.front =(self.front +1) % self.max_size#队头指针加1 
    return e 
def get_head(self): 
#返回队头元素，不修改队头指针
    if self.front !=self.rear:#队列非空
        return self.elem[self.front]#返回队头元素的值，队头指针不变
    else: 
        raise Exception('队列已空') 
def dance_partner(l_person: list): 
 #舞伴问题
#列表1_person中存放眺舞的男女。 
    mdancers= SqQueue()#男士队列初始化
    fdancers=SqQueue()#女士队列初始化
    for p in l_person: #依次将跳舞者根据其性别入队
        if p['sex']=='F': 
            fdancers.en_queue(p)#插入女队
    else: 
        mdancers.en_queue(p)#插入男队
        print ('The dancing partners are:') 
        while len (fdancers) !=0 and len (mdancers) !=0: 
            f=fdancers.de_queue()#女士出队
            m=mdancers.de_queue()#男士出队
            print('{0} {1}'.format(f['name'],m['name']))#输出男女姓名
        if len(fdancers)!=0:#女士队列非空，输出队头女士的姓名
            p= fdancers.get_head() 
            print (' The first woman to get a partner is:{0}'.format (p['name']) 
    elif len(mdancers)!=0:#男士队列非空，输出队头男士的姓名
        p= mdancers.get_head() 
        print('The first man to get a partner is:{0}'.format (P['name' 1]) 
if __name__=="__main__":

    l_person = [
    {'name': 'A', 'sex': 'M'},  
    {'name': 'B', 'sex': 'F'},  
    {'name': 'C', 'sex': 'M'},  
    {'name': 'D', 'sex': 'M'},  
    {'name': 'E', 'sex': 'F'},  
    ]  
    dance_partner(l_person)