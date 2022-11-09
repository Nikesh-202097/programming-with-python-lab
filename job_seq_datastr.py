from dataclasses import dataclass

@dataclass
class Job :
    jn:int                       #job number
    pr:int                       #job profit
    dl:int                       #job deadline
    

    def __init__(self,j,p,d):
        self.jn=j                  
        self.pr=p                  
        self.dl=d                  
    
    ''' function to get job name'''
    def get_jn(self):
        return(self.jn)
    
    ''' function to grt profit'''
    def get_pr(self):
        return(self.pr)
    
    ''' function to get deadline'''
    def get_dl(self):
        return(self.dl)
    
    
    
class JobSeq :
    def __init__(self,):
        self.d=[]                  #list of jobs
    
    ''' function to add job to job seq list'''
    def add(self,i):
        self.d.append(i)
     
    ''' function to display JobSeq object'''
    def display(self):
        print(self.d)



js=JobSeq()
j1=Job(1,100,2)
js.add(j1)
j2=Job(2,200,1)
js.add(j2)
j3=Job(3,150,2)
js.add(j3)
j4=Job(4,250,1)
js.add(j4)

js.display()