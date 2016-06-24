#naive bayes classifier

###1.Background

    First of all, make clear classification problem.
    
    Classification problem often use empirical methods to construct the mapping rules.
    
    In general situation, classification problem is lack of enough infomation to construct 
    
    hundred percent correct mapping rules,
    
    but it will achieve a certain sense correct according to learning experience data.
    
    Secondly, make clear the bayes theorem.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=P(A%7CB)%3D%5Cfrac%7BP(B%7CA)P(A)%20%7D%7BP(B)%7D&chco=000000&chf=a,s,00000080" style="border:none;" />
    
    Among them, P(A|B) is the probability of the occurrence of A event when the B event occurs.
    
###2.Characteristic

    Advantage:
    
        Able to handle multiple classification problems.
        
    Disadvamtage:
    
        Sensitive to input data
        
    Application scope:
    
        Nominal type
    
##3.Algorithm thinking
    
    Here is a example of text classification.
    
    Given text list is below.
    
    [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
     ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
     ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
     ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
     ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
     ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
     
     Given its classification is below
     
     [0,
     1,
     0,
     1,
     0,
     1]
     
     The question is how to pridict new text belong to which class.
     
     (1) Extract words from text and add into vocabulary.
     
     (2) Use vocabulary to transfer text into words vector.
     
     Each vector is composed by 0 and 1 which repesents a word occurs in the text. 
     
     (3) According to bayes formula, it is able to get formula as below.
     
<img src="http://chart.googleapis.com/chart?cht=tx&chl=P(C_%7Bi%7D%7CW)%3D%5Cfrac%7BP(W%7CC_%7Bi%7D)P(C_%7Bi%7D)%20%7D%7BP(W)%7D&chco=000000&chf=a,s,00000080" style="border:none;" />

        W repesents words vector. Ci repesents class 1 or 0. Usually, use the following formula to get P(W|Ci)
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=P(W%7CC_%7Bi%7D)%3DP(w_%7B1%7D%7CC_%7Bi%7D))%2BP(w_%7B2%7D%7CC_%7Bi%7D))%2B...%2BP(w_%7Bn%7D%7CC_%7Bi%7D))&chco=000000&chf=a,s,00000080" style="border:none;" />
        
        wn repesents the number n word of text. 
        
        P(Ci) equals the number of 1 or 0 text be divided by the total number of text.
        
        If there is a new text as input, Output will be the maximum of P(C1|W) and P(C2|W), 
        
        and the results often skip to be devided by P(W) because they are all going to do so.
        
    (4) Calculate the maximum of P(C1|W) and P(C2|W) to choose class of new text.
    
