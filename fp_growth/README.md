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
        
        Setp 1: Calculate each number of element ( frequent of element), record element which is greater than 
        
                the min support in the header table
        
        Setp 2: Loop the data set, fliter Element-set with element of hearder table, The new Element-set is 
        
                composed by element which is greater than the min support.
                
        Setp 3: Sort the new Element-set by frequent of element. If element is in the tree, update count, if
        
                element isn't in the tree, create a new node on the tree. If element is on the element link table 
                
                of header table , hang it at the end of element link table, if element isn't on the element link table 
                
                save tree node in the element link table.
                
                Header table: {'p': [1, None], 's': [1, None], 'r': [3, head node], 't': [1, None]}
                
    (3) Search Frequent item set
        
        Setp 1: Loop header table,search along the element node link. Search up from each element to the root node of fp-tree
        
                Get path end with element of node link.
        
        Step 2: Assume path is the sub data set, repeat step 2 
        
        Step 3: Repeat step 1 and 2
