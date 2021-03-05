Comparing two treatments
========================

christophe@pallier.org




In the previous section, the data from the two groups were assumed to be independent. If there is some pairing, for example if data were acquired in the same unit under two conditions, then the data are not independent. The simplest way to perform the data analysis is to  examine the differences between the two conditions computed over each unit.


Here data come organized a long table format with one measure per row, and condition and subject as variables. This less convenient to compute the differences within subjects than a short format with one subject per row, and one column per condition, but better to run linear model. To convert from one representation to the other, see stack, reshape2, plyr...





```r
tc <- read.csv("twotreat.csv")
head(tc)
```

```
##   X sub cond      y
## 1 1  s1    1 10.517
## 2 2  s1    2 12.011
## 3 3  s2    1  9.036
## 4 4  s2    2 10.430
## 5 5  s3    1  8.904
## 6 6  s3    2  9.397
```

```r
str(tc)
```

```
## 'data.frame':	40 obs. of  4 variables:
##  $ X   : int  1 2 3 4 5 6 7 8 9 10 ...
##  $ sub : Factor w/ 20 levels "s1","s10","s11",..: 1 1 12 12 14 14 15 15 16 16 ...
##  $ cond: int  1 2 1 2 1 2 1 2 1 2 ...
##  $ y   : num  10.52 12.01 9.04 10.43 8.9 ...
```

```r
tc$sub <- factor(tc$sub)  # make sure these vars are factors
tc$cond <- factor(tc$cond)
table(tc$sub)
```

```
## 
##  s1 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19  s2 s20  s3  s4  s5  s6  s7 
##   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2 
##  s8  s9 
##   2   2
```


(I assume that thereare no repeated measures within subject and treatment. If this is the case with your dataset, use aggregate or melt)

### Graphical explorations


```r
with(tc, interaction.plot(cond, sub, y))
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3.png) 


Fancier graphs can be obtained with lattice:


```r
require(lattice)
```

```
## Loading required package: lattice
```

```r
xyplot(y ~ cond, group = sub, data = tc, type = "l")
```

![plot of chunk unnamed-chunk-4](figure/unnamed-chunk-4.png) 



```r
xyplot(y ~ cond | sub, data = tc, type = "l")
```

![plot of chunk unnamed-chunk-5](figure/unnamed-chunk-5.png) 


We can also remove to main effects of subjects, as we are interested in the difference between condition within subjects:


```r
attach(tc)
tc$ycorr <- y + mean(y) - tapply(y, sub, mean)[sub]
detach(tc)
attach(tc)
par(mfcol = c(1, 2))
interaction.plot(cond, sub, y, main = "original data")
interaction.plot(cond, sub, ycorr, main = "after removing intersub var")
```

![plot of chunk unnamed-chunk-6](figure/unnamed-chunk-6.png) 

```r
par(mfcol = c(1, 1))
detach(tc)
```

### Descriptive stats

```r
with(tc, signif(tapply(y, cond, mean)))
```

```
##     1     2 
##  9.69 11.04
```

```r

# compute differences
c1 <- levels(tc$cond)[1]
c2 <- levels(tc$cond)[2]

s1 <- tc$sub[tc$cond == c1]
y1 <- tc$y[tc$cond == c1][order(s1)]

s2 <- tc$sub[tc$cond == c2]
y2 <- tc$y[tc$cond == c2][order(s2)]

summary(y1 - y2)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  -6.120  -1.780  -1.380  -1.350  -0.271   1.410
```

```r
se(y1 - y2)  # standard error of the effect
```

```
## [1] 0.4326
```

```r

# Check if the pairing was useful?
cor.test(y1, y2)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  y1 and y2
## t = 1.363, df = 18, p-value = 0.1897
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.1581  0.6592
## sample estimates:
##    cor 
## 0.3058
```


### Inferential stats


```r
t.test(y1, y2, paired = T)
```

```
## 
## 	Paired t-test
## 
## data:  y1 and y2
## t = -3.11, df = 19, p-value = 0.00577
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -2.2505 -0.4398
## sample estimates:
## mean of the differences 
##                  -1.345
```


Linear model approach


```r
(sm <- summary(model_lm <- lm(y ~ cond + sub, data = tc)))
```

```
## 
## Call:
## lm(formula = y ~ cond + sub, data = tc)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -2.389 -0.417  0.000  0.417  2.389 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)   10.591      0.991   10.69  1.8e-09 ***
## cond2          1.345      0.433    3.11   0.0058 ** 
## subs10        -0.832      1.368   -0.61   0.5502    
## subs11         0.268      1.368    0.20   0.8467    
## subs12        -0.563      1.368   -0.41   0.6855    
## subs13         0.587      1.368    0.43   0.6724    
## subs14        -0.642      1.368   -0.47   0.6440    
## subs15        -3.428      1.368   -2.51   0.0215 *  
## subs16        -0.614      1.368   -0.45   0.6585    
## subs17        -0.169      1.368   -0.12   0.9030    
## subs18        -1.996      1.368   -1.46   0.1608    
## subs19         0.488      1.368    0.36   0.7250    
## subs2         -1.531      1.368   -1.12   0.2770    
## subs20         0.756      1.368    0.55   0.5870    
## subs3         -2.113      1.368   -1.54   0.1389    
## subs4         -1.476      1.368   -1.08   0.2941    
## subs5         -0.975      1.368   -0.71   0.4845    
## subs6         -1.783      1.368   -1.30   0.2080    
## subs7          0.520      1.368    0.38   0.7082    
## subs8         -0.354      1.368   -0.26   0.7985    
## subs9         -4.165      1.368   -3.04   0.0067 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 1.37 on 19 degrees of freedom
## Multiple R-squared:  0.705,	Adjusted R-squared:  0.394 
## F-statistic: 2.27 on 20 and 19 DF,  p-value: 0.0399
```

```r
(diff <- sm$coefficients[2, "Estimate"])
```

```
## [1] 1.345
```

```r
(diffse <- sm$coefficients[2, "Std. Error"])
```

```
## [1] 0.4326
```



In this simple situation, mixed effect models will yield the same p-values:


```r

require(nlme)
```

```
## Loading required package: nlme
```

```r
(model_lme <- lme(y ~ cond, random = ~1 | sub, data = tc))
```

```
## Linear mixed-effects model fit by REML
##   Data: tc 
##   Log-restricted-likelihood: -74.81
##   Fixed: y ~ cond 
## (Intercept)       cond2 
##       9.690       1.345 
## 
## Random effects:
##  Formula: ~1 | sub
##         (Intercept) Residual
## StdDev:      0.9071    1.368
## 
## Number of Observations: 40
## Number of Groups: 20
```

```r
summary(model_lme)
```

```
## Linear mixed-effects model fit by REML
##  Data: tc 
##     AIC   BIC logLik
##   157.6 164.2 -74.81
## 
## Random effects:
##  Formula: ~1 | sub
##         (Intercept) Residual
## StdDev:      0.9071    1.368
## 
## Fixed effects: y ~ cond 
##             Value Std.Error DF t-value p-value
## (Intercept) 9.690    0.3670 19   26.40  0.0000
## cond2       1.345    0.4326 19    3.11  0.0058
##  Correlation: 
##       (Intr)
## cond2 -0.589
## 
## Standardized Within-Group Residuals:
##      Min       Q1      Med       Q3      Max 
## -1.97017 -0.63748 -0.05805  0.62255  1.52291 
## 
## Number of Observations: 40
## Number of Groups: 20
```

```r

# plot(ranef(model_lme)) plot(res_lme <- residuals(model_lme))
# qqnorm(res_lme) qqline(res_lme) plot(model_lme)
```



```r
require(lme4)
```

```
## Loading required package: lme4
## Loading required package: Matrix
## 
## Attaching package: 'lme4'
## 
## The following object is masked from 'package:nlme':
## 
##     lmList
```

```r
(model_lmer <- lmer(y ~ cond + (1 | sub), data = tc))
```

```
## Linear mixed model fit by REML ['lmerMod']
## Formula: y ~ cond + (1 | sub) 
##    Data: tc 
## REML criterion at convergence: 149.6 
## Random effects:
##  Groups   Name        Std.Dev.
##  sub      (Intercept) 0.907   
##  Residual             1.368   
## Number of obs: 40, groups: sub, 20
## Fixed Effects:
## (Intercept)        cond2  
##        9.69         1.35
```

```r
summary(model_lmer)
```

```
## Linear mixed model fit by REML ['lmerMod']
## Formula: y ~ cond + (1 | sub) 
##    Data: tc 
## 
## REML criterion at convergence: 149.6 
## 
## Random effects:
##  Groups   Name        Variance Std.Dev.
##  sub      (Intercept) 0.823    0.907   
##  Residual             1.871    1.368   
## Number of obs: 40, groups: sub, 20
## 
## Fixed effects:
##             Estimate Std. Error t value
## (Intercept)    9.690      0.367   26.40
## cond2          1.345      0.433    3.11
## 
## Correlation of Fixed Effects:
##       (Intr)
## cond2 -0.589
```

```r
# qqmath(ranef(model_lmer))
```


See http://freshbiostats.wordpress.com/2013/07/28/mixed-models-in-r-lme4-nlme-both/

Bootstrap confidence interval for the difference


```r
require(boot)
```

```
## Loading required package: boot
## 
## Attaching package: 'boot'
## 
## The following object is masked from 'package:lattice':
## 
##     melanoma
```

```r
samplemean <- function(x, d) {
    mean(x[d])
}
b <- boot(y1 - y2, samplemean, 1000)
boot.ci(b)
```

```
## Warning: bootstrap variances needed for studentized intervals
```

```
## BOOTSTRAP CONFIDENCE INTERVAL CALCULATIONS
## Based on 1000 bootstrap replicates
## 
## CALL : 
## boot.ci(boot.out = b)
## 
## Intervals : 
## Level      Normal              Basic         
## 95%   (-2.149, -0.510 )   (-2.122, -0.470 )  
## 
## Level     Percentile            BCa          
## 95%   (-2.221, -0.568 )   (-2.268, -0.590 )  
## Calculations and Intervals on Original Scale
```



### Plots

The errors bars can either represent the standard errors (or confidence intervals) of the means of each treatment, *or* the standard error bar for the difference between the two treatments when intersubject variability is taken out. 

First graphics: with the std.err. of the means:


```r
attach(tc)
par(mfrow = c(1, 1))

means <- tapply(y, cond, mean)
(ses <- tapply(y, cond, se))
```

```
##      1      2 
## 0.3571 0.3767
```

```r

ysca = c(min(means - 3 * ses), max(means + 3 * ses))

mp <- barplot(means, ylim = ysca, xpd = F)
arrows(mp, means - ses, mp, means + ses, code = 3, angle = 90)
```

![plot of chunk unnamed-chunk-13](figure/unnamed-chunk-13.png) 

```r

detach(tc)
```


If we remove the between Ss variability


```r
attach(tc)
par(mfrow = c(1, 1))

means <- tapply(y, cond, mean)
(ses <- tapply(ycorr, cond, se))
```

```
##      1      2 
## 0.2163 0.2163
```

```r

ysca = c(min(means - 3 * ses), max(means + 3 * ses))

mp <- barplot(means, ylim = ysca, xpd = F)
arrows(mp, means - ses, mp, means + ses, code = 3, angle = 90)
```

![plot of chunk unnamed-chunk-14](figure/unnamed-chunk-14.png) 

```r

detach(tc)
```


If we take the standard error from the regression:


```r
(sm <- summary(model_lm <- lm(y ~ cond + sub, data = tc)))
```

```
## 
## Call:
## lm(formula = y ~ cond + sub, data = tc)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -2.389 -0.417  0.000  0.417  2.389 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)   10.591      0.991   10.69  1.8e-09 ***
## cond2          1.345      0.433    3.11   0.0058 ** 
## subs10        -0.832      1.368   -0.61   0.5502    
## subs11         0.268      1.368    0.20   0.8467    
## subs12        -0.563      1.368   -0.41   0.6855    
## subs13         0.587      1.368    0.43   0.6724    
## subs14        -0.642      1.368   -0.47   0.6440    
## subs15        -3.428      1.368   -2.51   0.0215 *  
## subs16        -0.614      1.368   -0.45   0.6585    
## subs17        -0.169      1.368   -0.12   0.9030    
## subs18        -1.996      1.368   -1.46   0.1608    
## subs19         0.488      1.368    0.36   0.7250    
## subs2         -1.531      1.368   -1.12   0.2770    
## subs20         0.756      1.368    0.55   0.5870    
## subs3         -2.113      1.368   -1.54   0.1389    
## subs4         -1.476      1.368   -1.08   0.2941    
## subs5         -0.975      1.368   -0.71   0.4845    
## subs6         -1.783      1.368   -1.30   0.2080    
## subs7          0.520      1.368    0.38   0.7082    
## subs8         -0.354      1.368   -0.26   0.7985    
## subs9         -4.165      1.368   -3.04   0.0067 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 1.37 on 19 degrees of freedom
## Multiple R-squared:  0.705,	Adjusted R-squared:  0.394 
## F-statistic: 2.27 on 20 and 19 DF,  p-value: 0.0399
```

```r
diff <- sm$coefficients[2, "Estimate"]
diffse <- sm$coefficients[2, "Std. Error"]

attach(tc)
par(mfrow = c(1, 1))

means <- tapply(y, cond, mean)
(ses <- rep(diffse, length(means)))
```

```
## [1] 0.4326 0.4326
```

```r

ysca = c(min(means - 3 * ses), max(means + 3 * ses))

mp <- barplot(means, ylim = ysca, xpd = F)
arrows(mp, means - ses, mp, means + ses, code = 3, angle = 90)
```

![plot of chunk unnamed-chunk-15](figure/unnamed-chunk-15.png) 

```r

detach(tc)
```


A much nicer plot can be constructed, with confidence intervals for the means and for their difference (Cumming, Geoff, and Sue Finch. 2005. “Inference by Eye: Confidence Intervals and How to Read Pictures of Data.” American Psychologist 60 (2): 170–180.)



```r
attach(tc)
m1 <- t.test(y[cond == 1])$conf.int
m2 <- t.test(y[cond == 2])$conf.int
di <- diff(t.test(y1 - y2)$conf.int)
ysca <- c(min(c(m1, m2) - 0.1 * diff(range(c(m1, m2)))), max(c(m1, m2) + 0.1 * 
    diff(range(c(m1, m2)))))

plot(c(Gr1 = 1, Gr2 = 2, difference = 3), c(mean(m1), mean(m2), mean(m2)), pch = c(16, 
    16, 17), xlim = c(0.5, 3.5), ylim = ysca, axes = F, xlab = "", ylab = "")
axis(2, las = 1)
axis(1, at = 1:3, labels = c("cond1", "cond2", "difference"))
arrows(1:3, c(m1[1], m2[1], mean(m2) - di/2), 1:3, c(m1[2], m2[2], mean(m2) + 
    di/2), code = 3, angle = 90)
abline(h = mean(m1), lty = 2)
abline(h = mean(m2), lty = 2)
```

![plot of chunk unnamed-chunk-16](figure/unnamed-chunk-16.png) 

```r
detach(tc)
```



```r
require(gplots)
```

```
## Loading required package: gplots
## KernSmooth 2.23 loaded
## Copyright M. P. Wand 1997-2009
## 
## Attaching package: 'gplots'
## 
## The following object is masked from 'package:stats':
## 
##     lowess
```

```r
par(mfcol = (c(1, 2)))
plotmeans(y ~ cond, data = tc)
plotmeans(ycorr ~ cond, data = tc)
```

![plot of chunk unnamed-chunk-17](figure/unnamed-chunk-17.png) 

