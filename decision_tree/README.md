#decision tree

1.Background

    In real life, we will encounter this kind of problem.
    
    Some commodity's purchase have a certain relationship with customer's age,salary,and commodity prices. 
    
    We can get a table contains commodity's purchase information (yes / no) and age, salary, price. 
    
    Hope to predict another customer would buy a certain commodity whether or not. 
    
    In the situation, we present decision_tree algorithm.
    
2.Definition

    In the situation of known all kinds of attribute probability of happening,
    
    Use attributes as decision node to build a tree and Use results as leaf node .
    
    There are many algorithm about building decision tree, such as ID3,CART.
    
    ID3 is a decision tree classification algorithm based on information entropy.
    
3.Characteristic

    Advantage：
    
        (1) The computational complexity is not high.
        
        (2) The output is easy to understand.
        
        (3) Able to handle irrelevant feature data.
        
        (4) The lack of intermediate value has little influence on the results
    
    Disadvantage：
    
        There may be excessive matching problem.
    
    Application scope:
    
        Nominal type and numeric type

4.Algorithm thinking
    
    The key step is to construct a decision tree splitting attribute.
    
    The so-called splitting attribute is to construct different branches according to the different 
    
    division of a certain characteristic attribute, 
    
    and the goal is to make each split subset as pure as possible.
    
    There are many kinds of attribute selection algorithms.Here to introduce ID3
    
      
