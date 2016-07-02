#Linear Regression
###1.Background
    In statistics, linear regression is an approach for modeling the relationship between a scalar 
    
    dependent variable y and one or more explanatory variables (or independent variables) denoted X. 
    
    The case of one explanatory variable is called simple linear regression. For more than one explanatory 
    
    variable, the process is called multiple linear regression.
###2.Derivation
    
    Here is going to show two kinds of derivation.
    
    Input vecoter is X which is [x1,x2,...,xn] and the number is n, Output is Y which is [y1,y2,...,yn], 
    
    Assume that Y has relationship with X as below, Theta is coefficient vector which is unknow.
        
    Epsilon is error between real value and predictive value.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=h_%7B%5Ctheta%7D%3D%5Ctheta%5E%7BT%7DX%5C%5C%0A%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%5C%0AY%3D%5Ctheta%5E%7BT%7DX%2B%5Cepsilon%20%0A%0A%0A%0A" style="border:none;" />

    (1) Gradient descent method
        
        The loss function is defined as follows.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=J(W)%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5Em%20(h_%7Bw%7D(x%5E%7B(i)%7D)-y%5E%7B(i)%7D)%5E%7B2%7D" style="border:none;" />
        
        Update W by the follow formula, which cause loss function decrease in gradient direction.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20J(W)%7D%7B%5Cpart%20w_%7Bk%7D%7D%3D%20(WX%5E%7B(i)%7D-y%5E%7B(i)%7D)x%5E%7Bi%7D_%7Bk%7D" style="border:none;" />
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=w_%7Bk%7D%5E%7Bnew%7D%3Dw_%7Bk%7D%2B%5Calpha%20%5Cfrac%7B%5Cpart%20J(W)%7D%7B%5Cpart%20w_%7Bk%7D%7D" style="border:none;" />
        
        Batch gradient descent method, Use all the data to update W each iterative time, 
        
        it costs memery and iteration, it can continuously convergent. 
        
        Random gradient descent method, Use a random data sample to W each iterative time, 
        
        it costs less memery and few iteration, its result may be wandering in the convergence.
        
    (2) Least square method

<img src="http://chart.googleapis.com/chart?cht=tx&chl=XW%3DY%20%20%5C%20%5C%20%5C%20%3D%3E%20X%5E%7BT%7DXW%3DX%5E%7BT%7DY%20%20%5C%20%5C%20%5C%20%5C%5C%0A%5C%20%5C%20%5C%20%5C%5C%0Aif%20(X%5E%7BT%7DX)%5E%7B-1%7D%20exist%20%5C%5C%0A%5C%20%5C%20%5C%20%5C%20%5C%5C%0A%0AW%20%3D%20(X%5E%7BT%7DX)%5E%7B-1%7DX%5E%7BT%7D%20Y%0A%0A%0A%0A" style="border:none;" />



