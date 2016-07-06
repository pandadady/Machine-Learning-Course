#FP Growth
###1.Summary
    
    Apriori algorithm is slow in searching frequent item set.
    
    FP-Growth algorithm is used to search frequent item set in 2 round looping of data.
    
    It is based on FP-tree,which is short for frequent pattern tree.
    
###2.Detail
    
    (1) The data structure of FP-Tree 
    
        Tree node In python is shown as below
        
        class treeNode:
        
            def __init__(self, nameValue, numOccur, parentNode):
            
                self.name = nameValue
                
                self.count = numOccur
                
                self.nodeLink = None
                
                self.parent = parentNode     
                
                self.children = {} 
                
    (2) Create a FP-Tree
    
        For example, there is a data set
        
            [['r', 's'],
            
               ['r', 'p'],
               
               ['r', 't']]
        
        The element means 'r'. Element-set means ['r', 's'].
        
        Setp 1: Calculate each number of element ( frequent of element), record element which is greater than the min support in the 
        
                header table
        
        Setp 2: Loop the data set, fliter Element-set with element of hearder table, The new Element-set is composed by element which 
                
                is greater than the min support.
                
        Setp 3: Sort the new Element-set by frequent of element, save it into tree.
        
        
