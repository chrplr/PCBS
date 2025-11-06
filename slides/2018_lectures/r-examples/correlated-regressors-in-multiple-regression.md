Correlated regressors in multiple regression
===========================================

It is often asserted that one two (or more) independent variables are correlated, this creates a problem in multiple regression. What problem? And when is it serious?

In multiple regression, the coefficients estimated for each regressor represents the influence of the associated variable *when the others are kept constant*.
It  is the "unique" contribution of this variable.




```r
require(mvtnorm)
```

```
## Loading required package: mvtnorm
```

```r
require(car)
```

```
## Loading required package: car
```

```r

n <- 100
a1 <- 0.2
a2 <- 0.3
nsim <- 100

for (cor in c(0, 0.2, 0.4, 0.6, 0.8)) {
    d <- rmvnorm(n, sigma = matrix(c(1, cor, cor, 1), nrow = 2))
    x1 <- d[, 1]
    x2 <- d[, 2]
    print(cor.test(x1, x2))
    print("VIF:")
    print(vif(lm(rnorm(n) ~ x1 + x2)))
    
    stats <- matrix(NA, nrow = nsim, ncol = 4)
    for (i in 1:nsim) {
        y <- a1 * x1 + a2 * x2 + rnorm(n)
        lmmod <- lm(y ~ x1 + x2)
        slm <- summary(lmmod)
        
        stats[i, ] <- as.numeric(slm$coefficients[2:3, 1:2])
    }
    boxplot(stats, main = cor, ylim = c(-0.2, 0.6))
    print(apply(stats, 2, summary))
}
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  x1 and x2
## t = -1.052, df = 98, p-value = 0.2955
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.29593  0.09269
## sample estimates:
##     cor 
## -0.1057 
## 
## [1] "VIF:"
##    x1    x2 
## 1.011 1.011
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-11.png) 

```
##            [,1]    [,2]   [,3]   [,4]
## Min.    -0.0575 -0.0218 0.0849 0.0883
## 1st Qu.  0.1310  0.2380 0.0971 0.1010
## Median   0.1940  0.3180 0.1020 0.1060
## Mean     0.1910  0.3200 0.1020 0.1060
## 3rd Qu.  0.2450  0.3870 0.1070 0.1120
## Max.     0.4620  0.6410 0.1190 0.1240
## 
## 	Pearson's product-moment correlation
## 
## data:  x1 and x2
## t = 3.226, df = 98, p-value = 0.001705
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  0.1208 0.4772
## sample estimates:
##    cor 
## 0.3099 
## 
## [1] "VIF:"
##    x1    x2 
## 1.106 1.106
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-12.png) 

```
##            [,1]   [,2]   [,3]   [,4]
## Min.    -0.0475 0.0762 0.0831 0.0948
## 1st Qu.  0.1290 0.2180 0.0968 0.1100
## Median   0.1890 0.2930 0.1030 0.1180
## Mean     0.2010 0.3060 0.1020 0.1170
## 3rd Qu.  0.2590 0.3940 0.1080 0.1230
## Max.     0.5000 0.6200 0.1190 0.1350
## 
## 	Pearson's product-moment correlation
## 
## data:  x1 and x2
## t = 1.413, df = 98, p-value = 0.1608
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.05668  0.32861
## sample estimates:
##    cor 
## 0.1413 
## 
## [1] "VIF:"
##   x1   x2 
## 1.02 1.02
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-13.png) 

```
##            [,1]   [,2]   [,3]   [,4]
## Min.    -0.0637 0.0181 0.0877 0.0847
## 1st Qu.  0.1540 0.2340 0.1010 0.0975
## Median   0.2220 0.2990 0.1060 0.1030
## Mean     0.2140 0.2990 0.1060 0.1020
## 3rd Qu.  0.2780 0.3650 0.1110 0.1070
## Max.     0.4820 0.5950 0.1220 0.1180
## 
## 	Pearson's product-moment correlation
## 
## data:  x1 and x2
## t = 7.951, df = 98, p-value = 3.23e-12
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  0.4900 0.7325
## sample estimates:
##    cor 
## 0.6262 
## 
## [1] "VIF:"
##    x1    x2 
## 1.645 1.645
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-14.png) 

```
##            [,1]    [,2]  [,3]  [,4]
## Min.    -0.0728 -0.0311 0.107 0.118
## 1st Qu.  0.1130  0.1960 0.125 0.139
## Median   0.1930  0.3130 0.134 0.148
## Mean     0.1940  0.2990 0.132 0.146
## 3rd Qu.  0.2850  0.3980 0.138 0.152
## Max.     0.5220  0.6010 0.155 0.171
## 
## 	Pearson's product-moment correlation
## 
## data:  x1 and x2
## t = 14.75, df = 98, p-value < 2.2e-16
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  0.7573 0.8827
## sample estimates:
##    cor 
## 0.8302 
## 
## [1] "VIF:"
##    x1    x2 
## 3.219 3.219
```

![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-15.png) 

```
##            [,1]    [,2]  [,3]  [,4]
## Min.    -0.1980 -0.0744 0.141 0.135
## 1st Qu.  0.0844  0.1980 0.168 0.161
## Median   0.2100  0.2800 0.178 0.170
## Mean     0.2130  0.2940 0.176 0.169
## 3rd Qu.  0.3410  0.4170 0.184 0.176
## Max.     0.6330  0.7520 0.206 0.198
```


