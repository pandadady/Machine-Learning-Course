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
    
    The key step in constructing a decision tree is splitting attributes. 
    
    splitting attribute is to construct different branches according to the different 
    
    division of a certain characteristic attribute, 
    
    and the goal is to make each split subset as pure as possible.
    
    The key of splitting attribute is to choose the measure of attribute selection
    
    The measure of attribute selection is a split criterion. There are many algorithm about measure of attribute selection.
    
    here to introduce ID3.
    
    From the information theory, we know that the smaller the expected information, 
    
    the greater the information gain, and thus the higher the purity.
    
    So the core idea of ID3 algorithm is to use the information gain as the standard to select attributes.

    That is to say, when each split, the attribute of the maximum information gain is needed to split.
    
    
    
    
