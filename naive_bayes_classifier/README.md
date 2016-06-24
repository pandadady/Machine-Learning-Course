#naive bayes classifier

1.Background

    First of all, make clear classification problem.
    
    Classification problem often use Empirical methods to construct the mapping rules.
    
    In general situation, classification problem is lack of enough infomation to construct 
    
    hundred percent correct mapping rules,
    
    but it will achieve a certain sense correct according to learning experience data.
    
    Secondly, make clear the bayes theorem.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=P(A%7CB)%3D%5Cfrac%7BP(B%7CA)P(A)%20%7D%7BP(B)%7D&chco=000000&chf=a,s,00000080" style="border:none;" />
    
    Among them, P(A|B) is the probability of the occurrence of A event when the B event occurs.
    
3.Characteristic

    Advantage:
    
        Able to handle multiple classification problems.
        
    Disadvamtage:
    
        Sensitive to input data
        
    Application scope:
    
        Nominal type
    
4.Algorithm thinking
    
    Here is a example of text classification.
    
    Given text list is below.
    
    [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
     ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
     ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
     ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
     ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
     ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
     
