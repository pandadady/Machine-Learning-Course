#Support Vector Machine

###1.Summary
    support vector machine is supervised learning models with associated learning algorithms that 
    
    analyze data used for classification and regression analysis. Given a set of training examples, 
    
    each marked for belonging to one of two categories, an SVM training algorithm builds a model that 
    
    assigns new examples into one category or the other, making it a non-probabilistic binary linear classifier. 
    
    Above paragraph is from English Wikipedia.
    
    Support vector machine is a classifier using the separating plane to classify the data.
    
    For the n-dimensional data separating plane is n-1 dimension

    For a plane, the separating plane is a straight line.
    
    We hope that the points on both sides of the plane are far from the plane as far as possible.
    
    The nearest point to the separation plane is called the margin.
    
    The support vector is the closest point.
    
    The goal is to maximize the distance between the support vectors and the separation plane.
    
###2.Derivation
    The derivation of support vector machine algorithm is difficult for me at first.
    
    (1) Constrained extremum problem of the two programming.
    
        Given a training sample set，(xi,yi), x repesents feature, y repesents class -1 or 1. 
        
        i repesents the number i sample.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=z%3Dw%5E%7BT%7Dx%5E%7B(i)%7D%2Bb%3Cbr%3E%0A%3Cbr%3E%0Ag%3D1%2Cz%5Cge%200%3Cbr%3E%0A%3Cbr%3E%0Ag%3D-1%2Cz%3C0" style="border:none;" />
        
        Function margin definition is shown as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%20%5Chat%7B%5Cgamma%7D%5E%7B(i)%7D%3Dy%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%7D%2Bb)" style="border:none;" />
        
        Therefore,function margin repesents that the features are the confidence of positive or negative.
        
        Geometric margin definition is shown as below.
        
<img src="http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131131571364.png" height="309" width="360"/>

        Assume that B is on plane of WT+b=0,the distance from A to the surface is repesented by ri.
        
        B is the projection of A on the plane.if A is (xi，yi).B is show as below

<img src="http://chart.googleapis.com/chart?cht=tx&chl=x%3Dx%5E%7B(i)%7D-%5Cgamma%20%5E%7B(i)%7D%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=w%5E%7BT%7D(x%5E%7B(i)%7D-%5Cgamma%20%5E%7B(i)%7D%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D)%2Bb%3D0" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cgamma%20%5E%7B(i)%7D%20%3D%20%5Cfrac%7Bw%5E%7BT%7Dx%5E%7B(i)%7D%2Bb%7D%7B%7C%7Cw%7C%7C%7D%3D(%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D)%5E%7BT%7Dx%5E%7B(i)%7D%2B%5Cfrac%7Bb%7D%7B%7C%7Cw%7C%7C%7D" style="border:none;" />

        r is the distance from point to the plane.
        
        In other way.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cgamma%20%5E%7B(i)%7D%20%3Dy%5E%7B(i)%7D((%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D)%5E%7BT%7Dx%5E%7B(i)%7D%2B%5Cfrac%7Bb%7D%7B%7C%7Cw%7C%7C%7D)" style="border:none;" />

        When ||w|| is 1 , geometric margin is the function margin.
        
        The distance from nearest point to the plane is expressed by mathematical formula as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cgamma%20%3D%20min_%7Bi%3D1%2C...m%7D%5Cgamma%20%5E%7B(i)%7D" style="border:none;" />
        
        In other way, the purpose is to find a plane which is as far from as the nearest point.
        
        The formalization is show as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=max_%7B%5Cgamma%2Cw%2Cb%7D%5Cgamma%20%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%20%5Cgamma%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%7C%7Cw%7C%7C%3D1%0A" style="border:none;" />
        
        ||w||=1 constraint w. It's a geometric margin.
        
        Let's transfer it into a  function margin.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=max_%7B%5Cgamma%2Cw%2Cb%7D%20%5Cfrac%7B%5Cgamma%20%7D%7B%7C%7Cw%7C%7C%7D%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%20%5Cgamma%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%0A" style="border:none;" />

        Assume r is 1 and transfer min of 1/||w|| to  max of ||w||/2.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7B%5Cgamma%2Cw%2Cb%7D%20%5Cfrac%7B1%7D%7B2%7D%7C%7Cw%7C%7C%5E%7B2%7D%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%201%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%0A" style="border:none;" />

        It is a constrained extremum problem of the two programming. First line is objective function which is convex function.
        
        Second line and third line is constraint function.
        
    (2) Lagrange multiplier method
    
        Generalized inequality constrained extremum problem：
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7Bw%7D%20f(w)%3Cbr%3E%0A%3Cbr%3E%0A%20%20%20%20s.t.%20g_%7Bi%7D(w)%5Cle%200%2Ci%3D1%2C...%2Ck%20%3Cbr%3E%0A%3Cbr%3E%0A%20%20%20%20h_%7Bi%7D(w)%3D0%2C%20i%3D1%2C...l%0A%0A" style="border:none;" />
        
        
        
        
        
        
        


