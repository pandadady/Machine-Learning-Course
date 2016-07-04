#K Means

###1.Summary
  
    It is a unsupervise clustering algorithm, so it doesn't need training process.
    
    The key of clustering is to find the centroids of data. Usually, the number K of centroid is given by user.
    
    The mean of data is used as first centroid.
    
    While found centroids number < K:
        
        Looping centroids
            
            find 2 centroid in the current cluster and get the sum of centroid distance
            
            get the other cluster the sum of centroids distance
            
            compare the sum of centroids distance with last looping  the sum of distance
            
            record the splitting way of the min sum
            
        update clustering record
    
    The above is dichotomy k-means algorithm thinking.
    
    The way of finding centroid has 3 steps.
    
    (1) get centroid randomly between the min and max.
    
    (2) calc the distance from data sample to the centroid and calc cluster.
    
    (3) update centroid
    
    (4) Stop till the centroid isn't changed.
    

    
    
