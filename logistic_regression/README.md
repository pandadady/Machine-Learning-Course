#Logistic regression
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

<img src="http://chart.googleapis.com/chart?cht=tx&chl=t%20%3D%20%5Cbeta_%7B0%7D%20%2B%20%5Cbeta_%7B1%7Dx&chco=000000&chf=a,s,00000080" style="border:none;" />

    The logistic function can now be written as:
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=F(x)%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B-(%5Cbeta_%7B0%7D%20%2B%20%5Cbeta_%7B1%7Dx)%7D%7D&chco=000000&chf=a,s,00000080" style="border:none;" />

    They are independent given design matrix X and shared with parameters B.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=X%5E%7Bi%7D%20%3D%20w_%7B0%7D%2Bw_%7B1%7Dx%5E%7Bi%7D_%7B1%7D%2Bw_%7B2%7Dx%5E%7Bi%7D_%7B2%7D%2B...%2Bw_%7Bn%7Dx%5E%7Bi%7D_%7Bn%7D&chco=000000&chf=a,s,00000080" style="border:none;" />
    
###3.Optimum solution
    
    
   
    

