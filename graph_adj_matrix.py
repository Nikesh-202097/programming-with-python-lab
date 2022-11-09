from dataclasses import dataclass

@dataclass
class Edge :
    ver_s:int
    ver_d:int
    wt:int=0
    
    def get_ver_s(self):
        return self.ver_s
    
    def get_ver_d(self):
        return self.ver_d
    
    def get_wt(self):
        return self.wt
    
@dataclass    
class Graph:
    
    no_ver:int=1
    
    
    def __init__(self,n):
        self.no_ver=n
        self.g=[[0 for i in range(self.no_ver)] for j in range(self.no_ver) ]
    
    def add(self,e):
        self.g[int(e.get_ver_s())-1][int(e.get_ver_d())-1]=int(e.get_wt())
        self.g[int(e.get_ver_d())-1][int(e.get_ver_s())-1]=int(e.get_wt())
    def display(self):
        for i in range(self.no_ver):
            for j in range(self.no_ver):
                print(self.g[i][j],end='  ')
            print()
            

print("enter no of edge undirected graph with intger vertices")
no_edg =int(input())
g1=Graph(no_edg+1)
for i in range(no_edg):
    print("enter edge(v1 v2 w) ",i)
    edg=input()
    edg=edg.split()
    e1=Edge(edg[0],edg[1],edg[2])
    g1.add(e1)
g1.display()
    