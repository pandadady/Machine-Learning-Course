#Regression Tree

###1.Background
    
    There is a decision tree algorithm based on ID3 algorithm in the Machine-Learning folder.
    
    Decision tree algorithm use ID3 algorithm to split data by the purity of data.
    
    It is suitable for discrete type data but not continuous type data.
    
    It is a classification algorithm. 
    
    It is the time o learn another tree algorithm which is called CART(Classification And Regression Trees).
    
    It is used to solve the problem about non-linear regression.
    
    The core thinking of regression tree can be described by 2 steps.
    
    First, split the entire data into small sub data sets.
    
    Second, use suitable regression algorithm to fit the small data set.
    
###2.Algorithm Thinking

    Here is 2 kinds of CART. One is named regression tree,anther is called model tree. 
    
    The difference between 2 trees are the regression method and the splitting method.
    
    Create the tree：
    
        find the best way
        
        split data into 2 parts
        
        Create tree with part 1
        
        Create tree with part 2
    
    (1) Regression tree
    
        The regression method is mean of sub data (yes, too simple)
        
        The standard of splitting data is sample variance of sub data(yes, because of regression method), 
    
        which way of splitting minimize the variance is the best splitting way.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=var%20%3D%20%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5En%20(x%5E%7B(i)%7D-%5Cbar%7Bx%7D)" style="border:none;" />

    (2) Regression tree
        
        The regression method is linear regression.
        
        We have a special folder about linear regression.
        
        The splitting method is Expected variance.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=var%20%3D%20%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5En%20(x%5E%7B(i)%7D-E(x))%5C%5C%0A%5C%5C%0AE(x)%20is%20expected%20value." style="border:none;" />
        
        
        

        
    
    
