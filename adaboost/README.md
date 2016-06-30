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
        
    Assume that here is a classifier of adaboost, its misclassified rate is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cepsilon_%7Bi%7D%20%3D%5Cfrac%7BNo.i%20%5C%20%5C%20%5C%20misclassified%20%5C%20%5C%20%5C%20%20number%7D%7B%20total%20%5C%20%5C%20%5C%20%20number%7D" style="border:none;" />

    

    
