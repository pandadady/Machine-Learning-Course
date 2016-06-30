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
    
    Input:
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=T%3D%5B(x%5E%7B(1)%7D%2Cy%5E%7B(1)%7D)%2C(x%5E%7B(2)%7D%2Cy%5E%7B(2)%7D)%2C...(x%5E%7B(n)%7D%2Cy%5E%7B(n)%7D)%5D%0A%3Cbr%3E%0AY%5Cin%20%5B-1%2C1%5D" style="border:none;" />

    The output of xi of number i classifier is 
<img src="http://chart.googleapis.com/chart?cht=tx&chl=k_%7Bi%7D(x%5E%7Bi%7D)" style="border:none;" />
    
    
    
    
    
    Assume that here is a classifier of adaboost, its misclassified rate is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cepsilon_%7Bi%7D%20%3D%5Cfrac%7BNo.i%20%5C%20%5C%20%5C%20misclassified%20%5C%20%5C%20%5C%20%20number%7D%7B%20total%20%5C%20%5C%20%5C%20%20number%7D" style="border:none;" />
    
    Adaboost algorithm assigns a weight alpha for each classifier, alpha is calculated by the formula shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7Bi%7D%20%3D%5Cfrac%7B1%7D%7B2%7Dln(%5Cfrac%7B1-%5Cepsilon%20%7D%7B%5Cepsilon%7D)" style="border:none;" />

    
    
    
    

    

    
