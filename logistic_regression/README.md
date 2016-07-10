#Logistic Regression
###1.Background
    Logistic regression was developed by statistician David Cox in 1958.
    
    Logistic regression measures the relationship between the categorical 
    
    dependent variable and one or more independent variables by estimating 
    
    probabilities using a logistic function, which is the cumulative logistic distribution.
    
###2.Definition
    An explanation of logistic regression can begin with an explanation of the standard logistic function. 
    
    The logistic function is useful because it can take an input with any value from negative to positive infinity, 
    
    whereas the output always takes values between 0 and 1 and hence is interpretable as a probability. 
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Csigma(t)%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B-t%7D%7D&chco=000000&chf=a,s,00000080" style="border:none;" />

     A graph of the logistic function on the t-interval (-6,6) is shown below.
     
<img src="https://upload.wikimedia.org/wikipedia/commons/8/88/Logistic-curve.svg" height="200" width="300"/>

    Assume that t is a linear function of a single explanatory variable  x 
    
    We can then express t as follows:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=t%3Dw_%7B0%7D%2Bw_%7B1%7Dx&chco=000000&chf=a,s,00000080" style="border:none;" />

    The logistic function can now be written as:
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=Y%3D%5Cfrac%7B1%7D%7B1%2Be%5E%7B-(w_%7B0%7D%2Bw_%7B1%7DX)%7D%7D&chco=000000&chf=a,s,00000080" style="border:none;" />

    They are independent given design matrix X and shared with parameters B.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=X%5E%7Bi%7D%20%3D%20w_%7B0%7D%2Bw_%7B1%7Dx%5E%7Bi%7D_%7B1%7D%2Bw_%7B2%7Dx%5E%7Bi%7D_%7B2%7D%2B...%2Bw_%7Bn%7Dx%5E%7Bi%7D_%7Bn%7D&chco=000000&chf=a,s,00000080" style="border:none;" />
    
###3.Optimum solution
    
    The key of the algorithm is to find the optimal w.
    
    According to the definition of the likelihood function, we get the following formula.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=L(Y)%3D%5Cprod_%7Bi%3D1%7D%5Em%20p(Y%5Ei)%0A&chco=000000&chf=a,s,00000080" style="border:none;" />

    Assume that
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=p(Y_%7Bi%7D%3D0%7CX)%3Dp_%7Bi%7D%0A%0A&chco=000000&chf=a,s,00000080" style="border:none;" />

    And then
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=p(Y_%7Bi%7D%3D1%7CX)%3D1-p_%7Bi%7D%0A%0A&chco=000000&chf=a,s,00000080" style="border:none;" />

    so
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=p(Y_%7Bi%7D)%3Dp_%7Bi%7D%5E%7BY_%7Bi%7D%7D(1-p_%7Bi%7D)%5E%7B1-Y_%7Bi%7D%7D%0A%0A&chco=000000&chf=a,s,00000080" style="border:none;" />

    Bring p(Yi) into likelihood function formula.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=L(W)%3D%5Cprod_%7Bi%3D1%7D%5EM%20(%5Cfrac%7B1%7D%7B1%2Be%5E%7B-(w_%7B0%7D%2Bw_%7B1%7Dx%5E%7Bi%7D_%7B1%7D%2B...%2Bw_%7Bn%7Dx%5E%7Bi%7D_%7Bn%7D)%7D%7D)%5E%7BY%5E%7Bi%7D%7D%0A(1-%5Cfrac%7B1%7D%7B1%2Be%5E%7B-(w_%7B0%7D%2Bw_%7B1%7Dx%5E%7Bi%7D_%7B1%7D%2B...%2Bw_%7Bn%7Dx%5E%7Bi%7D_%7Bn%7D)%7D%7D)%5E%7B1-Y%5E%7Bi%7D%7D&chco=000000&chf=a,s,00000080" style="border:none;" />
    
    The optimal w is the solution of the maximum value of L(w) value.
    
    Because lnL (W) is a monotonically increasing function of L (W), the optimal solution is consistent.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=lnL(W)%3D%5Csum_%7Bi%3D1%7D%5EM%20(Y%5E%7Bi%7Dln%5Cfrac%7Be%5E%7BX%5E%7Bi%7D%7D%7D%7B1%2Be%5E%7BX%5E%7Bi%7D%7D%7D%2B(1-Y%5E%7Bi%7D)ln%5Cfrac%7B1%7D%7B1-e%5E%7BX%5E%7Bi%7D%7D%7D)" style="border:none;" />
    
    Gradient ascent method is needed here.For a linear function, the gradient is the slope.
    
    Gradient repesents direction. a repesents step.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=w_%7Bk%7D%3Dw_%7Bk%7D%2B%5Calpha%20%5Cfrac%7B%5Cpart%20lnL(w)%7D%7B%5Cpart%20w_%7Bk%7D%7D&chco=000000&chf=a,s,00000080" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(w)%7D%7B%5Cpart%20w_%7Bk%7D%7D%3D%5Csum_%7Bi%3D1%7D%5Em%20x%5E%7Bi%7D_%7Bk%7D%5By%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7B-x_%7Bi%7D%7D%7D%5D" style="border:none;" />

###4.Algorithm thinking
    
    Random gradient ascent method is needed here.
    
    (1) Initialize that w is 1, and default iteration number is 150.
    
    (2) At each iteration, it is needed to calculate w for m times, m is the number of input data.
    
    (3) At each calculation, it is needed to randomly get 1 piece of data to calculate, 
    
        and delete it from data set at the end.
    
    
    
    
    


    
    
    

