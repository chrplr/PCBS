Interpreting the parameters of a linear model in a simple 2x2 anova design
===========================================================================
# Time-stamp: <2012-03-13 09:57 christophe@pallier.org>

First, let us create a 2x2 design, resulting from the crossing of binary factors 'a' and 'b': 


```r
a <- gl(2, 1, 4)
b <- gl(2, 2, 4)
means <- c(4, 6, 10, 15)
```


First, we fit an additive model without the interaction term.


```r
tapply(means, list(a = a, b = b), mean)
```

```
##    b
## a   1  2
##   1 4 10
##   2 6 15
```

```r
diff(tapply(means, list(a), mean))  # main effect of a
```

```
##   2 
## 3.5 
```

```r
diff(tapply(means, list(b), mean))  # main effect of b
```

```
##   2 
## 7.5 
```

```r


summary(mod2 <- lm(means ~ a + b))
```

```
## 
## Call:
## lm(formula = means ~ a + b)
## 
## Residuals:
##     1     2     3     4 
##  0.75 -0.75 -0.75  0.75 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)     3.25       1.30    2.50     0.24
## a2              3.50       1.50    2.33     0.26
## b2              7.50       1.50    5.00     0.13
## 
## Residual standard error: 1.5 on 1 degrees of freedom
## Multiple R-squared: 0.968,	Adjusted R-squared: 0.905 
## F-statistic: 15.2 on 2 and 1 DF,  p-value: 0.178 
## 
```

```r
model.matrix(mod2)
```

```
##   (Intercept) a2 b2
## 1           1  0  0
## 2           1  1  0
## 3           1  0  1
## 4           1  1  1
## attr(,"assign")
## [1] 0 1 2
## attr(,"contrasts")
## attr(,"contrasts")$a
## [1] "contr.treatment"
## 
## attr(,"contrasts")$b
## [1] "contr.treatment"
## 
```

```r
model.tables(aov(means ~ a + b))
```

```
## Tables of effects
## 
##  a 
## a
##     1     2 
## -1.75  1.75 
## 
##  b 
## b
##     1     2 
## -3.75  3.75 
```

```r
model.tables(aov(means ~ a * b))
```

```
## Tables of effects
## 
##  a 
## a
##     1     2 
## -1.75  1.75 
## 
##  b 
## b
##     1     2 
## -3.75  3.75 
## 
##  a:b 
##    b
## a   1     2    
##   1  0.75 -0.75
##   2 -0.75  0.75
```


Then, we fit a model including the interaction:


```r
par(las = 1)

interaction.plot(a, b, means, ylim = c(0, 17), legend = F, type = "b", pch = 16, 
    bty = "l")

eps = 0.9
text(1, 4 + eps, "a1b1")
text(2, 6 + eps, "a2b1")
text(1, 10 + eps, "a1b2")
text(2, 15 + eps, "a2b2")

lines(c(1, 2), c(10, 12), lty = 3)

arrows(1, 0, 1, 4, code = 3, length = 0.1)
arrows(2, 4, 2, 6, code = 3, length = 0.1)
arrows(1, 4, 1, 10, code = 3, length = 0.1)
arrows(2, 12, 2, 15, code = 3, length = 0.1)


mod1 = lm(means ~ a * b)
model.matrix(mod1)
```

```
##   (Intercept) a2 b2 a2:b2
## 1           1  0  0     0
## 2           1  1  0     0
## 3           1  0  1     0
## 4           1  1  1     1
## attr(,"assign")
## [1] 0 1 2 3
## attr(,"contrasts")
## attr(,"contrasts")$a
## [1] "contr.treatment"
## 
## attr(,"contrasts")$b
## [1] "contr.treatment"
## 
```

```r
summary(mod1)
```

```
## 
## Call:
## lm(formula = means ~ a * b)
## 
## Residuals:
## ALL 4 residuals are 0: no residual degrees of freedom!
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)        4         NA      NA       NA
## a2                 2         NA      NA       NA
## b2                 6         NA      NA       NA
## a2:b2              3         NA      NA       NA
## 
## Residual standard error: NaN on 0 degrees of freedom
## Multiple R-squared:    1,	Adjusted R-squared:  NaN 
## F-statistic:  NaN on 3 and 0 DF,  p-value: NA 
## 
```

```r

text(1.08, 2, "Intercept")  # intercept
text(2.08, 5, "a2")  # a2
text(1.08, 7.5, "b2")  # b2
text(2.08, 13, "a2:b2")  # a2:b2
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3.png) 



