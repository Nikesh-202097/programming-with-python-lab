''' program to print all permutations of a string '''
# function for add result to output list
def toString(List): 
    return ''.join(List)

# function for computing permutations
def permutations(lst,s,e):  #str is list,s is  curent start index ,end index
    if s==e:                # check we reach at end then print list
        print (toString(lst))
    else: 
        #fixed fist element in each case and swap next one with each elements remains
        for i in range(s,e): 
            lst[s], lst[i] = lst[i], lst[s] 
            permutations(lst, s+1, e) 
            lst[s], lst[i] = lst[i], lst[s]
    
        
str="STR"
lst=list(str)                                      
permutations(lst,0,3)
    