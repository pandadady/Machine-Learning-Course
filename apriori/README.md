#Apriori
###1.Summary

    It is a association rule searching algorithm. 
    
    Association rule means the rule of 2 item how to be difined have relationship.
    
    Confidence degree measure the intensity of association rule. How to calculate the 
    
    confidence degree of certain association rule. It is important to understand frequent item sets 
    
    and support degree.Frequent item sets means set of items which often appears together.
    
    Support degree equal the percent of frequent item sets in the entire data set.
    
    Assume the formalization of association rule is like " {A}-->{B} "
    
    Confidence degree equal the ratio of support of { A,B } to support of { B }.
    
    There always is a way to find all the association rules of data set, such as saving data in memery and looping.
    
    It costs lots of time when the number of items is huge (It must be huge.)
    
    The Apriori principle said that if a item set is a non-frequent item set, its super item set must be 
    
    a non-frequent item set. 
    
###2.Detail
    
    The goal of Apriori algorithm is searching association rules. Before searching association rules, it is necessary 
    
    to find frequent item sets.
    
    How to find frequent item sets?
    
    (1) Set min support degree.
    
    (2) Calculate 1 element set of data set, frequent item set is the set greater than  min support degree.
    
    (3) Calculate 2 element set of data set, frequent item set is the set greater than  min support degree.
    
    (4) Go on till all the element set. 
    
    How to find association rules?
    
    (1) Set min confidence.
    
    (2) Loop all the frequent item sets,association rule is the rule greater than  min confidence.
    
###3.Improvement

    The above method of searching frequent item set will cost lots of time.
    
    Usually, FP-growth algorithm is used to solve the problem
    
    
    
    
    
