#Q1
# load in the data
work = read.table ("/Users/Desktop/workmandata.csv",sep =",",header =T)
str ( work )#kan type
work $ workman =as.factor(work$workman)
str ( work ) # double check the type of workman again
#a
with(work, tapply(y, workman, mean))
with(work, tapply(y, workman, sd))
with(work, boxplot(y ~ workman))
#The boxplot shows tha different workman has different average outputs as same as standard deviations.
#the 6th workman has the highest average ouput and the 7th workman has the lowest output.

#b
#null: output means for the ten workmen are equal
#alternative: at least one of the output means is different with others

anova(lm(y ~ workman, data = work))
#The p value is close to 0 indicating 
#we should reject the null hypothesis
#the result is very significant 
#as the p value is less than 0.001.

#c
res = residuals(lm(y ~ workman, data = work))
qqnorm(res)
qqline(res)
#There are points far from the fitted straight 
#line at the two ends especially at the tail indicating
#the assumptions of normality  may not be appropriate.

#d
bartlett.test(y ~ workman, data = work)
#The p value is  0.0007024 less 
#than 0.001 indicating a strong
#evidence against the null hypothesis 
#that the variances in each of the workman 
#are the same

#Q2

#a
library(MASS)
boxcox(lm(y ~ workman, data = work))
#The optimal lambda is close to -1, so we use -1. 
#Thus, the
#simple transformation on Y is inverse of Y.

#b
bartlett.test(1/y ~ workman, data = work)
#The p value is 0.9399 much larger than 0.05,
#so we can not reject he null hypothesis
#that the variances in each of the workman 
#are the same
#It is not agree with Q1-d

#c
anova(lm(1/y ~ workman, data = work))
#The p value is close to 0 
#indicating we should reject the 
#null hypothesis
#the result is very significant 
#as the p value is less than 0.001.
#It is agree with result we have in Q1-b.

res = residuals(lm(1/y ~ workman, data = work))
qqnorm(res)
qqline(res)
#Although there are points far from the fitted straight 
#line at  the tail 
#It is much better than the plot in Q1-c, 
#we now can consider the residuals are approximate normal.

#d
#we show above that under the second ANOVA, 
#the assumption of contant variance is satisfied
#by the bartlett test and 
#the assumption of the normality is 
#also can be considered satisfied,
#but they are not true in the first ANOVA,
#so we choose the second ANOVA.


#Q3
# load in the data
beers = read.table ('/Users/Desktop/beers.csv',sep =",",header =T)
str (beers)
#a
with(beers, tapply(rating, country, mean))
with(beers, tapply(rating, type, mean))
with(beers, tapply(rating, list(country,type), mean))

#b

boxplot(rating ~ country, data = beers)
boxplot(rating ~ type, data = beers)
#COUNTRY XIAO DE QU BIE
#TYPE DA DE QU BIE

#c
with(beer,interaction.plot(country,type,rating, col=c("blue","red"),lwd=2,type="b"))

#The IPA and USA is the LARGEST rating while the Lager 
#and Belgium has the lowest rating,
#The main effect of type is significant 
#as IPA is much higher than Lager across 3 countries,
#As the two lines are not paralleled,
#the interaction effect looks existing, for example,
#UK has the highest rating in type Lager 
#but the lowest in IPA.

#Q4 modify

#a
fit = lm(rating ~ country * type, data = beer)
anova(fit)

#The p value of type is  0.0001394 < 0.001 which means that
#The type effect is very  significant while the p value of country is
# 0.2935138 > 0.05 which means it is not significant effect.
#These results consistent with boxplots in Q3-b that there are not very 
#significant difference in the boxplots across countries but types.
#At last, the p value of interaction effect is 0.1129074 > 0.05 indicating a 
#not significant interaction effect.

#b
fit2 = lm(rating ~ country + type, data = beer)
anova(fit2)

#before refitting
res = residuals(fit)
qqnorm(res)
qqline(res)
#There are points far from the 
#line at the two ends obviously,
#so it looks like the normality is not true.
#after refitting
res2 = residuals(fit2)
qqnorm(res2)
qqline(res2)
#Now, there are only about 2 points
#far from the line at the head obviously, the points
#are supposed to be outliers, and overall, 
#we can think the normality is true.

#c

shapiro.test(res2)

#The Shapiro-Wilk Normality Test shows 
#that the p value is 0.1081 > 0.05, so it means
#that we can not reject the Normality 
#at 0.05 significance level. 
#So the formal Shapiro-Wilk Normality Test
#shows the normality is true.


#d

TukeyHSD(aov(rating ~ country + type, data = beers), which="country")





