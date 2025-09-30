#邻接矩阵表示法
INF = 0x3f3f3f3f
class AMGraph:
    def __init__(self):
        self.vexs = [] #顶点表
        self.arcs = [] #邻接矩阵
        self.vexnum = 0 #图的当前结点
        self.arcnum = 0 #图的当前边数
    def locate_vex(self,name):
        #定位顶点在顶点数组中的下标
        for i in range(0,self.vexnum):
            if self.vexs[i] == name:
                return i    
    def create_udn(self):
        #采用邻接矩阵创建无向网
        self.vexnum = int(input())  #输入总顶点数
        self.arcnum = int(input())  #输入总边数
        for i in range(self.vexnum):
            vexname = input() 
            self.vexs.append(vexname)
        #初始化邻接矩阵，边的权值均置于无穷大
        self.arcs = [[INF for i in range(self.vexnum)] for i in range(self.vexnum)]
        for k in range(self.arcnum):   #构造邻接矩阵
            v1 = input()
            v2 = input()
            w = int(input())  #输入一条边依附的顶点及权值
            i= self.locate_vex(v1)
            j = self.locate_vex(v2)   #确人v1和v2在图中的位置，即顶点数组的下标
            self.arcs[i][j] = w  #边<v1,v2>的权值为w
            self.arcs[j][i] = self.arcs[i][j] #置<v1,V2>的对称边<v2,v2>的权值为w
if __name__ == '__main__':
    g = AMGraph()
    g.create_udn()
    print('邻接矩阵：')
    for i in range(0,g.vexnum):
        for j in range(0,g.vexnum):
            if j != g.vexnum-1:
                if (g.arcs[i][j] < INF):
                    print(g.arcs[i][j],end='\t')
                else:
                    print('?\t',end='')
            else:
                if (g.arcs[i][j] < INF):
                    print(g.arcs[i][j])
                else:
                    print('?')   


#先序遍历二叉树AI
class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.Lchild = None
        self.rchild = None

    def create_bitree(self):
        # 按先序次序输入二叉树中结点的值
        ch = input("请输入节点值（输入#表示空节点）: ")
        if ch == '#':
            self.data = None
        else:
            self.data = ch  # 根节点赋给ch
            self.Lchild = BinaryTree()  # 为当前结点创造一个空的左子树
            self.Lchild.create_bitree()  # 递归创建左子树
            self.rchild = BinaryTree()
            self.rchild.create_bitree()

    def preorder_recursive(self):
        # 前序遍历二叉树的递归算法
        if self.data is not None:
            print(self.data)  # 访问根节点
            self.Lchild.preorder_recursive()  # 前序遍历左子树
            self.rchild.preorder_recursive()  # 前序遍历右子树
def copy(t):
    # 复制一颗完全相同的二叉树
    if t.data is None:
        tree = BinaryTree()
    else:
        tree = BinaryTree(t.data)
        tree.Lchild = copy(t.Lchild)
        tree.rchild = copy(t.rchild)
    return tree

def depth(t):
    # 计算深度
    if t.data is None:
        return 0
    else:
        return 1 + max(depth(t.Lchild), depth(t.rchild))

def node_count(t):
    # 统计二叉树结点的个数
    if t.data is None:
        return 0
    else:
        return 1 + node_count(t.Lchild) + node_count(t.rchild)

if __name__ == '__main__':
    tree = BinaryTree()
    print('请输入二叉树各结点的值:')
    tree.create_bitree()
    new_tree = copy(tree)
    print('复制得到的新树的前序序列(递归):')
    new_tree.preorder_recursive()  # 使用正确的方法名
    print('新树的深度:')
    print(depth(new_tree))
    print('新树的结点数:')
    print(node_count(new_tree))
              