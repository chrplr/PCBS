# display of parameters of lm in a simle 2x2 anova
# Time-stamp: <2012-03-13 09:57 christophe@pallier.org>

a=gl(2,1,4)
b=gl(2,2,4)
means=c(4,6,10,15)

# model with interaction
par(las=1)


interaction.plot(a,b,means,ylim=c(0,17),legend=F,type='b',pch=16,bty="l")

eps=.9
text(1,4+eps,"a1b1")
text(2,6+eps,"a2b1")
text(1,10+eps,"a1b2")
text(2,15+eps,"a2b2")

lines(c(1,2),c(10,12),lty=3)

arrows(1,0,1,4, code=3,length=.1)
arrows(2,4,2,6, code=3, length=.1)
arrows(1,4,1,10, code=3, length=.1)
arrows(2,12,2,15, code=3, length=.1)


mod1 = lm(means~a*b)
model.matrix(mod1)
summary(mod1)

text(1.08,2,"Intercept") # intercept
text(2.08,5,"a2") # a2
text(1.08,7.5,"b2") # b2
text(2.08,13,"a2:b2") # a2:b2

# additive model
tapply(means,list(a=a,b=b),mean)
diff(tapply(means,list(a),mean)) # main effect of a
diff(tapply(means,list(b),mean)) # main effect of b


summary(mod2<-lm(means~a+b))
model.matrix(mod2)
model.tables(aov(means~a+b))
model.tables(aov(means~a*b))
