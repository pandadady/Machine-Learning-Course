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
    
    
