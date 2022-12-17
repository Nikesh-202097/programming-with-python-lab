from dataclasses import dataclass

@dataclass
class Edge :
    ver_s:int=0
    ver_d:int=0
    wt:int=0
    
    def get_ver_s(self):
        return self.ver_s
    
    def get_ver_d(self):
        return self.ver_d
    
    def get_wt(self):
        return self.wt
    
    def setter(self,s,d,w):
        self.ver_s=s
        self.ver_d=d
        self.wt=w
    
    
    # def __repr__(self):
    #     print(self.ver_s,end="")
    #     print(":(",end="")
    #     print(self.ver_d,end=",")
    #     print(self.wt,end="")
    #     print(")")
    
@dataclass    
class Graph:
    
    no_ver:int=1
    graph=[]
    
    def add(self,e):
        self.graph.append(e)
        
    
    def display(self):
        for i in range(len(self.graph)):
            print(self.graph[i])
    
print("enter the no of edge ")
n=int(input())
g=Graph(n)
for i in range(n):
    e=Edge()
    print("enter edge like this 'source,destination,wt' ")
    str=input()
    
    list=str.split(sep=",")
    e.setter(int(list[0]),int(list[1]),int(list[2]))
    g.add(e)

g.display()   

