#Support Vector Machine

###1.Summary
    Support vector machine is supervised learning models with associated learning algorithms that 
    
    analyze data used for classification and regression analysis. Given a set of training examples, 
    
    each marked for belonging to one of two categories, an SVM training algorithm builds a model that 
    
    assigns new examples into one category or the other, making it a non-probabilistic binary linear classifier. 
    
    Above paragraph is from English Wikipedia.
    
    Support vector machine is a classifier using the separating plane to classify the data.
    
    For the n-dimensional data separating plane is n-1 dimension

    For a plane, the separating plane is a straight line.
    
    We hope that the points on both sides of the plane are far from the plane as far as possible.
    
    The nearest point to the separation plane is called the margin.
    
    The support vector is the closest point.
    
    The goal is to maximize the distance between the support vectors and the separation plane.
    
###2.Derivation
    The derivation of support vector machine algorithm is difficult for me at first.
    
    (1) Constrained extremum problem of the two programming.
    
        Given a training sample set，(xi,yi), x repesents feature, y repesents class -1 or 1. 
        
        i repesents the number i sample.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=z%3Dw%5E%7BT%7Dx%5E%7B(i)%7D%2Bb%3Cbr%3E%0A%3Cbr%3E%0Ag%3D1%2Cz%5Cge%200%3Cbr%3E%0A%3Cbr%3E%0Ag%3D-1%2Cz%3C0" style="border:none;" />
        
        Function margin definition is shown as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%20%5Chat%7B%5Cgamma%7D%5E%7B(i)%7D%3Dy%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%7D%2Bb)" style="border:none;" />
        
        Therefore,function margin repesents that the features are the confidence of positive or negative.
        
        Geometric margin definition is shown as below.
        
<img src="http://images.cnblogs.com/cnblogs_com/jerrylead/201103/201103131131571364.png" height="309" width="360"/>

        Assume that B is on plane of WT+b=0,the distance from A to the surface is repesented by ri.
        
        B is the projection of A on the plane.if A is (xi，yi).B is show as below

<img src="http://chart.googleapis.com/chart?cht=tx&chl=x%3Dx%5E%7B(i)%7D-%5Cgamma%20%5E%7B(i)%7D%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=w%5E%7BT%7D(x%5E%7B(i)%7D-%5Cgamma%20%5E%7B(i)%7D%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D)%2Bb%3D0" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cgamma%20%5E%7B(i)%7D%20%3D%20%5Cfrac%7Bw%5E%7BT%7Dx%5E%7B(i)%7D%2Bb%7D%7B%7C%7Cw%7C%7C%7D%3D(%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D)%5E%7BT%7Dx%5E%7B(i)%7D%2B%5Cfrac%7Bb%7D%7B%7C%7Cw%7C%7C%7D" style="border:none;" />

        r is the distance from point to the plane.
        
        In other way.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cgamma%20%5E%7B(i)%7D%20%3Dy%5E%7B(i)%7D((%5Cfrac%7Bw%7D%7B%7C%7Cw%7C%7C%7D)%5E%7BT%7Dx%5E%7B(i)%7D%2B%5Cfrac%7Bb%7D%7B%7C%7Cw%7C%7C%7D)" style="border:none;" />

        When ||w|| is 1 , geometric margin is the function margin.
        
        The distance from nearest point to the plane is expressed by mathematical formula as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cgamma%20%3D%20min_%7Bi%3D1%2C...m%7D%5Cgamma%20%5E%7B(i)%7D" style="border:none;" />
        
        In other way, the purpose is to find a plane which is as far from as the nearest point.
        
        The formalization is show as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=max_%7B%5Cgamma%2Cw%2Cb%7D%5Cgamma%20%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%20%5Cgamma%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%7C%7Cw%7C%7C%3D1%0A" style="border:none;" />
        
        ||w||=1 constraint w. It's a geometric margin.
        
        Let's transfer it into a  function margin.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=max_%7B%5Cgamma%2Cw%2Cb%7D%20%5Cfrac%7B%5Cgamma%20%7D%7B%7C%7Cw%7C%7C%7D%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%20%5Cgamma%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%0A" style="border:none;" />

        Assume r is 1 and transfer min of 1/||w|| to  max of ||w||/2.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7B%5Cgamma%2Cw%2Cb%7D%20%5Cfrac%7B1%7D%7B2%7D%7C%7Cw%7C%7C%5E%7B2%7D%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%201%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%0A" style="border:none;" />

        It is a constrained extremum problem of the two programming. 
        
        First line is objective function which is convex function.
        
        Second line and third line is constraint function.
        
    (2) Lagrange multiplier method
    
        Generalized inequality constrained extremum problem：
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7Bw%7D%20f(w)%3Cbr%3E%0A%3Cbr%3E%0A%20%20%20%20s.t.%20g_%7Bi%7D(w)%5Cle%200%2Ci%3D1%2C...%2Ck%20%3Cbr%3E%0A%3Cbr%3E%0A%20%20%20%20h_%7Bi%7D(w)%3D0%2C%20i%3D1%2C...l%0A%0A" style="border:none;" />

        According to the lagrange multiplier method, we can get formula as below.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=L(w%2C%5Calpha%20%2C%20%5Cbeta%20)%3D%20f(w)%2B%5Csum_%7Bi%3D1%7D%5Ek%5Calpha_%7Bi%7Dg_%7Bi%7D(w)%2B%5Csum_%7Bi%3D1%7D%5El%5Cbeta_%7Bi%7Dh_%7Bi%7D(w)%0A" style="border:none;" />
        
        Define the following function.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta%20_%7Bp%7D%3Dmax_%7Bx%5Calpha.%5Cbeta%3A%20%5Calpha%5Cge%200%20%7D%20L(w%2C%5Calpha%2C%5Cbeta)" style="border:none;" />
        
        When w don't satisfy primal constraints,  
        
        it is possible to adjust alpha and beta to make theta get a max value which infinity. 
        
        When w satisfy primal constraints,
        
        theta is f(w).
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=Primal%20Problem%3Dmin_%7Bw%7Df(w)%3Dmin_%7Bw%7D%5Ctheta_%7Bp%7D(w)%3Dmin_%7Bw%7D%20max_%7B%5Calpha.%5Cbeta%3A%5Calpha%5Cge%200%7D%20L(w%2C%5Calpha%2C%5Cbeta)" style="border:none;" />

    (3) Duality problem
    
        Duality problem of primal problem is shown as below.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta%20_%7BD%7D(%5Calpha%2C%5Cbeta)%20%3D%20min_%7Bw%7D%20L(w%2C%5Calpha%2C%5Cbeta)%0A%3Cbr%3E%0A%3Cbr%3E%0Ad%5E%7B*%7D%3Dmax_%7B%5Calpha.%5Cbeta%3A%5Calpha%5Cge%200%7Dmin_%7Bw%7DL(w%2C%5Calpha%2C%5Cbeta)%3D%5Ctheta%20_%7BD%7D(%5Calpha%2C%5Cbeta)" style="border:none;" />
    
        Generally. Max Min(X) <= Min Max(X) is correct in any other function.
    
        Add KKT conditions ,which is shown as below, into the problem in order 
        
        to solve dual problem instead of primal problem.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20L(w%5E%7B*%7D%2C%5Calpha%5E%7B*%7D%2C%5Cbeta%5E%7B*%7D)%7D%0A%7Bw_%7Bi%7D%7D%3D0%2Ci%3D1%2C...%2Cn%3Cbr%3E%0A%5Cfrac%7B%5Cpart%20L(w%5E%7B*%7D%2C%5Calpha%5E%7B*%7D%2C%5Cbeta%5E%7B*%7D)%7D%7B%5Cbeta_%7Bi%7D%7D%3D0%2Ci%3D1%2C...%2Cl%3Cbr%3E%0A%0A%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha%5E%7B*%7D_%7Bi%7Dg_%7Bi%7D(w%5E%7B*%7D)%3D0%2Ci%3D1%2C...k%3Cbr%3E%0Ag_%7Bi%7D(w%5E%7B*%7D)%5Cle%200%2Ci%3D1%2C...k%3Cbr%3E%0A%5Calpha%5E%7B*%7D%5Cge%200%2Ci%3D1%2C...k%3Cbr%3E%0A%0A%0A" style="border:none;" />

        According KKT dual complementarity(the third line). The value of primal problem is the value of dual problem.
        
    (4) Optimum solution
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=min_%7B%5Cgamma%2Cw%2Cb%7D%20%5Cfrac%7B1%7D%7B2%7D%7C%7Cw%7C%7C%5E%7B2%7D%3Cbr%3E%0A%3Cbr%3E%0As.t.%20y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%5Cge%201%2Ci%3D1%2C...%2Cm%20%3Cbr%3E%0A%3Cbr%3E%0A%0A" style="border:none;" />

        Change constraints.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=g_%7Bi%7D(w)%3D-y%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)%2B1%5Cle%200%0A%0A" style="border:none;" />
    
        Add into the lagrange formula.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=L(w%2C%5Calpha%2Cb)%3D%5Cfrac%7B%7C%7Cw%7C%7C%5E%7B2%7D%7D%7B2%7D-%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7D%5By%5E%7B(i)%7D(w%5E%7BT%7Dx%5E%7B(i)%2Bb%7D)-1%5D%0A%0A" style="border:none;" />
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=d%5E%7B*%7D%3Dmax_%7B%5Calpha.%5Cbeta%3A%5Calpha%5Cge%200%7Dmin_%7Bw%7DL(w%2C%5Calpha%2C%5Cbeta)%0A" style="border:none;" />

        First, caclulate the min value which is about w and b.
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20L(w%2C%5Calpha%2Cb)%7D%7B%5Cpart%20w%7D%3Dw-%5Csum_%7Bi%3D1%7D%5Em%5Calpha_%7Bi%7Dy%5E%7B(i)%7Dx%5E%7B(i)%7D%3D0%0A%3Cbr%3E%0A%5Cfrac%7B%5Cpart%20L(w%2C%5Calpha%2Cb)%7D%7B%5Cpart%20b%7D%3D%5Csum_%7Bi%3D1%7D%5Emalpha_%7Bi%7Dy%5E%7B(i)%7D%3D0%0A" style="border:none;" />

        Add w into the lagrange formula.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=L(w%2C%5Calpha%2Cb)%3D%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7D-%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%2Cj%3D1%7D%5Em%20y%5E%7B(i)%7D%20y%5E%7B(j)%7D%20%5Calpha_%7Bi%7D%20%5Calpha_%7Bj%7D(x%5E%7B(i)%7D)%5E%7BT%7Dx%5E%7B(j)%7D%0A" style="border:none;" />

        Second, caclulate the max value which is about alpha.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=max_%7B%5Calpha%7D%20W(%5Calpha)%3D%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7D-%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5Em%20y%5E%7B(i)%7D%20y%5E%7B(j)%7D%5Calpha_%7Bi%7D%5Calpha_%7Bj%7D(x%5E%7B(i)%7D)%5E%7BT%7Dx%5E%7B(j)%7D%3Cbr%3E%0As.t.%5Calpha_%7Bi%7D%5Cge%200%2Ci%3D1%2C...%2Cm%3Cbr%3E%0A%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3D0%0A%0A%0A" style="border:none;" />
        
        before cacluation , Let's learn coordinate ascent method
        
        To solve this problem.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=max_%7B%5Calpha%7DW(%5Calpha_%7B1%7D%2C%5Calpha_%7B2%7D%2C...%2C%5Calpha_%7Bm%7D)" style="border:none;" />
        
        Except the Newton descent method and the gradient descent method, there is coordinate ascent method.
        
        All alpha except alpha-i are treated as a fixed value, W is a function of alpha-i.Directly optimize the alphai
        
        We would calculate optimiztion from i to m, or we would change the order to accelerate the convergence of W.
        
    (5) SMO 
        
        This section is from <<Sequential Minimal Optimization A Fast Algorithm for Training Support Vector Machines>>.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=W(%5Calpha)%3D%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7D-%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%2Cj%3D1%7D%5Em%20y%5E(i)y%5E(j)%5Calpha_%7Bi%7D%5Calpha_%7Bj%7D%3Cx%5E%7B(i)%7D.x%5E%7B(j)%7D%3E" style="border:none;" />
            
        From above we know this formula.
            
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3D0%0A%3D%3E%20%5Calpha_%7B1%7Dy%5E%7B(1)%7D%2B%5Calpha_%7B2%7Dy%5E%7B(2)%7D%3D-%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=w%3D%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7Dx%5E%7B(i)%7D%0A%3D%3E%20z%3Dw%5E%7BT%7Dx%2Bb%3D%5Csum_%7Bi%3D1%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3Cx%5E%7B(i)%7D.x%3E%2Bb" style="border:none;" />

        According to coordinate ascent method, calculation start from a1 and a2.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=W%3D%5Calpha_%7B1%7D%2B%5Calpha_%7B2%7D%2BConstant1-%0A%5Cfrac%7B1%7D%7B2%7D(y%5E%7B(1)2%7D%5Calpha_%7B1%7D%5E%7B2%7D%3Cx%5E%7B(1)%7D.x%5E%7B(1)%7D%3E%2By%5E%7B(1)%7Dy%5E%7B(2)%7D%5Calpha_%7B1%7D%5Calpha_%7B2%7D%3Cx%5E%7B(1)%7D.x%5E%7B(2)%7D%3E%2B" style="border:none;" />
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B1%7Dy%5E%7B(1)%7D%5Csum_%7Bi%3D3%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3Cx%5E%7B(i)%7D.x%5E%7B(1)%7D%3E%2By%5E%7B(2)%7Dy%5E%7B(1)%7D%5Calpha_%7B2%7D%5Calpha_%7B1%7D%3Cx%5E%7B(2)%7D.x%5E%7B(1)%7D%3E%2B%0A" style="border:none;" />
<img src="http://chart.googleapis.com/chart?cht=tx&chl=y%5E%7B(2)2%7D%5Calpha_%7B2%7D%5E%7B2%7D%3Cx%5E%7B(2)%7D.x%5E%7B(2)%7D%3E%2B%5Calpha_%7B2%7Dy%5E%7B(2)%7D%5Csum_%7Bi%3D3%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3Cx%5E%7B(i)%7D.x%5E%7B(2)%7D%3E)%0A" style="border:none;" />

        Assume that.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=k_%7Bij%7D%3D%3Cx%5E%7B(i)%7D.x%5E%7B(j)%7D%3E%3Cbr%3E%0A%3Cbr%3E%0Av_%7Bj%7D%3D%5Csum_%7Bi%3D3%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7Dk_%7Bji%7D%3Dz-b-y%5E%7B(1)%7D%5Calpha_%7B1%7D%5E%7B*%7Dk_%7B1i%7D-y%5E%7B(2)%7D%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B2i%7D" style="border:none;" />
        
        Add into W.
<img src="http://chart.googleapis.com/chart?cht=tx&chl=W%3D%5Calpha_%7B1%7D%2B%5Calpha_%7B2%7D%2BConstant1-%5Cfrac%7B1%7D%7B2%7D%5Calpha_%7B1%7D%5E%7B2%7Dk_%7B11%7D-%5Calpha_%7B1%7D%5Calpha_%7B2%7Dk_%7B12%7Dy%5E%7B(1)%7Dy%5E%7B(2)%7D-%5Calpha_%7B1%7Dy%5E%7B(1)%7DV_%7B1%7D-%5Cfrac%7B1%7D%7B2%7D%5Calpha_%7B2%7D%5E%7B2%7Dk_%7B22%7D-%5Calpha_%7B2%7Dy%5E%7B(2)%7DV_%7B2%7D" style="border:none;" />

        we can get this.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B1%7Dy%5E%7B(1)%7D%2B%5Calpha_%7B2%7Dy%5E%7B(2)%7D%3D-%5Csum_%7Bi%3D3%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3Cbr%3E" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%3D%3E%5Calpha_%7B1%7D%2B%5Calpha_%7B2%7Dy%5E%7B(2)%7Dy%5E%7B(1)%7D%3D-y%5E%7B(1)%7D%5Csum_%7Bi%3D3%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3Cbr%3E" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Set%3A%20S%3Dy%5E%7B(2)%7Dy%5E%7B(1)%7D%2CA%3D-y%5E%7B(1)%7D%5Csum_%7Bi%3D3%7D%5Em%20%5Calpha_%7Bi%7Dy%5E%7B(i)%7D%3Cbr%3E%0A%3D%3E%5Calpha_%7B1%7D%2B%5Calpha_%7B2%7DS%3DA" style="border:none;" />

       Add in to W.
<img src="http://chart.googleapis.com/chart?cht=tx&chl=W%3DA-S%5Calpha_%7B2%7D%2B%5Calpha_%7B2%7D-%5Cfrac%7B1%7D%7B2%7D(A-S%5Calpha_%7B2%7D)%5E%7B2%7Dk_%7B11%7D-Sk_%7B12%7D(A-S%5Calpha_%7B2%7D)%5Calpha_%7B2%7D-(A-S%5Calpha_%7B2%7D)y%5E%7B(1)%7Dv_%7B1%7D-%5Cfrac%7B1%7D%7B2%7D%5Calpha_%7B2%7D%5E%7B2%7Dk_%7B22%7D-y%5E%7B(2)%7D%5Calpha_%7B2%7Dv_%7B2%7D%2BConstant1" style="border:none;" />
    
        Calculate derivative and find the alpha2 which make derivative zero.
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20W%7D%7B%5Cpart%20%5Calpha_%7B2%7D%7D%3D1-S%2BSk_%7B11%7D(A-S%5Calpha_%7B2%7D)-Sk_%7B12%7D(A-2S%5Calpha_%7B2%7D)%2BSy%5E%7B(1)%7Dv_%7B1%7D-%5Calpha_%7B2%7Dk_%7B22%7D-y%5E%7B(2)%7Dv_%7B2%7D%3D0" style="border:none;" />
       
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%3D1-S%2BASk_%7B11%7D-K_%7B11%7D%5Calpha_%7B2%7D-ASk_%7B12%7D%2B2k_%7B12%7D%5Calpha_%7B2%7D%2By%5E%7B(2)%7Dv_%7B1%7D-%5Calpha_%7B2%7Dk_%7B22%7D-y%5E%7B(2)%7Dv_%7B2%7D%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%3DASk_%7B11%7D-ASk_%7B12%7D-%5Calpha_%7B2%7Dk_%7B11%7D-%5Calpha_%7B2%7Dk_%7B22%7D%2B2k_%7B12%7D%5Calpha_%7B2%7D%2By%5E%7B(2)%7D(v_%7B1%7D-v_%7B2%7D)%2By%5E%7B(2)%7D(y%5E%7B(2)%7D-y%5E%7B(1)%7D)%3D0%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B2%7Dk_%7B11%7D%2B%5Calpha_%7B2%7Dk_%7B22%7D-2k_%7B12%7D%5Calpha_%7B2%7D%3DASk_%7B11%7D-ASk_%7B12%7D%2By%5E%7B(2)%7D(v_%7B1%7D-v_%7B2%7D)%2By%5E%7B(2)%7D(y%5E%7B(2)%7D-y%5E%7B(1)%7D)%3D0%0A%0A" style="border:none;" />

        Add v into W.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B2%7Dk_%7B11%7D%2B%5Calpha_%7B2%7Dk_%7B22%7D-2k_%7B12%7D%5Calpha_%7B2%7D%3D%0A%0A" style="border:none;" />
<img src="http://chart.googleapis.com/chart?cht=tx&chl=ASk_%7B11%7D-ASk_%7B12%7D%2By%5E%7B(2)%7D(Z_%7B1%7D-b-y%5E%7B1%7D%5Calpha_%7B1%7D%5E%7B*%7Dk_%7B11%7D-y%5E%7B(2)%7D%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B21%7D-Z_%7B2%7D%2Bb%2By%5E%7B1%7D%5Calpha_%7B1%7D%5E%7B*%7Dk_%7B12%7D" style="border:none;" />
<img src="http://chart.googleapis.com/chart?cht=tx&chl=-y%5E%7B(2)%7D%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B22%7D)%2By%5E%7B(2)%7D(y%5E%7B(2)%7D-y%5E%7B(1)%7D)%3D0" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%3DASk_%7B11%7D-ASk_%7B12%7D-%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B21%7D%2B%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B22%7D%2BS%5Calpha_%7B1%7D%5E%7B*%7Dk_%7B12%7D-S%5Calpha_%7B1%7D%5E%7B*%7Dk_%7B11%7D%2By%5E%7B(2)%7D(Z_%7B1%7D-Z_%7B2%7D%2By%5E%7B(2)%7D-y%5E%7B(1)%7D)" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%3DASk_%7B11%7D-ASk_%7B12%7D-%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B21%7D%2B%5Calpha_%7B2%7D%5E%7B*%7Dk_%7B22%7D%2B%0A(AS-%5Calpha_%7B2%7D%5E%7B*%7D)(k_%7B12%7D-k_%7B11%7D)%2By%5E%7B(2)%7D(Z_%7B1%7D-Z_%7B2%7D%2By%5E%7B(2)%7D-y%5E%7B(1)%7D)" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B2%7D(k_%7B11%7D%2Bk_%7B22%7D-2k_%7B12%7D)%3D%5Calpha_%7B2%7D%5E%7B*%7D(k_%7B11%7D%2Bk_%7B22%7D-2k_%7B12%7D)%2By%5E%7B(2)%7D(Z_%7B1%7D-Z_%7B2%7D%2By%5E%7B(2)%7D-y%5E%7B(1)%7D)%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Set%3A%5Ceta%20%3D%20k_%7B11%7D%2Bk_%7B22%7D-2k_%7B12%7D%3Cbr%3E%0A%5Calpha_%7B2%7D%3D%5Calpha_%7B2%7D%5E%7B*%7D%2B%5Cfrac%7By%5E%7B(2)%7D(Z_%7B1%7D-Z_%7B2%7D%2By%5E%7B(2)%7D-y%5E%7B(1)%7D)%7D%7B%5Ceta%7D%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B2%7D%5E%7Bnew%7D%20%3D%20H%20%2C%20if%20%5Calpha_%7B2%7D%5Cge%20H%3Cbr%3E%0A%5Calpha_%7B2%7D%5E%7Bnew%7D%20%3D%20%5Calpha_%7B2%7D%20%2C%20if%20L%3C%5Calpha_%7B2%7D%3C%20H%3Cbr%3E%0A%5Calpha_%7B2%7D%5E%7Bnew%7D%20%3D%20L%20%2C%20if%20%5Calpha_%7B2%7D%5Cle%20%20L%3Cbr%3E%0A" style="border:none;" />
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7B1%7D%5E%7Bnew%7D%2BS%5Calpha_%7B2%7D%5E%7Bnew%7D%3D%5Calpha_%7B1%7D%5E%7B*%7D%2BS%5Calpha_%7B2%7D%5E%7B*%7D%3Cbr%3E%0A%3D%3E%5Calpha_%7B1%7D%5E%7Bnew%7D%3D%5Calpha_%7B1%7D%5E%7B*%7D%2BS(%5Calpha_%7B2%7D%5E%7B*%7D-%5Calpha_%7B2%7D%5E%7Bnew%7D)%0A" style="border:none;" />
        Supplement of calculation of H and L.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=0%20%5Cge%20%5Calpha%20%5Cle%20%20C%3Cbr%3E%0Aif%20y%5E%7B(1)%7D%20%5Cne%20y%5E%7B(2)%7D%20%3A%20%5Calpha_%7B1%7D-%5Calpha_%7B2%7D%3DK%3Cbr%3E%0AL%3Dmax(0%2C%5Calpha_%7B2%7D-%5Calpha_%7B1%7D)%3Cbr%3E%0AH%3Dmin(C%2CC%2B%5Calpha_%7B2%7D-%5Calpha_%7B1%7D)%3Cbr%3E" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=if%20y%5E%7B(1)%7D%20%3D%20y%5E%7B(2)%7D%20%3A%20%5Calpha_%7B1%7D%2B%5Calpha_%7B2%7D%3DK%3Cbr%3E%0AL%3Dmax(0%2C%5Calpha_%7B2%7D%2B%5Calpha_%7B1%7D-C)%3Cbr%3E%0AH%3Dmin(C%2C%5Calpha_%7B2%7D%2B%5Calpha_%7B1%7D)%3Cbr%3E" style="border:none;" />
