#Support Vector Machine

###1.Summary
    support vector machine is supervised learning models with associated learning algorithms that 
    
    analyze data used for classification and regression analysis. Given a set of training examples, 
    
    each marked for belonging to one of two categories, an SVM training algorithm builds a model that 
    
    assigns new examples into one category or the other, making it a non-probabilistic binary linear classifier. 
    
    Above paragraph is from English Wikipedia.
    
    Support vector machine is a classifier using the separating surface to classify the data.
    
    For the n-dimensional data separating surface is n-1 dimension

    For a plane, the separating surface is a straight line.
    
    We hope that the points on both sides of the surface are far from the surface as far as possible.
    
    The nearest point to the separation surface is called the margin.
    
    The support vector is the closest point.
    
    The goal is to maximize the distance between the support vectors and the separation surface.
    
###2.Derivation
    The derivation of support vector machine algorithm is difficult for me at first.
    
    (1) function margin and geometric margin.
    
        Given a training sample set，(xi,yi), x repesents feature, y repesents class. i repesents the number i sample.
        
        Function margin definition is shown as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%20%5Chat%7B%5Cgamma%7D%5E%7B(i)%7D%3Dy%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%7D%2Bb)" style="border:none;" />
        
        Geometric margin definition is shown as below.
        
<img src="http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131131571364.png" height="309" width="360"/>
