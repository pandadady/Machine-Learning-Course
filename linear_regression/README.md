#Linear Regression
###1.Background
    In statistics, linear regression is an approach for modeling the relationship between a scalar 
    
    dependent variable y and one or more explanatory variables (or independent variables) denoted X. 
    
    The case of one explanatory variable is called simple linear regression. For more than one explanatory 
    
    variable, the process is called multiple linear regression.
###2.Derivation
    
    Here is going to show two kinds of derivation.
    
    (1) Gradient descent method
        Input vecoter is X which is [x1,x2,...,xn], Output is Y which is [y1,y2,...,yn], assume that Y has 
        
        relationship with X as below, W is coefficient vector which is unknow.
        
        <img src="http://chart.googleapis.com/chart?cht=tx&chl=Y%3DXW" style="border:none;" />
        
        The purpose is to get the suitable coefficient . Assume the suitable coefficient is W, then we get 
        
        <img src="http://chart.googleapis.com/chart?cht=tx&chl=h_%7Bw%7D(x)%3DXW" style="border:none;" />
        
        The loss function is defined as follows.
        
        <img src="http://chart.googleapis.com/chart?cht=tx&chl=J(W)%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5Em%20(h_%7Bw%7D(x%5E%7B(i)%7D)-y%5E%7B(i)%7D)%5E%7B2%7D" style="border:none;" />
        
        
        
    (2) Least square method
