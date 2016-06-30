#AdaBoost
###1.Background
    AdaBoost, short for "Adaptive Boosting". It can be used in conjunction with many other types of learning 
    
    algorithms.AdaBoost is adaptive in the sense that a misclassified sample of the previous classifier is 
    
    used to train the next classifier. AdaBoost is sensitive to noisy data and outliers.
    
    In some problems it can be less susceptible to the overfitting problem than other learning algorithms.
    
    The individual learners can be weak, but as long as the performance of each one is slightly better than random 
    
    guessing (e.g., their error rate is smaller than 0.5 for binary classification), 
    
    the final model can be proven to converge to a strong learner.

    From wikipedia.
    
###2.Derivation
    
    The below section is from <<AdaBoost and the Super Bowl of Classifiers A Tutorial 
    
    Introduction to Adaptive Boosting>>
    
    Input:
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=T%3D%5B(x%5E%7B(1)%7D%2Cy%5E%7B(1)%7D)%2C(x%5E%7B(2)%7D%2Cy%5E%7B(2)%7D)%2C...(x%5E%7B(n)%7D%2Cy%5E%7B(n)%7D)%5D%0A%3Cbr%3E%0AY%5Cin%20%5B-1%2C1%5D" style="border:none;" />

    The output of xi of number i classifier is  
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=k_%7Bi%7D(x%5E%7Bi%7D)" style="border:none;" />

    The (m-1)-th iteration is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=C_%7B(m-1)%7D(x_%7Bi%7D)%3D%5Calpha_%7B1%7Dk_%7B1%7D(x%5E%7Bi%7D)%2B%5Calpha_%7B2%7Dk_%7B2%7D(x%5E%7Bi%7D)%2B...%2B%5Calpha_%7Bm-1%7Dk_%7Bm-1%7D(x%5E%7Bi%7D)" style="border:none;" />

    The (m)-th iteration is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=C_%7B(m)%7D(x_%7Bi%7D)%3DC_%7B(m-1)%7D(x_%7Bi%7D)%2B%5Calpha_%7Bm%7Dk_%7Bm%7D(x%5E%7Bi%7D)" style="border:none;" />
    
    Set total errors of m-th round is exponential loss, formula is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=E_%7Bm%7D%3D%5Csum_%7Bi%3D1%7D%5EN%20e%5E%7B-y_%7Bi%7DC_%7B(m)%7D(x_%7Bi%7D)%7D%3Cbr%3E%0A%3D%5Csum_%7Bi%3D1%7D%5EN%20e%5E%7B-y_%7Bi%7D(C_%7B(m-1)%7D(x_%7Bi%7D)%2B%5Calpha_%7Bm%7Dk_%7Bm%7D(x_%7Bi%7D))%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Set%3A%20%5C%20%5C%20%5C%20w_%7Bi%7D%5E%7B(m)%7D%3De%5E%7B-y_%7Bi%7DC_%7B(m-1)(x_%7Bi%7D)%7D%7D%0A%3Cbr%3E%0A%3Cbr%3E%0A%3Cbr%3E%0A%0AE_%7Bm%7D%3D%20%5Csum_%7Bi%3D1%7D%5EN%20w_%7Bi%7D%5E%7B(m)%7D%20e%5E%7B-y_%7Bi%7D%5Calpha_%7Bm%7Dk_%7Bm%7D(x_%7Bi%7D)%7D%7D" style="border:none;" />
    
    It is easy to understand that some of Ki are correct and the others are error, so E trans to the below formula.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=E_%7Bm%7D%3D%20%5Csum_%7By_%7Bi%7D%3Dk_%7Bm%7D(x_%7Bi%7D)%7D%20w_%7Bi%7D%5E%7B(m)%7D%20e%5E%7B-%5Calpha_%7Bm%7D%7D%2B%5Csum_%7By_%7Bi%7D%5Cne%20k_%7Bm%7D(x_%7Bi%7D)%7D%20w_%7Bi%7D%5E%7B(m)%7D%20e%5E%7B%5Calpha_%7Bm%7D%7D" style="border:none;" />
    
    Simplify the notation to
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=E_%7Bm%7D%3D%20W_%7Bc%7D%20e%5E%7B-%5Calpha_%7Bm%7D%7D%2BW_%7Be%7D%20e%5E%7B%5Calpha_%7Bm%7D%7D" style="border:none;" />

    Em is a function of alpha_m. It's easy to get a alpha_m when make Em get min value.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20E_%7Bm%7D%7D%7B%5Cpart%20%5Calpha_%7Bm%7D%7D%20%3D%20-W_%7Bc%7De%5E%7B-%5Calpha_%7Bm%7D%7D%2BW_%7Be%7De%5E%7B%5Calpha_%7Bm%7D%7D%3D0" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%20-W_%7Bc%7D%2BW_%7Be%7De%5E%7B2%5Calpha_%7Bm%7D%7D%3D0%3Cbr%3E%0A%5Calpha_%7Bm%7D%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7BW_%7Bc%7D%7D%7BW_%7Be%7D%7D)" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7Bm%7D%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7BW-W_%7Be%7D%7D%7BW_%7Be%7D%7D)%3Cbr%3E%0A%3D%5Calpha_%7Bm%7D%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7B1-W_%7Be%7D%7D%7BW_%7Be%7D%7D)" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7Bm%7D%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7BW-W_%7Be%7D%7D%7BW_%7Be%7D%7D)%3Cbr%3E%0A%3D%5Calpha_%7Bm%7D%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7B%5Cfrac%7BW%7D%7BW%7D-%5Cfrac%7BW_%7Be%7D%7D%7BW%7D%7D%7B%5Cfrac%7BW_%7Be%7D%7D%7BW%7D%7D)%3Cbr%3E%0A%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7B1-e_%7Bm%7D%7D%7Be_%7Bm%7D%7D)" style="border:none;" />

    

    
    
    
    

    

    
