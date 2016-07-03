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
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=J(%5Ctheta)%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5Em%20(h_%7B%5Ctheta%7D(x%5E%7B(i)%7D)-y%5E%7B(i)%7D)%5E%7B2%7D%0A%0A%0A" style="border:none;" />
        
        Update theta by the follow formula, which cause loss function decrease in gradient direction.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20J(%5Ctheta)%7D%7B%5Cpart%20%5Ctheta_%7Bk%7D%7D%3D(%5Ctheta%20x%5E%7B(i)%7D-y%5E%7B(i)%7D%20%20)x%5E%7B(i)%7D_%7Bk%7D%20%0A%5C%5C%0A%20%5C%20%5C%20%5C%5C%0A%5Ctheta_%7Bk%7D%5E%7Bnew%7D%3D%5Ctheta_%7Bk%7D-%5Calpha%20%5Cfrac%7B%5Cpart%20J(%5Ctheta)%7D%7B%5Cpart%20%5Ctheta_%7Bk%7D%7D%0A%0A%0A" style="border:none;" />
        
        Batch gradient descent method, Use all the data to update W each iterative time, 
        
        it costs memery and iteration, it can continuously convergent. 
        
        Random gradient descent method, Use a random data sample to W each iterative time, 
        
        it costs less memery and few iteration, its result may be wandering in the convergence.
        
    (2) Least square method

        As known from  2-norm definition, we can have
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%7C%7CX%7C%7C_%7B2%7D%3D(x_%7B1%7D%5E%7B2%7D%2Bx_%7B2%7D%5E%7B2%7D%2B...%2Bx_%7Bn%7D%5E%7B2%7D)%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D%0A%0A" style="border:none;" />
        
    In the linear regression algorithm derivation, the problem is how to calculate the special solution w
    
    of linear equations which is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7B%5Ctheta%7D%7C%7CX%5Ctheta-Y%7C%7C_%7B2%7D%5E%7B2%7D%0A%0A%0A%0A" style="border:none;" />
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%7C%7CX%5Ctheta-Y%7C%7C_%7B2%7D%5E%7B2%7D%5Cge%200%20%5C%5C%0A%5C%5C%0A%3D%3EX%5Ctheta%3DY%5C%5C%0A%5C%5C%0A%3D%3EX%5E%7BT%7DX%5Ctheta%3DX%5E%7BT%7DY%0A%0A%0A%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=When%20(X%5E%7BT%7DX)%5E%7B-1%7D%20%5C%20%5C%20exist%20%5C%5C%0A%20%5C%20%5C%20%5C%5C%0A%5Ctheta%3D%20(X%5E%7BT%7DX)%5E%7B-1%7DX%5E%7BT%7DY%0A%0A%0A%0A" style="border:none;" />

###3.Locally weighted linear regression derivation

    The linear regression algorithm is easy to appear under fitting condition.
    
    Locally weighted linear regression algorithm is often used to solve this sittuation.
    
    For the each pair of (x , y), There is a group of weight.  
    
    The weight and the distance from X to xi are in the direct ratio.
    
    (1) Least square method
    
        W is a diagonal matrix. The  diagonal element is 
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=w%5E%7Bi%7D%3Dexp(-%5Cfrac%7B(x%5E%7Bi%7D-x)%5E%7B2%7D%7D%7B2k%5E%7B2%7D%7D)" style="border:none;" />
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=X%5Ctheta%3DY%20%5C%20%5C%20%3D%3EWX%5Ctheta%3DWY%20%5C%20%5C%20%3D%3EX%5E%7BT%7DWX%5Ctheta%3DX%5E%7BT%7DWY%5C%5C%0A%20%5C%20%5C%20%5C%5C%0Aif%20(X%5E%7BT%7DWX)%5E%7B-1%7D%20then%3A%20%5C%20%5C%20%5Ctheta%3D(X%5E%7BT%7DWX)%5E%7B-1%7DX%5E%7BT%7DWY" style="border:none;" />




